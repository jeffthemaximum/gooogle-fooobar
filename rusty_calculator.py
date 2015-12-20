''' using shunting-yard algorithm '''
''' pseudocode source: https://en.wikipedia.org/wiki/Shunting-yard_algorithm '''
''' stack source: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html '''

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


#instantiate output queue
output_string = ''

#instantiate operator stack
operator_stack = Stack()

string = "2*4*3+9*3+5"
# while there are tokens to be read
for i in string:
    # read the token
    token = i
    if token == '+':
        while operator_stack.isEmpty() is False and operator_stack.peek() == '*':
            output_string += (operator_stack.pop())
        operator_stack.push(token)
    elif token == '*':
        operator_stack.push(token)
    # if the token is a string between 0-9
    else:
        # add it to the output queue
        output_string += token
# when there are no more tokens to be read
# while there are still operator tokens in the stack
while operator_stack.isEmpty() is False:
    # pop the operator onto the output queue
    output_string += operator_stack.pop()

print output_string





