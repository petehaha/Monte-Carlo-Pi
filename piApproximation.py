from random import random
from math import sqrt

sampleSize = int(input("Input the sample size\n\n"))
pointsInCircle = 0

for counter in range(sampleSize):

    a = random() # x coordinate of point
    b = random() # y coordinate of point
    
    if (sqrt(pow(a,2) + pow(b,2)) < 1.0):
        pointsInCircle += 1

# area as percentage assumes radius = 0.5 e.g. imagine a box with side length 1
area = pointsInCircle/sampleSize 

# A / radius ^ 2 = pi
print("Approximation for pi is... ", area / pow(0.5 , 2)) 
