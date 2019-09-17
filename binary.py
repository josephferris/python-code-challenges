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
from copy import copy
import operator


def main(my_num):
    bit_list = []
    if my_num != 0:
        while my_num >= 1:
            if (my_num % 2) == 0:
                bit_list.insert(0, '0')
                my_num = my_num // 2
            else:
                bit_list.insert(0, '1')
                my_num = (my_num - 1) // 2
    else:
        bit_list = ['0']
    bit_string = ''.join(bit_list)
    print(f"bit_string = {bit_string}")


if __name__ == "__main__":
    input_int = int(input())
    main(input_int)

'''
I tried using the '&' operator and it did not work the way it was supposed to:
Since it did not work, I used % 2
'''