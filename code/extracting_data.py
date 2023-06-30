import csv
import cv2

# Load the BMP image
image_path = './2000_LST.bmp'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get the dimensions of the grayscale image
height, width = gray_image.shape

# Create a CSV file to store the pixel color values
csv_path = '2000_LST.csv'

with open(csv_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Row", "Column", "Pixel Value"])  # Write header
    
    # Write pixel color values to CSV
    for row in range(height):
        for col in range(width):
            pixel_value = gray_image[row, col]
            writer.writerow([row, col, pixel_value])

print("CSV file created successfully.")
