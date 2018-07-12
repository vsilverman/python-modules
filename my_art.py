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
import platform
import sys
import subprocess

def my_python_art(cfgfn):
    print ("PropFile: " + cfgfn)
#   default properties are dependent on the platform
    my_default_folder, my_default_script = get_default_properties()
    my_props=my_files.read_properties(cfgfn)
#    my_folder=my_props["part.folder"]
    my_folder=my_props.get("part.folder", my_default_folder)
    my_script=my_props.get("part.script", my_default_script)
    process(my_folder, my_script)
    

def get_default_properties():
    '''
        This function determins default
        property values depending on the
        type of the platform this ART
        framework is running on (e.g.
        Windows vs Linux/Mac platforms)
        '''
    os_name = platform.system()
    if os_name.startswith("Linux") or os_name.startswith("Darwin"):
        return "/path/to/my_folder", "call-from-python.sh"
    else:
        return "d:/", "call-from-python.cmd"

    
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
            print("[F] : " + file)
            if file.endswith(script_name):
                # add absolute path to the filename
                filepath = os.path.join(dirpath, file)
                #                 paraemeters to be passed to subprocess
                #                 may be defined in the 2nd parameter, e.g.
                #                subprocess.call(["mycurl.cmd", "-help"])
                subprocess.call([filepath, ""])


def main():
    if __name__ == '__main__':
        PropFile = "./" + "part.cfg"
        if len(sys.argv) < 2:
            print ("Usage: python my_art.py PropFile")
            print ("Running demo version with default params")
        else:
            PropFile = sys.argv[1]
        my_python_art(PropFile)

	
main()
		
