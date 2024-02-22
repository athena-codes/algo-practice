import numpy as np
import pandas as pd

# Generate fake maintenance data
np.random.seed(0)

# Number of samples
n_samples = 1000

# Time to failure (in days)
time_to_failure = np.random.randint(1, 365, size=n_samples)

# Failure event (1: failure occurred, 0: no failure)
failure_event = np.random.choice([0, 1], size=n_samples, p=[0.9, 0.1])

# Sensor readings (fake sensor data)
sensor_data = pd.DataFrame(np.random.randn(n_samples, 5), columns=['sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5'])

# Combine data into a DataFrame
maintenance_data = pd.DataFrame({'time_to_failure': time_to_failure,
                                 'failure_event': failure_event})
maintenance_data = pd.concat([maintenance_data, sensor_data], axis=1)

# Print the first few rows of the dataset
print(maintenance_data.head())
