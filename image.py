import cv2
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

def detect_colors(image_path, top_n=3):
    # Read the image
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize to reduce computation
    img_resized = cv2.resize(img, (150, 150), interpolation=cv2.INTER_AREA)

    # Reshape image to a list of pixels
    pixels = img_resized.reshape((-1, 3))
    pixels_list = [tuple(pixel) for pixel in pixels]

    # Count colors
    counter = Counter(pixels_list)
    most_common = counter.most_common(top_n)

    print("\n🎨 Top Colors:")
    colors = []
    for i, (color, count) in enumerate(most_common):
        rgb = np.array(color)
        percentage = (count / len(pixels_list)) * 100
        print(f"{i+1}. RGB{tuple(rgb)}  →  {percentage:.2f}%")
        colors.append(rgb / 255.0)

    # Display the colors
    plt.figure(figsize=(8, 2))
    plt.title("Top Colors in Image")
    plt.axis('off')
    plt.imshow([colors])
    plt.show()

# Example usage
detect_colors(r"D:\100 days of 100 projects\Day46 Image Color Detector\download.png")
