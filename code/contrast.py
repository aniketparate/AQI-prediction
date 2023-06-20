import cv2

# Read the grayscale BMP image
image_path = 'data/img/2020_predict.bmp'
grayscale_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Convert the grayscale image to RGB
rgb_image = cv2.cvtColor(grayscale_image, cv2.COLOR_GRAY2RGB)

# Save the RGB image
output_image_path = 'data/img/2020_color_predict.bmp'
cv2.imwrite(output_image_path, rgb_image)

print("Image converted and saved successfully.")
