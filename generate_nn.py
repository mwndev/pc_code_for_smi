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


def retina_density(connections_array):
    input_height = len(connections_array)
    input_width = len(connections_array[0])


load_dotenv()

mongLink = os.getenv('MONGO_URI')

print(mongLink)

cluster = MongoClient(mongLink)
db = cluster["abgi"]
collection = db["p1_neurons"]

layers_neurons_data = [[], [], [], []]

for i in range(1, 640 * 480):
    layers_neurons_data[0].append(0.6)
for i in range(1, 100):
    print("fuck off")

# collection.insert_one()
