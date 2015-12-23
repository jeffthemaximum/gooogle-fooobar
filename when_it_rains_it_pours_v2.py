'''
When it rains it pours
======================

It's raining, it's pouring. You and your agents are nearing the building where the captive 
rabbits are being held, but a sudden storm puts your escape plans at risk. The structural 
integrity of the rabbit hutches you've built to house the fugitive rabbits is at risk because 
they can buckle when wet. Before the rabbits can be rescued from Professor Boolean's lab, you 
must compute how much standing water has accumulated on the rabbit hutches. 

Specifically, suppose there is a line of hutches, stacked to various heights and water 
is poured from the top (and allowed to run off the sides). We'll assume all the hutches 
are square, have side length 1, and for the purposes of this problem we'll pretend that the 
hutch arrangement is two-dimensional.

For example, suppose the heights of the stacked hutches are [1,4,2,5,1,2,3] 
(the hutches are shown below):

...X...
.X.X...
.X.X..X
.XXX.XX
XXXXXXX
1425123

When water is poured over the top at all places and allowed to runoff, it will remain trapped at the 'O' locations:

...X...
.XOX...
.XOXOOX
.XXXOXX
XXXXXXX
1425123

The amount of water that has accumulated is the number of Os, which, in this instance, is 5.

Write a function called answer(heights) which, given the heights of the stacked hutches from 
left-to-right as a list, computes the total area of standing water accumulated when water is 
poured from the top and allowed to run off the sides. 

The heights array will have at least 1 element and at most 9000 elements. Each element will 
have a value of at least 1, and at most 100000.
'''

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