import operator
import bisect


def binary_search(data, val):
    highIndex = len(data)-1
    lowIndex = 0
    while highIndex > lowIndex:
        index = (highIndex + lowIndex) / 2
        sub = data[index]
        if data[lowIndex] == val:
            return lowIndex
        elif sub == val:
            return index
        elif data[highIndex] == val:
            return highIndex
        elif sub > val:
            if highIndex == index:
                return highIndex
            highIndex = index
        else:
            if lowIndex == index:
                return highIndex
            lowIndex = index
    return highIndex


# takes in points which are [ ... , [x, y, neuron_id], ...]
def get_list_of_unique_coordinate_values_from_points(points: list, index_of_coordinate: int):
    # if index is 0 it's the x coordinates, if 1 it's y
    unique_coordinates = []
    for point in points:
        coordinate = point[index_of_coordinate]
        if (coordinate not in unique_coordinates):
            unique_coordinates.append(coordinate)
    return sorted(unique_coordinates)

# TODO


def convert_neuron_to_xy_array(neurons_array):
    return_value = []
    for neuron in neurons_array:
        return_value.append(
            [
                neuron["positive_x_coordinate"],
                neuron["negative_y_coordinate"],
                neuron["id"]
            ]
        )
    return return_value


# takes in points which are [ ... , [x, y, neuron_id], ...]
def match_closest_to_from_points(to_points: list, from_points: list, wiggleroom_as_radius: int):

    unique_x_to_vals = get_list_of_unique_coordinate_values_from_points(
        to_points, 0)
    unique_y_to_vals = get_list_of_unique_coordinate_values_from_points(
        to_points, 1)
    unique_x_from_vals = get_list_of_unique_coordinate_values_from_points(
        from_points, 0)
    unique_y_from_vals = get_list_of_unique_coordinate_values_from_points(
        from_points, 1)

    to_by_x = (sorted(to_points, key=lambda x: x[0]))
    to_by_y = (sorted(to_points, key=lambda x: x[1]))

    from_by_x = (sorted(from_points, key=lambda x: x[0]))
    from_by_y = (sorted(from_points, key=lambda x: x[1]))

    for from_point in to_by_x:
        closest_x = bisect.bisect_left(
            from_by_x, from_point, key=lambda x: x[0])
        closest_y = bisect.bisect_left(
            from_by_y, from_point, key=lambda x: x[1]
        )

    # now that we have the closest x and y coordinates we can check add the surrounding rows and cols
    x_candidates = []
    y_candidates = []

    # get index of center coordinates in x and y arrays
    center_index_x = bisect.bisect_left(
        closest_x
    )
    center_index_y = bisect.bisect_left(
        closest_y
    )

    for iter in range(-wiggleroom_as_radius, wiggleroom_as_radius):

        # to ensure that you don't check an out of bounds array
        if 0 <= iter <= len(unique_x_from_vals):
            # TODO how to sort out useless rows by checking if closest point is within some expected area
            # check closest_y of da row mann so that u dont add a stupidd lajn mann!
            x_candidates.append(unique_x_from_vals[center_index_x + iter])

        if 0 <= iter <= len(unique_y_from_vals):
            y_candidates.append(unique_y_from_vals[center_index_y + iter])

    x_candidates.sort()
    y_candidates.sort()

    # these are the rows and cols that will be checked
    print("x and y cantidate arrays:")
    print(x_candidates)
    print(y_candidates)

    min_x = x_candidates[0]
    max_x = x_candidates[-1]
    min_y = y_candidates[0]
    max_y = y_candidates[-1]
