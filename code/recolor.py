import cv2
import numpy as np
import pandas as pd

# Read the CSV file
data = pd.read_csv('updated_csv_file.csv')

# Get the maximum row and column values
max_row = data['Y'].max()
max_column = data['X'].max()

# Create a blank image with the size based on the maximum row and column values
image = np.zeros((max_row + 1, max_column + 1, 3), dtype=np.uint8)

# Iterate over the rows of the CSV data
for index, row in data.iterrows():
    r, c, red, green, blue = row['Y'], row['X'], row['r'], row['g'], row['b']
    image[r, c] = (blue, green, red)  # Set the pixel value in the image

# Display the image
# cv2.imshow('Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Save the reconstructed image
output_image_path = "output_image.bmp"
cv2.imwrite(output_image_path, image)

print("Image saved successfully.")
