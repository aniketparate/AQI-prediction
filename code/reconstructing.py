import csv
import cv2
import numpy as np

# Read the CSV file containing pixel color values
csv_path = 'data/csv/2010_predict.csv'

rows = []
with open(csv_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header
    for row in reader:
        rows.append(row)

# Determine the dimensions of the image
max_row = max(int(row[0]) for row in rows)
max_col = max(int(row[1]) for row in rows)

# Create an empty image with grayscale dimensions
reconstructed_image = np.zeros((max_row + 1, max_col + 1), dtype=np.uint8)

# Set pixel values based on the CSV data
for row in rows:
    r, c, pixel_value = map(int, row)
    reconstructed_image[r, c] = pixel_value

# Display the reconstructed image
output_image_path = 'data/img/2010_predict.bmp'
cv2.imwrite(output_image_path, reconstructed_image)
# cv2.imshow("Reconstructed Image", reconstructed_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
