import numpy as np

# Input is an RGB numpy array with shape (height, width, 3), can be uint, int, float, or double, values expected in the range 0..255
# Output is a double YUV numpy array with shape (height, width, 3), values in the range 0..255
def RGB2YUV(rgb):
    m = np.array([[0.29900, -0.16874, 0.50000],
                  [0.58700, -0.33126, -0.41869],
                  [0.11400, 0.50000, -0.08131]])

    yuv = np.dot(rgb, m)
    yuv[1] += 128.0
    yuv[2] += 128.0
    return yuv

# Input is a YUV numpy array with shape (height, width, 3), can be uint, int, float, or double, values expected in the range 0..255
# Output is a double RGB numpy array with shape (height, width, 3), values in the range 0..255
def YUV2RGB(yuv):
    m = np.array([[1.0, 1.0, 1.0],
                  [-0.000007154783816076815, -0.3441331386566162, 1.7720025777816772],
                  [1.4019975662231445, -0.7141380310058594, 0.00001542569043522235]])

    rgb = np.dot(yuv, m)
    rgb[0] -= 179.45477266423404
    rgb[1] += 135.45870971679688
    rgb[2] -= 226.8183044444304
    return rgb

# ---- 1 ----

# Prompt the user for RGB values
R = float(input("Enter R value (0-255): "))
G = float(input("Enter G value (0-255): "))
B = float(input("Enter B value (0-255): "))
rgb_array = np.array([R, G, B])

# Convert RGB to YUV and print the result
yuv_result = RGB2YUV(rgb_array)
print("RGB to YUV:")
print(yuv_result)

# Prompt the user for YUV values
Y = float(input("Enter Y value (0-255): "))
U = float(input("Enter U value (0-255): "))
V = float(input("Enter V value (0-255): "))
yuv_array = np.array([Y, U, V])

# Convert YUV to RGB and print the result
rgb_result = YUV2RGB(yuv_array)
print("YUV to RGB:")
print(rgb_result)

# Give an RGB value inside a numpy array to convert it to YUV
# print(RGB2YUV(np.array([50, 12, 200]))

# Give a YUV value inside a numpy array to convert it to RGB
# print(YUV2RGB(np.array([44.794, 215.58788, 131.71372]))
