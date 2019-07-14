#!/usr/bin/python

import taglib
from shutil import copyfile
import glob
import os
import sys

def get_tags(path):
    try:
        song = taglib.File(path)
        
        try:
            artist = song.tags["ARTIST"][0]
        except:
            artist = "Unknown"
        try:
            album = song.tags["ALBUM"][0]
        except:
            album = "Unknown"

        return artist, album

    except:
        return "",""

def sort_file(path, target, artist, album):
    target_dir = target + "/" + artist + "/" + album
   
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)
    
    try:
        copyfile(path, target_dir + "/" + path.split("/")[-1])
    except:
        print("Error while copying : " + path)

def main(argv):
    try:
        my_path = argv[0]
        target = argv[1]
    except:
        print("Bad arguments")
        exit(-1)
    print("src: " + my_path)
    print("dst: " + target)
    files = glob.glob(my_path + '/**/*', recursive=True)

    for elems in files:
        artist, album = get_tags(elems)

        if artist != "" and album != "":
            sort_file(elems, target, artist, album)

if __name__ == "__main__":
   main(sys.argv[1:])

