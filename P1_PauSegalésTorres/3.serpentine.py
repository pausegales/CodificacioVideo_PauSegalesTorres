import numpy as np
from PIL import Image

def serpentine(image_filepath):
    #Loading image (expecting rgb (3-Dimensional array))
    image = Image.open(image_filepath)
    image_data = image.load()
    width, height = image.size
    #Initiating the storing matrix
    serpent = []

    #print(np.shape(image))

    x, y = 0, 0
    direction = 1  # 1 for moving down-right, -1 for moving up-right

    # Iterate over each pixel in a diagonal serpentine pattern
    while x < width and y < height:
        r, g, b = image_data[x, y]
        serpent.append((r, g, b))

        # Check for boundaries and change direction
        if direction == 1:
            if x + 1 < width and y - 1 >= 0:
                x += 1
                y -= 1
            else:
                if x + 1 < width:
                    x += 1
                else:
                    y += 1
                direction = -1
        else:
            if x - 1 >= 0 and y + 1 < height:
                x -= 1
                y += 1
            else:
                if y + 1 < height:
                    y += 1
                else:
                    x += 1
                direction = 1
    return serpent


# ---- 3 ----
iterated_serpentine = serpentine("baixa.jpeg")