import pudb

def make_squares(x):
    i = 0
    squares = []
    while i**2 < x:
        squares.append(i**2)
        i += 1
    if i ** 2 == x:
        return False
    else:
        return squares[::-1]

def answer(x):
    squares = make_squares(x)
    # subtract largest square from x
    # or catch case of perfect square
    try:
        biggest = squares[0]
    except:
        return 1
        
    count = 0
    total = x - biggest
    count += 1
    while total != 0:
        flag = False
        i = 0
        while i < len(squares) and flag == False:
            num = squares[i]
            if squares[i] <= total:
                biggest = squares[i]
                squares = squares[i:]
                total = total - biggest
                count += 1
                flag = True
            i += 1
    return count


print answer(36)