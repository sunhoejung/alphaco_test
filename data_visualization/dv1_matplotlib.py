# matplotlib 기본 문법
import matplotlib.pyplot as plt

# Prepare the data
dates = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
    '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'
]
min_temperature = [20.7, 17.9, 18.8, 14.6, 15.8, 15.8, 15.8, 17.4, 21.8, 20.0]
max_temperature = [34.7, 28.9, 31.8, 25.6, 28.8, 21.8, 22.8, 28.4, 30.8, 32.0]

# Create a plot
plt.figure(figsize=(10, 5))
plt.plot(dates, min_temperature, label='Min Temperature', marker='o', linestyle='-')
plt.plot(dates, max_temperature, label='Max Temperature', marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Min and Max Temperatures (January 2021)')
plt.xticks(rotation=45)
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
