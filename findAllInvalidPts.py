#Finds all invalid points up to desired limit and plots them

import numpy
from matplotlib import pyplot as plt
import math

#Lists to contain all non-solutions



#The program iterates over all c1,c2 up to a desired limit.
#For each such pair, it checks all a,b,k1,k2 to see if there is a
#solution to the most general equation. If there is, the loop
#breaks (we only need one solution), and if not, the point
#is added to the list of non-solutions.

def findInvalidPts(maxc1):
    c1list = []
    c2list = [] 
    validc1 = []
    validc2 = []
    for c1 in numpy.arange(2, maxc1, 0.5):
        maxxb = int(c1)
        print(c1)
        solutionFound = False
        for c2 in numpy.arange(int(c1*c1*0.25),int((c1*c1)/3)+1,0.5):      #int(c1*c1*0.25)
                solutionFound = False

                if math.trunc(c1) == c1 and math.trunc(c2) == c2:
                    for b in numpy.arange(0, maxxb):
                        if solutionFound:
                            break
                        for k1 in numpy.arange(0,b+1):
                            if solutionFound:
                                break
                            for k2 in numpy.arange(0,b+1):
                                f = 2*c1*b - 2*b*b + (k1+k2)*b - (k1*k1+k2*k2) -2*c2
                                a = c1 - b + (k1+k2)*0.5
                                if f == 0 and a >= k1 and a >= k2 and a == int(a):
                                    solutionFound = True
                                    validc1.append(c1)
                                    validc2.append(c2)
                                    break
                                elif b == maxxb-1 and k1 == b and k2 == b:
                                    c1list.append(c1)
                                    c2list.append(c2)
                elif math.trunc(c1) != c1 and math.trunc(c2) != c2:
                    for b in numpy.arange(0, maxxb):
                        if solutionFound:
                            break
                        for k1 in numpy.arange(0,b+1):
                            if solutionFound:
                                break
                            for k2 in numpy.arange(0,b+1):
                                f = 2*c1*b - 2*b*b + (k1+k2)*b - (k1*k1+k2*k2) -2*c2
                                a = c1 - b + (k1+k2)*0.5
                                if f == 0 and a >= k1 and a >= k2 and a == math.trunc(a):
                                    solutionFound = True
                                    validc1.append(c1)
                                    validc2.append(c2)
                                    break
                                elif b == maxxb-1 and k1 == b and k2 == b:
                                    c1list.append(c1)
                                    c2list.append(c2)
                                    
    plt.plot(c1list,c2list,'.r')
    plt.plot(validc1,validc2,'.b')
    plt.show()
    
findInvalidPts(30)