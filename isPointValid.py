#A program to determine whether a point is a valid
#set of coefficients for an alcoved polygon
#enter coords, and if there is an alcoved polygon
#corresponding to that point, the program will 
#show the values of a, b, k1, k2 that constitute the polygon. 

import numpy
import math

c1 = float(input("c1 = "))
c2 = float(input("c2 = "))

for b in numpy.arange(0,c1+1,1):     #int(math.sqrt(c2))
    for k1 in numpy.arange(0,b+1,1):
        for k2 in numpy.arange(0,b+1,1):
            f = 2*c1*b-2*b*b + (k1+k2)*b -(k1*k1+k2*k2)-2*c2
            a = c1-b+(k1+k2)*0.5
            if f == 0 and a >= k1 and a >= k2 and a == math.trunc(a):
                print("a = ",a,"b = ",b, "k1 = ", k1, "k2 = ", k2)
