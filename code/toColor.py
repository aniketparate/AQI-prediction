import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Open the grayscale temperature map
image = Image.open('data\img\grey_2020.bmp').convert('L')  # Convert to grayscale

# Convert the grayscale image to a numpy array
image_array = np.array(image)

# Define the desired color range
color_min = 20  # Minimum temperature value for the color range
color_max = 200  # Maximum temperature value for the color range

# Create a mask for the black background
background_mask = image_array > 0

# Normalize the grayscale image to the range [0, 1]
normalized_image = image_array / 255.0
# normalized_image = (image_array - color_min) / (color_max - color_min)
# normalized_image = np.clip(normalized_image, 0, 1)

# Apply the colormap to the normalized image
cmap = plt.cm.get_cmap('RdYlGn')  # Choose the colormap (RdYlGn: red to yellow to green)
color_map = cmap(normalized_image)

# Apply the background mask to the color map
color_map[~background_mask] = [0, 0, 0, 0]  # Set non-background pixels as transparent

# Convert the color map to an RGB image
color_image = Image.fromarray((color_map[:, :, :3] * 255).astype(np.uint8), mode='RGB')

# Show the color image
color_image.show()

# Save the color image
# color_image.save('temp_map_color.jpg')
