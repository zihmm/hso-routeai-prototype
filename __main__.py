import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as ts
from keras import Sequential
from keras import layers

# Parse generated route data
csv_routes = pd.read_csv('data/dataset_acme_routes.csv', sep=";")

# Convert route date and times to numeric values (for scaling)
csv_routes['date'] = pd.to_datetime(csv_routes['date'], format='%d.%m.%Y').apply(lambda date: date.toordinal())
csv_routes['start_at']= csv_routes['start_at'].apply(lambda time: int(time.split(':')[0]) * 60 + int(time.split(':')[1]))
csv_routes['arrived_at']= csv_routes['arrived_at'].apply(lambda time: int(time.split(':')[0]) * 60 + int(time.split(':')[1]))

# Features & labels
features = csv_routes[
    ['date', 'start_at', 'arrived_at', 'duration_in_m', 'is_rush_hour', 'weather_conditions', 'seasonal_happening', 'traffic_density']
]

target = csv_routes['duration_in_m']

# Preprocess and normalize data
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split train and test data
train_features, train_target, test_features, test_target = train_test_split(features_scaled, target, test_size=.3, random_state=42)

# Initialize network
model = Sequential([
    layers.Dense(100, activation='relu', input_shape=(train_features.shape[1],)),  # Hidden 1, 100 Neurons (not validated)
    layers.Dense(100),  # Hidden 2, 100 Neurons (not validated)
    layers.Dense(1)  # Output, 1 Neuron is enough
])

model.compile(optimizer="adam", loss="mse", metrics=["mae"])

# Train the model
model.fit(train_features, test_features, epochs=100, validation_split=0.3)

# TODO Validatae the model