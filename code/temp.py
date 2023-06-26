import numpy as np
import csv
from PIL import Image

# Open the temperature color map image
image = Image.open('./data/img/og/2020_LST.bmp')

# Convert the image to numpy array
image_array = np.array(image)

# Define the temperature range
min_temp = 0  # Minimum temperature in degrees Celsius
max_temp = 50  # Maximum temperature in degrees Celsius

# Convert RGB to temperature values
temperature_data = []
height, width, _ = image_array.shape
for y in range(height):
    for x in range(width):
        pixel = image_array[y, x]
         # Interpolate temperature value based on pixel color
        r, g, _ = pixel
        temperature = min_temp + (max_temp - min_temp) * (1 - g / 255)
        temperature_data.append([x, y, temperature])  # Save spatial coordinates and temperature

# Save temperature data to CSV file
with open('temperature_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['X', 'Y', 'Temperature'])  # Header row
    writer.writerows(temperature_data)

print("Temperature data extracted and saved to temperature_data.csv")
