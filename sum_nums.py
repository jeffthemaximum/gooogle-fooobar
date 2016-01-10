import pudb

def sum_nums(x):
    nums = [int(i) for i in str(x)]
    while len(nums) > 1:
        nums = sum(nums)
        nums = [int(i) for i in str(nums)]
    return nums[0]

def tricky_sum_nums(x):
    if x == 0:
        return 0
    elif x % 9 == 0:
        return 9
    else:
        return x % 9

for i in range(1, 100):
    print str(i) + ": " + str(sum_nums(i))

print sum_nums(12345)
print tricky_sum_nums(12345)
