import pudb

def make_col(col_num):
    col = []
    multiplier = weights[col_num-1]
    for i in range(multiplier):
        col.append('R')
    for i in range(multiplier):
        col.append('L')
    for i in range(multiplier):
        col.append('-')
    return col

def max_weight(peculiar_weights, left_weight):
    for i, weight in enumerate(peculiar_weights):
        foo = weight / 2
        if left_weight <= foo:
            return peculiar_weights[i-1]

def answer(x):
    answer = ''
    num_cols = weights.index(max_weight(weights, x)) + 1
    for i in range(1, num_cols+1):
        if i == 1:
            answer += cols[1]['col'][(x-1) % 3]
        else:
            offset = cols[i]['offset']
            answer += cols[i]['col'][(x - offset) % 3**(i) - 1]
    print str(x) + ": " + str(answer)

weights = []
cols = {}
x = 0

# make weights list
while 3**x < 100000000:
    weights.append(3**x)
    x += 1

# make cols
for i in range(1,9):
    cols[i] = {
        'col': make_col(i),
        'offset': (3**(i-1)) / 2
    }

for i in range(1, 15):
    answer(i)