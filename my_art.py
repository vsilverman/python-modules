'''
Created on May 8, 2018

    This program takes as parameter
    the name of config file, which
    defines location of the root folder.
    Starting from the root folder
    this program searches for the
    specified script and executes it
    if found.

@author: Vlad
'''
import my_files
import os
import sys
import subprocess

my_folder = "d:/workspace-eclipse-4.6/python-modules/src/root/nested/"
my_script = "call-from-python.cmd"

def my_python_art(cfgfn):
    print ("PropFile: " + cfgfn)
    my_props=my_files.read_properties(cfgfn)
    my_folder=my_props["part.folder"]
    my_script=my_props["part.script"]
    process(my_folder, my_script)
    
    
def process(folder_name, script_name):
    '''
    This function prints
    recursive content of folder_name,
    including child folders and files,
    and executes script_name in every
    folder where it finds it.
    '''
    for dirpath, dirs, files in os.walk(folder_name):
        print("[D] : " + dirpath)
        for file in files:
#            print("[F] : " + os.path.join(dirpath, file))
            print("[F] : " + file)
            if file.endswith(script_name):
                filepath = os.path.join(dirpath, file)
#				 paraemeters to be passed to subprocess
#				 may be defined in the 2nd parameter, e.g.
#                subprocess.call(["mycurl.cmd", "-help"])
                subprocess.call([script_name, ""])
    

def main():
    if __name__ == '__main__':
        PropFile = my_folder + "p-art.cfg"
        if len(sys.argv)<2:
            print ("Usage: python my_art.py PropFile")
            print ("Running demo version with default params")
        else:
            PropFile = sys.argv[1]
        my_python_art(PropFile)
	
main()
		