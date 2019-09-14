# -*- coding: utf-8 -*-
#
# Reverse an array without affecting special characters
# Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.
#
# Examples:
#
# Input:   str = "a,b$c"
# Output:  str = "c,b$a"
# Note that $ and , are not moved anywhere.
# Only subsequence "abc" is reversed
#
# Input:   str = "Ab,c,de!$"
# Output:  str = "ed,c,bA!$"
#
# to use stdin change to: 
input_string = input("enter string").strip()
#input_string = "Ab,c,de!$Ab,c,de!$#$%^&*;lknaoijfgdnmaskuif*(&^%&()kjhkj)"

def main(in_string):
    chars = list(in_string)
    reverse_chars = []
    char_count = 0
    special_chars = []
    for char in chars:
        if char.isalpha():
            reverse_chars.insert(0, char)
        else:
            special_chars.append((char_count, char))
        char_count += 1
    for tup_item in special_chars:
        reverse_chars.insert(tup_item[0], tup_item[1])
    output_string = ''.join(reverse_chars)
    return f"{input_string}\n became \n{output_string}"




if __name__ == '__main__':
    output = main(input_string)
    print(output)

    