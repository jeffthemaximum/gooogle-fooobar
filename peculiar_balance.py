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

print answer(2)

# for i in range(1, 15):
#     print str(i) + ": " + str(answer(i))