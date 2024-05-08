# RouteAI Prototype
Simple prototype to analyze route data to predict drive time in the future under certain conditions 

This ist just an experimental project to learn about the TensorFlow and Keras Framework. **Dont use in production**

Used as prototype for HSO KI professional course project.

## Feature Engineering

### weather_condition
Historical weatherconditions with impact on road conditions.

| Description | Value                                                      |
|-------------|------------------------------------------------------------|
| 1           | Very bad condittions (e.g. heavy snowfall, very icy roads) |
| 2           | Bad conditions (e.g. snow, icy roads)                      |
| 3           | Normal conditions                                          |
| 4           | Good conditions                                            |
| 5           | Very good conditions                                       |

### is_rushhour
Rush hour in switzerland; on workdays from 7:00 to 9:00, 11:30 to 13:00 and 16:30 to 18:00

| Description         | Value |
|---------------------|-------|
| Is not in rush hour | 0     |
| Is in rush hour     | 1     |

### traffic_density
Road traffic density

| Description | Value                               |
|-------------|-------------------------------------|
| 1           | Heavy traffic (e.g. road accidents) |
| 3           | Normal conditions                   |
| 4           | Good conditions                     |

