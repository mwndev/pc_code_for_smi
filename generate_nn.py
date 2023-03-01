from pymongo import MongoClient
import os
from dotenv import load_dotenv
import math
import operator
import bisect
from mafs import binary_search

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

# for loop with floats
def decimal_range(start, stop, increment):
    while start < stop:  # and not math.isclose(start, stop): Py>3.5
        yield start
        start += increment

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

    for row in range(0, rows):
        for col in range(0, horiz_pixels):
            # img[row][col] is current pixel
            if (fovea_border_left_index < col < fovea_border_right_index and fovea_border_top_index < row < fovea_border_bottom_index):
                img[row][col] = True
            else:
                img[row][col] = False

    return img


def generate_layer_1(fovea_array: list, fovea_density: float, fovea_connections: int, periph_density: float, periph_connections: int):
    layer_1 = []

    for i in range(0, len(fovea_array)):
        for j in range(0, len(fovea_array[i])):
            current_neuron = {
                # id is coordinate
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
    print("layer_1 last neuron" + str(current_neuron))
    return layer_1

# periph factor should be 0.5 because you want a 0.25 as many neurons in the second layer (2D!)


def generate_deep_layer(fovea_array, periph_proportion, fovea_proportion):

    current_neuron = {}
    peripheral_neurons = []
    fovea_neurons = []
    neurons = []

    p_next_row = 0
    p_next_pixel = 0

    # generate periph neurons

    periph_factor = 1 / math.sqrt(periph_proportion)

    for row in decimal_range(0, len(fovea_array), periph_factor):
        for col in decimal_range(0, float(len(fovea_array[0])), periph_factor):
            if (not row % 1 == 0 or not col % 1 == 0):
                break
            row = int(row)
            col = int(col)
            if (fovea_array[row][col] == True):
                break
            current_neuron = {
                # id is coordinate
                "id":  "x" + str(col) + "y" + str(row) + "z" + str(1),
                "count": col + row,
                "activation_lvl": 0,
                "negative_y_coordinate": row,
                "positive_x_coordinate": col,
                "connections": {
                    "x0y0z0": 0.8,
                },
                "next_layer_absolute_density": 1,
                "connections_to_next_layer": 9,
            }
            peripheral_neurons.append(current_neuron)

    # generate fovea neurons

    fovea_factor = 1 / math.sqrt(fovea_proportion)

    for row in decimal_range(0, len(fovea_array), fovea_factor):

        for col in decimal_range(0, len(fovea_array[math.floor(row)]), fovea_factor):
            if (fovea_array[math.floor(row)][math.floor(col)] == False):
                continue
            current_neuron = {
                # id is coordinate
                "id": "x" + str(col) + "y" + str(row) + "z" + str(1),
                "count": col + row,
                "activation_lvl": 0,
                "negative_y_coordinate": row,
                "positive_x_coordinate": col,
                "connections": {
                    "x0y0z0": 0.8
                },
                "next_layer_absolute_density": 1,
                "connections_to_next_layer": 25,
            }
            fovea_neurons.append(current_neuron)

    print('fov neru ')
    print(len(fovea_neurons))

    return fovea_neurons + peripheral_neurons


def connect_2_layers(from_neurons_array, to_neurons_array, diffusion_factor):
    # first element of each nested array has to be the y coordinate
    to_neurons_2d = []
    y_coordinate_values = []

    # create sorted array that contains all y coordinate values
    for iter in range(0, len(to_neurons_array)):
        to_neuron = to_neurons_array[iter]
        if (to_neuron["negative_y_coordinate"] not in y_coordinate_values):
            y_coordinate_values.append(to_neuron["negative_y_coordinate"])
            y_coordinate_values.sort()
            # find value in sorted array
            # bisect.bisect_left()

    # create array with a row for each y_coordinate value
    for iter in range(0, len(y_coordinate_values)):
        to_neurons_2d.append([])

    # put to_neurons into 2d array
    for iter in range(0, len(to_neurons_array)):
        to_neuron = to_neurons_array[iter]
        y_coordinate_index = bisect.bisect_left(
            y_coordinate_values, to_neuron["negative_y_coordinate"])
        to_neurons_2d[y_coordinate_index].append(to_neuron)

    # sort neurons within rows of 2d array
    to_neurons_2d.sort(key=operator.itemgetter("positive_x_coordinate"))

    # finds center of neuron connections in to_neurons
    # TODO edit binary_search to accomodate object
    for from_neuron in from_neurons_array:
        row = binary_search(
            y_coordinate_values,
            from_neuron["negive_y_coordinate"])

        for neuron in to_neurons_2d[row]:
            binary_search(row, neuron[""])


load_dotenv()

mongLink = os.getenv('MONGO_URI')

print(mongLink)

cluster = MongoClient(mongLink)
db = cluster["abgi"]
collection = db["p1_neurons"]

layers_neurons_data = [[], [], [], []]


# collection.insert_one()
