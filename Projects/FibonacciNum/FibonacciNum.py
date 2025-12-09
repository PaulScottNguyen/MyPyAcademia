# first two numbers
num1, num2 = 0, 1

print("Fibonacci sequence:")
# run loop 15 times
for i in range(15):
    # print next number of a series
    print(num1, end="  ")
    # add last two numbers to get next number
    res = num1 + num2

    # update values
    num1 = num2
    num2 = res