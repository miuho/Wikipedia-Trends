#!/usr/bin/env python

import sys
import os


# Read each line from large data set
for line in sys.stdin:
    # Split each line by space ' '
    info = line.split()
    
    # Each entry must have 4 elements
    if (len(info) != 4):
        continue
    
    # Exclude if entry is not English Wikipedia
    if ("en" != info[0]):
        continue

    # Exclude if entry's tile begins with following strings
    if (info[1].find("Media:") == 0 or 
        info[1].find("Special:") == 0 or
        info[1].find("Talk:") == 0 or
        info[1].find("User:") == 0 or
        info[1].find("User_talk:") == 0 or
        info[1].find("Project:") == 0 or
        info[1].find("Project_talk:") == 0 or
        info[1].find("File:") == 0 or
        info[1].find("File_talk:") == 0 or
        info[1].find("MediaWiki:") == 0 or
        info[1].find("MediaWiki_talk:") == 0 or
        info[1].find("Template:") == 0 or
        info[1].find("Template_talk:") == 0 or
        info[1].find("Help:") == 0 or
        info[1].find("Help_talk:") == 0 or
        info[1].find("Category:") == 0 or
        info[1].find("Category_talk:") == 0 or
        info[1].find("Portal:") == 0 or
        info[1].find("Wikipedia:") == 0 or
        info[1].find("Wikipedia_talk:") == 0):
        continue
        
    # Exclude if entry's title begins with lowercase letter
    if (info[1][0].islower()):
        continue

    # Exclude if entry's title ends with following extensions
    if (info[1].endswith(".jpg") or
        info[1].endswith(".gif") or
        info[1].endswith(".png") or
        info[1].endswith(".JPG") or
        info[1].endswith(".GIF") or
        info[1].endswith(".PNG") or
        info[1].endswith(".txt") or
        info[1].endswith(".ico")):
        continue

    # Exclude if entry's title matches following strings
    if (info[1] == "404_error/" or
        info[1] == "Main_Page" or
        info[1] == "Hypertext_Transfer_Protocol" or
        info[1] == "Search"):
        continue
    
    # Extract the date from filename
    filename = os.environ["mapreduce_map_input_file"]
    i = filename.rfind("201508")
    if (i == -1):
        continue
    date = filename[i+6:i+8]

    # Output the key value pair
    print "%s\t%s,%s" % (info[1], date, info[2])
