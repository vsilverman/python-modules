'''
Created on Apr 9, 2018

@author: Vlad

 * This class can process a sequence of strings (sentence) 
 * and print out a list of all anagrams in this sentence
 * and corresponding number of its occurrences
 * 
 * For example given a sentence of "132 321 dad dog add god 231"
 * it will print out:
 *     123 3
 *     dad 2
 *     dog 2
'''

def find_anagrams(s):
    d=dict()
    words = s.split()
    for w in words:
        sw = sort_word_by_chars(w)
#        sw = ''.join(sorted(w))
        if (d.has_key(sw)):
            val = d[sw] + 1
        else:
            val = 1
        d[sw] = val
    for sw in d.keys():
        if (d[sw] > 1):
            print(sw + " " + str(d[sw]))
            
def sort_word_by_chars(word):
    return ''.join(sorted(word))

if __name__ == '__main__':
    print("This program takes user input as a string and")
    print("prints out a list of all anagrams in this sentence")
    print("_________________________________________")
    sentence = "132 321 dad dog add god 231"
    for i in range (3):
        s1=raw_input("\nEnter a string with some anagrams: ")
        if (s1==""):
            s1=sentence    
        find_anagrams(s1)
    print("\n--- end of program ---")