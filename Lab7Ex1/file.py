# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 16:15:12 2022

@author: SANDHYA
"""

import random

pts = [random.uniform(0, 100) for i in range(0,10000)]

# Open file in write mode
with open("file.txt", mode = 'w') as out_file:
    for pt in pts:
        # Write every item of the list to the file and then change line
        out_file.write(str(pt)+"\n")
        
# Read file 
l = []
with open("file.txt", mode = 'r') as file:
    for line in file:
        l.append(float(line))

        