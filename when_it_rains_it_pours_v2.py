def answer(x):
    # setup list to store tuples of heights from pos and neg iteration
    heights = []

    # get length cuz i'll prolly use it a bunch
    length = len(x)

    # 'maxim' as variable name for height cuz my last name is cool
    maxim = 0

    # iterate left to right
    for i in range(length):

        #initialize difference
        difference = 0

        # check if height > maxim
        if x[i] > maxim:

            #make new maxim
            maxim = x[i]

        #else your in a trough
        else:

            #find dif between maxim and height
            difference = maxim - x[i]

        #append difference to heights in tuple form
        heights.append([difference])

    # keep seperate iterator for reverse iteration for simplicity's sake
    k = 0

    #reset maxim to zero
    maxim = 0

    # iterate right to left
    # syntax is range(start, end, step) for all you n00bs
    for j in range(length-1, -1, -1):

        #initialize difference
        difference = 0

        # check if height > maxim
        if x[j] > maxim:

            #make new maxim
            maxim = x[j]

        #else your in a trough
        else:

            #find dif between maxim and height
            difference = maxim - x[j]

        #append difference to heights in tuple form
        heights[j].append(difference)

    # get minimum height at each bunny hutch
    heights = map(lambda x: min(x), heights)

    # add heights and return
    return sum(heights)





print(answer( [1, 2, 3, 2, 1]))