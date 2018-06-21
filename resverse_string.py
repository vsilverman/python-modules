'''
Created on Apr 9, 2018

@author: Vlad
'''

def rev_string(s):
    out = "Reversed string: "
    out += s[::-1]
    print(out)

if __name__ == '__main__':
    print("This program takes user input as a string")
    print("and prints out the reversed string")
    print("_________________________________________")
    for i in range (3):
        s1=raw_input("\nEnter a string: ")
        rev_string(s1)
    print("\n--- end of program ---")