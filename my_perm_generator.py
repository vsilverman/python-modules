"""
Created on Nov 19, 2019

This program generates all permutations
of a given length from a char string

@author: Vlad
"""

from itertools import permutations


def main():
    # Get all permutations of length 2
    # from an input string of chars
    input_str = "abcdefg"
    l_chars = list(input_str)
    print ("Input Chars List: " + str(l_chars) + "\n")
    # perm = permutations([1, 2, 3], 2)
    perm = permutations(l_chars, 2)

    # Print the obtained permutations
    for i in list(perm):
        print (i)


if __name__ == '__main__':
    # function below will be executed only
    # if we run this program as a script,
    # i.e. - "python my_files.py"
    main()
