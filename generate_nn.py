from pymongo import MongoClient
import os
from dotenv import load_dotenv

# recognise 3d/2d objects

# overlay conclusions

# add to working memory (spatial + meaning data)

# neuron density functions

# no density function required, simply allocate different amounts of neurons

# MEANING ISN'T ALLOCATED ON TOP OF 3D DATA DIRECTLY!!! IT'S LAYERED OVER INDIVIDUAL OBJECT DATA

# 3D DATA IS DETACHED ASAP , THEN REATTACHED ONCE A CONCEPT IS DETERMINED TO BE MEANINGFUL (TRIGGERS CONCLUSION/POSEM ATTACHED NEOCORTICAL NEURONS)

# how much of the conceptual subcomponents is added to the 3d data in short term memory? how does peripheral aiming relate to this?
# how does grabbing something relate to this?

# standard density (until 0.85), remember that this function runs twice, symmetrically
# y=0.1x+0.18
# 10 connections

# until fovea (0.85 -> 0.96)
# y=5.4x−4.23
# 16 connections

# fovea (0.96 - 1)
# y=2
# 25 connections?

# 3 additional physical detachment layers
# identical number of neurons
# 16 connections

# 2 layers of conclusion
# one third the neurons
# 10 connections


# turn input image into a black and white image at first

# test with cam
def generate_fovea_array(black_white_image: list, fovea_pixel_diameter: int):
    img = black_white_image
    rows = len(img)
    horiz_pixels = len(img[0])
    base_layer_object = {}

    # find way to log these more easily
    fovea_border_top_index = (rows / 2) - (fovea_pixel_diameter / 2)
    fovea_border_right_index = (horiz_pixels / 2) + (fovea_pixel_diameter / 2)
    fovea_border_bottom_index = (rows / 2) + (fovea_pixel_diameter / 2)
    fovea_border_left_index = (horiz_pixels / 2) - (fovea_pixel_diameter / 2)

    # black and white means only one int per pixel
    # [[row array], [row array], ...]
    # just define pixels where the fovea exists

    for i in range(0, rows):
        for j in range(0, horiz_pixels):
            # img[i][j] is current pixel
            # print(img[i][j])
            if (fovea_border_left_index < j < fovea_border_right_index and fovea_border_top_index < i < fovea_border_bottom_index):
                img[i][j] = True
                # print(i)
                # print(j)
                if (i == 261 and j == 344):
                    print(img[i][j])
            else:
                img[i][j] = False

    # i have to convert this into an array (or 2) that can take in the image input data
    # print(img[0])
    # print("should be false: ")
    # print(img[1][1])
    # print(img[239][319])
    # print("should be true: ")
    return img


def generate_layers_1_and_2_from_fovea_array(fovea_array: list, fovea_density: float, fovea_connections: int, periph_density: float, periph_connections: int):
    layer_1 = []
    layer_2 = []
    connections = []

    for i in range(0, len(fovea_array)):
        for j in range(0, len(fovea_array[i])):
            current_neuron = {
                "id":  "x" + str(j) + "y" + str(i) + "z" + str(1),
                "count": i + j,
                "activation_lvl": 0,
                "negative_y_coordinate": i,
                "positive_x_coordinate": j,
                "connections": {
                    "x0y0z0": 0.8
                },
                "next_layer_absolute_density": fovea_density if fovea_array[i][j] == True else periph_density,
                "connections_to_next_layer": fovea_connections if fovea_array[i][j] == True else periph_connections,
            }
            layer_1.append(current_neuron)
    print("layer_1 first neuron" + str(current_neuron))

    next_neuron_counter_x = 0
    next_neuron_counter_y = 0


def return_squares_with_data(fovea_array):
    squares_arr = []
    current_square = {}
    current_pixel = 0
    for i in range(0, len(fovea_array)):
        for j in range(0, len(fovea_array[i])):
            current_pixel = fovea_array[i][j]

            # find x axis width of square
            if ("top-right" not in current_square and "top-left" not in current_square):
                current_square["top-left"] = j

            if ("top-right" not in current_square):
                current_square["top_right"] = i
            elif (current_square["top-right"] < j):
                current_square["top_right"] = j

            if "top_left" not in current_square and "type" not in current_square:
                # corner pixels are [x, y]
                current_square["top_left"]["x"] = j
                current_square["top_left"]["y"] = i
                current_square["type"] = current_pixel
            elif (current_pixel is not current_square["type"] or j is len(fovea_array[i])):
                # right end of square
                break

            # remember to set current_square = {} at end of square


def find_square_height(top_left: dict, top_right: dict, fovea_array: list, pixel_type):
    max_x_index = len(fovea_array[0]) - 1
    square_height = 1
    for row in range(0, len(fovea_array)):
        for pixel_index in range(top_left["x"], top_right["x"]):
            current_pixel = fovea_array[row][pixel_index]

            if (current_pixel is pixel_type):
                if (max_x_index is not pixel_index):
                    next_pixel = fovea_array[row][pixel_index + 1]
                    if (next_pixel is not pixel_type):

                        # first condition is for error handling so the script doesn't try to read index 480 which doesn't exist
                        # if len(fovea_array[0]) is not top_right - 1 and pixel_index is top_right["x"] + 1 and pixel_type is current_pixel:
                        # return square_height

                        # if fovea_array[row][pixel_index] is not pixel_type:
load_dotenv()

mongLink = os.getenv('MONGO_URI')

print(mongLink)

cluster = MongoClient(mongLink)
db = cluster["abgi"]
collection = db["p1_neurons"]

layers_neurons_data = [[], [], [], []]


# collection.insert_one()
