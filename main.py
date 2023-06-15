import cv2
import numpy as np

def calculate_temperature(r,g,b):
    # Convert RGB values to range [0, 1]
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # Define temperature range
    hot_temperature = 100.0
    cold_temperature = 0.0

    # Map RGB values to temperature based on color mapping
    temperature = (1 - r) * hot_temperature + (1 - g) * cold_temperature

    return temperature

def map_temperature_to_color(temperature):
    hot_color = (0, 0, 255)      # Red
    cold_color = (0, 255, 0)     # Green
    moderate_color = (255, 165, 0)  # Orange

    # Map temperature to color based on temperature ranges
    if temperature >= 80.0:
        return hot_color
    elif temperature <= 40.0:
        return cold_color
    else:
        return moderate_color

image = cv2.imread('2000_LST.bmp', cv2.IMREAD_COLOR)

if image is not None:
    greyscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(greyscale, 0, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    temperature_data = []
    for coutour in contours:
        for point in coutour:

            pixel = image[point[0][1], point[0][0]]
            r, g, b = pixel[2], pixel[1], pixel[0]

            temperature = calculate_temperature(r,g,b)
            temperature_data.append(temperature)


    temperature_map = np.zeros_like(image, dtype=np.uint8)
    for contour in contours:
        avg_temperature = np.mean(temperature_data)
        color = map_temperature_to_color(avg_temperature)
        cv2.drawContours(temperature_map, [contour], -1, color, thickness=cv2.FILLED)


    print(temperature_data)

    # image_with_contours = cv2.drawContours(image.copy(), contours, -1, (0, 0, 255), 2)
    cv2.imshow('Temperature Map', temperature_map)
    cv2.namedWindow('Temperature Map', cv2.WINDOW_NORMAL)

    cv2.imshow('Image with Contours', image)
    cv2.namedWindow('Image with Contours', cv2.WINDOW_NORMAL)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Failed to load the image')


# 1. import cv2 and numpy
# 2. define a function to calculate temperature
# 3. define a function to map temperature to color
# 4. load the image
# 5. convert the image to greyscale
# 6. apply threshold to the greyscale image
# 7. find contours in the thresholded image
# 8. iterate over the contours
# 9. iterate over the pixels within the contour
# 10. get the RGB values of the pixel
# 11. calculate the temperature of the pixel
# 12. append the temperature to the temperature_data list
# 13. calculate the average temperature of the contour
# 14. map the average temperature to a color
# 15. draw the contour on the temperature map
# 16. display the temperature map
# 17. display the image with contours
# 18. wait for a key press
# 19. close all windows
# 20. else print a message
