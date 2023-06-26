import csv
import math

def calculate_distance(rgb1, rgb2):
    r1, g1, b1 = rgb1
    r2, g2, b2 = rgb2
    return math.sqrt((r2 - r1) ** 2 + (g2 - g1) ** 2 + (b2 - b1) ** 2)

def find_closest_rgb(rgb, rgb_values):
    closest_rgb = None
    closest_distance = float('inf')
    for rgb_value in rgb_values:
        if rgb_value[:3] == [-1, -1, -1]:
            closest_rgb = [-1, -1, -1]
            return closest_rgb
        distance = calculate_distance(rgb, rgb_value[:3])
        if distance < closest_distance:
            closest_distance = distance
            closest_rgb = rgb_value
    return closest_rgb

# Read the RGB and temperature values from the first CSV file
with open('rgb_temperature_values.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    rgb_temperature_values = [list(map(int, row[:4])) for row in reader]

# Read the X, Y, r, g, b values from the second CSV file
with open('temperature_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    temperature_data = [list(map(int, row[:5])) for row in reader]

# Iterate over the temperature data and find the closest RGB value from the first file
for i, data in enumerate(temperature_data):
    closest_rgb = find_closest_rgb(data[2:5], rgb_temperature_values)
    temperature_data[i][2:5] = closest_rgb[:3]

# Write the updated X, Y, r, g, b values to a new CSV file
with open('updated_csv_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['X', 'Y', 'r', 'g', 'b'])
    writer.writerows(temperature_data)
