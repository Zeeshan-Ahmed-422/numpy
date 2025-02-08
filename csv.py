import csv

# Define the header and data
header = ['Date', 'Temperature', 'Humidity', 'WindSpeed', 'Precipitation']
data = [
    ['2024-11-01', 22.5, 65, 12, 0.2],
    ['2024-11-02', 24.1, 60, 10, 0.0],
    ['2024-11-03', 19.8, 70, 8, 0.5],
    ['2024-11-04', 21.3, 68, 15, 0.0],
]

# Create and write to the CSV file
with open('weather_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)  # Write the header
    writer.writerows(data)   # Write the data rows

print("weather_data.csv file created successfully!")
