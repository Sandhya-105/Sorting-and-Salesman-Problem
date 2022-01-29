# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 13:45:26 2022

@author: SANDHYA
"""

import math
import csv
from City import City
from Point import Point
from itertools import permutations
import matplotlib.pyplot as plt
cities = []
xArray = []
yArray = []

def harvesine_distance(point1, point2):
    
    lng1 = math.radians(point1.getX())
    lat1 = math.radians(point1.getY())
    lng2 = math.radians(point2.getX())
    lat2 = math.radians(point2.getY())
    
    dlat = (lat2 - lat1)/2
    dlng = (lng2 - lng1)/2
    
    sinlat = math.pow(math.sin(dlat), 2)
    sinlng = math.pow(math.sin(dlng), 2)
    
    d = math.sqrt(sinlat + (math.cos(lat1) * math.cos(lat2) * sinlng))
    dist = 2 * 6371 * math.asin(d)
    return(dist) # in kms

# open the CSV file
with open("cities.csv", mode = 'r') as file:
    # read the CSV file
    csvFile = csv.reader(file)
    next(csvFile, None)

    # display the contents of the CSV file
    for line in csvFile:
        
        name, coords, area, population, pop_density, gdp, income = line
        #print(name, coords, area, population, pop_density, gdp, income)
        lat_lng = coords.split()
        location = Point(lat_lng[1], lat_lng[0])
        city = City(name, location, area, population, pop_density, gdp, income)
        city.getLocation().setfillColor("red")
        cities.append(city)
        
perm = list(permutations(cities))
distance = []
x = []

for city in perm:
    if( city[0].getName() == "Milan"):
     x.append(city)
    
for i in x:
    dist = 0
    for j in range(0, len(i)-1):
     d = harvesine_distance(i[j].getLocation(), i[j+1].getLocation())
     dist = d + dist
    distance.append(dist)

mind = min(distance)
mindindex = distance.index(mind)
pcities = x[mindindex]

for city in pcities:
    plt.scatter(city.getLocation().getX(), city.getLocation().getY(), c = city.getLocation().getfillColor())
    plt.text(city.getLocation().getX(), city.getLocation().getY(), city.getName(), c = "Black", size = 10)
    xArray.append(city.getLocation().getX())
    yArray.append(city.getLocation().getY())
plt.plot(xArray, yArray, c = "black")    

