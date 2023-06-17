import csv
import cv2
import numpy as np

# Read the CSV file containing pixel color values
csv_path = '2000_LST.csv'

rows = []
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        rows.append(row)

# Determine the dimensions of the image
max_row = max(int(row[0]) for row in rows)
max_col = max(int(row[1]) for row in rows)

# Create an empty image with original color dimensions
reconstructed_image = np.zeros((max_row + 1, max_col + 1, 3), dtype=np.uint8)

# Set pixel color values based on the CSV data
for row in rows:
    r, c, b, g, r = map(int, row)  # Assuming CSV format: "Row", "Column", "Blue", "Green", "Red"
    reconstructed_image[r, c] = (b, g, r)

# Save the reconstructed image
output_image_path = "output_image.bmp"
cv2.imwrite(output_image_path, reconstructed_image)

print("Image saved successfully.")
