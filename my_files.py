'''
Created on Feb 25, 2018


@author: Vlad
'''
import os
import random
from pkg_resources._vendor.appdirs import _get_win_folder_with_pywin32
#from test.test_whichdb import _fname


def jokeOfTheDay():

    '''
    This function prints a single
    random joke from a list of jokes, 
    contained in the "jokes.txt" file
    
    To run this function from other module
    include in that module following lines:
        from my_files import jokeOfTheDay
        jokeOfTheDay()
    '''

    filename = "jokes.txt"
    
    # check if file exists
    if (not os.path.exists(filename)):
        print("file " + filename + " does not exist")
        quit()
    
    # read file into list of lines
    text_file = open(filename, "r")
    lines = text_file.readlines()
    
    # find the number of lines in file
    nmblines=len(lines)
    
    # generate random int number in defined range
    rand=random.randint(0, nmblines-1)
    
    #print random number and close file
    print(lines[rand])
    text_file.close()
    

def print_file(filename):
    '''
    This function prints file
    '''
    text_file = open(filename,'r')
    line = text_file.readline()
    while(line != ""):
        print(line)
        line = text_file.readline()
    text_file.close()
    

def print_reversed_file(fname):
    '''
    This function prints file
    in reverse order 
    '''
    for line in reversed(list(open(fname))):
        print(line.rstrip())
        

def write_reversed_line_in_file(infname, outfname):
    '''
    This function reverses
    every line in file
    '''
    out_file = open(outfname, "w")
    for line in list(open(infname)):
        print ("line: " + line.rstrip())
        rline = line.rstrip()[::-1] #reverse a line
        print ("rline: " + rline)
        out_file.write(rline + "\n")

def digits_in_file(fname):
    '''
    This function counts
    number of digits in file
    '''
    n = 0
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()
            for w in words:
                for character in w:
                    if(character.isdigit()):
                        n=n+1
    print("Number of digits = " + str(n))
    
    
def read_properties(fname):
    '''
    This function prints and returns contents
    of the specified properties file
    '''
    props = {}
    with open(fname) as fp:
        for line in fp:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            key, value = parse_property(line)
            props[key] = value
    print (props)
    return props
    

def parse_property(prop):
    key, value = prop.split('=')
    key = key.strip()  # handles key = value as well as key=value
    value = value.strip()
    return key, value # return 2 values
    

def dir_list(folder, ext):
    '''
    This function prints
    list of files with 
    given extension in
    specified folder
    '''
    for file in os.listdir(folder):
        if file.endswith(ext) or ext=="*":
            print(os.path.join(folder, file))
    

def dir_recur_list(folder):
    '''
    This function prints
    recursive content of folder
    and for every *.txt file 
    counts number of digits in it.
    '''
    for dirpath, dirs, files in os.walk(folder):
        print("[D] : " + dirpath)
        for file in files:
#            print("[F] : " + os.path.join(dirpath, file))
            print("[F] : " + file)
            if file.endswith(".txt"):
                filepath = os.path.join(dirpath, file)
#                print_file(filepath)
                digits_in_file(filepath)


def python_art(cfgfn):
    my_props=read_properties(cfgfn)
    my_folder=my_props["part.folder"]
    dir_recur_list(my_folder)
    
    
def main():
    if __name__ == '__main__':
        jokeOfTheDay()
        config_file="part.cfg"
        file_name="content.txt"
        rfile_name="rev-content.txt"
        print_file(file_name)
        print ('\n')
        print_reversed_file(file_name)
        print ('\n')
        write_reversed_line_in_file(file_name, rfile_name)
        print ('\n')
        read_properties(config_file)
        print ('\n')
        digits_in_file(file_name)
        print ('\n')
        dir_list("d:/Flash1", ".txt")
        print ('\n')
        dir_list(read_properties(config_file)["part.folder"], "*")
        print ('\n')
        #dir_recur_list("d:\Flash1")
        #print ('\n')
        python_art(config_file)


main()
