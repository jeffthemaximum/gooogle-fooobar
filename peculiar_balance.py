'''
Peculiar balance
================

Can we save them? Beta Rabbit is trying to break into a lab that contains the only known zombie cure
 - but there's an obstacle. The door will only open if a challenge is solved correctly. The future of 
 the zombified rabbit population is at stake, so Beta reads the challenge: There is a scale with an 
 object on the left-hand side, whose mass is given in some number of units. Predictably, the task is 
 to balance the two sides. But there is a catch: You only have this peculiar weight set, having 
 masses 1, 3, 9, 27, ... units. That is, one for each power of 3. Being a brilliant mathematician, 
 Beta Rabbit quickly discovers that any number of units of mass can be balanced exactly using this set.

To help Beta get into the room, write a method called answer(x), which outputs a list of strings 
representing where the weights should be placed, in order for the two sides to be balanced, assuming 
that weight on the left has mass x units.

The first element of the output list should correspond to the 1-unit weight, the second element to 
the 3-unit weight, and so on. Each string is one of: 

"L" : put weight on left-hand side 
"R" : put weight on right-hand side 
"-" : do not use weight 

To ensure that the output is the smallest possible, the last element of the list must not be "-".

x will always be a positive integer, no larger than 1000000000.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int) x = 2
Output:
    (string list) ["L", "R"]

Inputs:
    (int) x = 8
Output:
    (string list) ["L", "-", "R"]
'''

def max_weight(peculiar_weights, left_weight):
    for i, weight in enumerate(peculiar_weights):
        foo = weight / 2
        if left_weight <= foo:
            return peculiar_weights[i-1]

def make_weights(num):
    weights = []
    x = 0
    while (3**x)/2 < num:
        weights.append(3**x)
        x += 1
    weights.append(3**x)
    return weights

def answer(x):
    answer = []
    weights = make_weights(x)
    num_cols = weights.index(max_weight(weights, x)) + 1

    for i in range(1, num_cols+1):
        offset = (3**(i-1)) / 2
        factor = (x - offset - 1) % 3**(i)
        index = (3**(i-1))
        if factor < index :
            answer.append('R')
        elif factor <  index *2:
            answer.append('L')
        else:
            answer.append('-')
    return answer

for i in range(1, 110000tags):
    print str(i) + ": " + str(answer(i))