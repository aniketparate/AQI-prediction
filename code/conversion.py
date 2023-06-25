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
        distance = calculate_distance(rgb, rgb_value)
        if distance < closest_distance:
            closest_distance = distance
            closest_rgb = rgb_value
    return closest_rgb

# Read the RGB values from the first CSV file
with open('first_csv_file.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    rgb_values = [list(map(int, row[:3])) for row in reader]

# Read the RGB values from the second CSV file
with open('second_csv_file.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row if it exists
    rgb_values_to_update = [list(map(int, row[:3])) for row in reader]

# Iterate over the RGB values in the second file and find the closest RGB value from the first file
for i, rgb_value_to_update in enumerate(rgb_values_to_update):
    closest_rgb = find_closest_rgb(rgb_value_to_update, rgb_values)
    rgb_values_to_update[i] = closest_rgb

# Write the updated RGB values to a new CSV file
with open('updated_csv_file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['R', 'G', 'B'])
    writer.writerows(rgb_values_to_update)
