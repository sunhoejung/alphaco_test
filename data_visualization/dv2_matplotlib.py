import matplotlib.pyplot as plt

# Prepare the data
dates = [
    '2021-01-01', '2021-01-02', '2021-01-03', '2021-01-04', '2021-01-05',
    '2021-01-06', '2021-01-07', '2021-01-08', '2021-01-09', '2021-01-10'
]
min_temperature = [20.7, 17.9, 18.8, 14.6, 15.8, 15.8, 15.8, 17.4, 21.8, 20.0]
max_temperature = [34.7, 28.9, 31.8, 25.6, 28.8, 21.8, 22.8, 28.4, 30.8, 32.0]

# Create a plot using the object-oriented approach in matplotlib
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the data
ax.plot(dates, min_temperature, label='Min Temperature', marker='o', linestyle='-')
ax.plot(dates, max_temperature, label='Max Temperature', marker='o', linestyle='-')

# Set labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Min and Max Temperatures (January 2021)')

# Rotate x-axis labels for better readability
ax.set_xticklabels(dates, rotation=45)

# Add legend
ax.legend()

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
