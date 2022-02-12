# Lab7 ---ISP

## Observations

1. TypeCasting is a must when reading the text file containing random float numbers which was represented as strings.
2. Using with open(), the file can be opened and automatically gets closed when it runs fully. It's a good example for resource management.


The mergesort.py algorithm works faster than the insertionsort.py algorithm.

Mergesort algorithm works on divide and conquer strategy i.e, it splits the array/list and then assembles the value which is the least in comparison. Works better on large dataset in this case ours.
Insertion sort on the another hand works on inplace sorting i.e, it takes each element and compare it with the preceding element. It takes a lot of computation power.

### Time comparison
Mergesort: Insertionsort = 1:4 ( on multiple accounts)

### Object Oriented Programming Concepts

Inheritance and access modifiers: data abstraction has been used here.

Inheritance: For code reusability, here, the City, Shape and Point classes have their own methods which was needed by another program(travelling salesmen problem). We have cities file which has 10 city details. In order to extract the location from this file, we need to convert the cities file into individual city class( which in turn has point class).

Access Modifiers: The classes(city, shape, point) to be inherited must not be corrupted and hence for data security, data abstraction was used. These class members are made private. For accessing the members: getters and setters are used.





 
