import pudb
import timeit
# def egcd(a, b):
#     if a == 0:
#         return (b, 0, 1)
#     else:
#         g, y, x = egcd(b % a, a)
#         return (g, x - (b // a) * y, y)

# def modinv(a, m):
#     g, x, y = egcd(a, m)
#     if g != 1:
#         raise Exception('modular inverse does not exist')
#     else:
#         return x % m

# from http://stackoverflow.com/questions/14279866/what-is-inverse-function-to-xor
# c = a^b
# a = c^b; // or b^c (order is not important)
# b = c^a; // or a^c

# 129*message[0] = 129
# 129 XOR message[-1] = 129
# 129 % 256 = 129
# Thus digest[0] = 129.

# For digest[1]:
# 129*message[1] = 16641
# 16641 XOR message[0] = 16640
# 16640 % 256 = 0
# Thus digest[1] = 0.
# For example, if message[0] = 1 and message[1] = 129, then:
# For digest[0]:

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def answer(x):
    message = []
    for i in range(0, len(x)):
        j = 0 
        twenty_five = x[i]
        message_at_i = 0 if i == 0 else message[i - 1]
        # i hoped to find a way to find a pattern in the j
        # values which end the while loop here, so I wouldn't
        # have to just iterate through, but I couldn't do it.
        check = ((twenty_five ^ message_at_i) + (j * 256))
        while check % 129 != 0:
            j += 1
            check = ((twenty_five ^ message_at_i) + (j * 256))
        twenty_one = check / 129
        message.append(twenty_one)

    return message

digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]

wrapped = wrapper(answer, digest)
print timeit.timeit(wrapped, number=1000)

print answer(digest)
