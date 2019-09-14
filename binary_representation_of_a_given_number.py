# Method 1: Iterative
# For any number, we can check whether its ‘i’th bit is 0(OFF) or 1(ON) by bitwise
#  ANDing it with “2^i” (2 raise to i).
#
# 1) Let us take number 'NUM' and we want to check whether it's 0th bit is ON or OFF
#     bit = 2 ^ 0 (0th bit)
#     if  NUM & bit == 1 means 0th bit is ON else 0th bit is OFF
#
# 2) Similarly if we want to check whether 5th bit is ON or OFF
#     bit = 2 ^ 5 (5th bit)
#     if NUM & bit == 1 means its 5th bit is ON else 5th bit is OFF.
#
#
# Method 2: Recursive
# Following is recursive method to print binary representation of ‘NUM’.
#
# step 1) if NUM > 1
#     a) push NUM on stack
#     b) recursively call function with 'NUM / 2'
# step 2)
#     a) pop NUM from stack, divide it by 2 and print it's remainder.
#
#
# Method 3: Recursive using bitwise operator
# Steps to convert decimal number to its binary representation are given below:

# step 1: Check n > 0
# step 2: Right shift the number by 1 bit and recursive function call
# step 3: Print the bits of number
#

input_int = int(input())

stack = []


def main(mynum):
    stackem(mynum)
    #print('\n' + str(bin(mynum)))


def stackem(mynum):
    if mynum >= 1:
        stack.append(mynum)
        stackem(mynum / 2)
    if len(stack) > 0:
        result = int(stack.pop() % 2)
        print(result, end='')


if __name__ == "__main__":
    main(input_int)
