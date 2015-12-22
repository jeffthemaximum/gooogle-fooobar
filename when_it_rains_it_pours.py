import pudb


def answer(x):

    # make copy of x here and enumerate with list indices
    enumerated_x = [pair for pair in enumerate(x)]

    # get max and index and end_index
    maximum_tuple = max(enumerated_x, key=lambda x: x[1])
    maximum = maximum_tuple[1]
    maximum_index = maximum_tuple[0]
    end_index = len(x) - 1


    i = maximum_index + 1
    water_total = 0

    # bloated code to find water to the right of the highest rabbit hutch
    while((i - 1) != end_index):
        # find max in right half and index
        right_half = enumerated_x[(maximum_index+1):(end_index+1)]
        if len(right_half) > 0:
            right_half_maximum_tuple = max(right_half, key=lambda x: x[1])
            right_half_maximum = right_half_maximum_tuple[1]
            right_half_maximum_index = right_half_maximum_tuple[0]
        else:
            break

        # check to make sure right half maximum isn't maximum_index + 1
        while (right_half_maximum_index == maximum_index + 1 and right_half_maximum_index != end_index):
            # find max in right half and index
            right_half = enumerated_x[(maximum_index+1):(end+1)]
            right_half_maximum_tuple = max(right_half, key=lambda x: x[1])
            right_half_maximum = right_half_maximum_tuple[1]
            right_half_maximum_index = right_half_maximum[0]

        # iterate across items between maximum and right half maximum
        # find different between items and lowest of maximum and right_half_maximum
        lowest_of_two_maximums = min(maximum, right_half_maximum)
        while i < right_half_maximum_index: # and right_half_maximum_index != end_index
            difference = lowest_of_two_maximums - x[i]
            water_total += difference
            i += 1

        # realign iterator with beginning of new sublist
        i += 1

        #reset maximum for new loop through while loop
        maximum = right_half_maximum
        maximum_index = right_half_maximum_index

    # bloated codez to find maximum to left side of highest rabbit hutch
    maximum_tuple = max(enumerated_x, key=lambda x: x[1])
    maximum = maximum_tuple[1]
    maximum_index = maximum_tuple[0]
    i = maximum_index - 1
    while((i + 1) != 0):
        # find max in right half and index
        left_half = enumerated_x[(0):(maximum_index)]
        if len(left_half) > 0:
            left_half_maximum_tuple = max(left_half, key=lambda x: x[1])
            left_half_maximum = left_half_maximum_tuple[1]
            left_half_maximum_index = left_half_maximum_tuple[0]
        else:
            break

        # check to make sure right half maximum isn't maximum_index + 1
        while (left_half_maximum_index == maximum_index - 1 and left_half_maximum_index != 0):
            # find max in right half and index
            left_half = enumerated_x[(1):(maximum_index-1)]
            left_half_maximum_tuple = max(left_half, key=lambda x: x[1])
            left_half_maximum = left_half_maximum_tuple[1]
            left_half_maximum_index = left_half_maximum_tuple[0]

        # iterate across items between maximum and right half maximum
        # find different between items and lowest of maximum and right_half_maximum
        lowest_of_two_maximums = min(maximum, left_half_maximum)
        while i > left_half_maximum_index: # and left_half_maximum_index != 0:
            difference = lowest_of_two_maximums - x[i]
            water_total += difference
            i -= 1

        # realign iterator with beginning of new sublist
        i -= 1

        #reset maximum for new loop through while loop
        maximum = left_half_maximum
        maximum_index = left_half_maximum_index

    return water_total

print(answer([4, 2, 5, 1, 2, 3, 1, 2]))