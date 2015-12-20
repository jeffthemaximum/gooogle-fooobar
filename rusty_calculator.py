''' 
using shunting-yard algorithm
pseudocode source: https://en.wikipedia.org/wiki/Shunting-yard_algorithm 
stack source: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementingaStackinPython.html


task: Lab minion Rusty works for Professor Boolean, a mad scientist. He's been stuck in this dead-end job crunching 
numbers all day since 1969. And it's not even the cool type of number-crunching - all he does is addition and 
multiplication. To make matters worse, under strict orders from Professor Boolean, the only kind of calculator minions 
re allowed to touch is the Unix dc utility, which uses reverse Polish notation.

Recall that reverse Polish calculators such as dc push numbers from the input onto a stack. When a binary operator 
(like "+" or "*") is encountered, they pop the top two numbers, and then push the result of applying the operator 
to them.

For example:
2 3 * => 6
4 9 + 2 * 3 + => 13 2 * 3 + => 26 3 + => 29

Each day, Professor Boolean sends the minions some strings representing equations, which take the form of single digits 
separated by "+" or "*", without parentheses. To make Rusty's work easier, write function called answer(str) that takes 
such a string and returns the lexicographically largest string representing the same equation but in reverse 
Polish notation.

All numbers in the output must appear in the same order as they did in the input. So, even though "32+" is 
lexicographically larger than "23+", the expected answer for "2+3" is "23+".

Note that all numbers are single-digit, so no spaces are required in the answer. 
Further, only the characters [0-9+*] are permitted in the input and output.

The number of digits in the input to answer will not exceed 100.
'''

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
    else:
        output_string += token
while operator_stack.isEmpty() is False:
    output_string += operator_stack.pop()

print output_string
