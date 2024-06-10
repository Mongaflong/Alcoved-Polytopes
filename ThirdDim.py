#For the third dimension wowwowoow

from random import randint as ran
import matplotlib.pyplot as plt
from scipy import spatial as spa
import numpy
import math
import time



a = 0
b = 10


def genIntPts(a,b):
    a1 = a
    b1 = ran(1,b)
    
    a2 = a
    b2 = ran(1,b)
    
    a3 = a
    b3 = ran(1,b)

    
    if b1 == b2:
        a12 = ran(-b1,0)
        b12 = ran(1,b2)
        
    
    elif b1 < b2:
        a12 = ran(-b1,0)
        b12 = ran(b2-b1,b2)
    else:
        a12 = ran(-b1,b2-b1)
        b12 = ran(0,b2)
        
        
    
    if b1 == b3:
        a13 = ran(-b1,0)
        b13 = ran(1,b3)
    
    elif b1 < b3:
        a13 = ran(-b1,0)
        b13 = ran(b3-b1,b3)
    else:
        a13 = ran(-b1,b3-b1)
        b13 = ran(0,b3)
        
    
    if b2 == b3:
        a23 = ran(-b2,0)
        b23 = ran(1,b3)
     
    elif b2 < b3:
        a23 = ran(-b2,0)
        b23 = ran(b3-b2,b3)
    else:
        a23 = ran(-b2,b3-b2)
        b23 = ran(0,b3)

    """
    k = 1
    a1 = 0
    a2 = 0    
    a3 = 0
    b1 = 2*k
    b2 = 2*k
    b3 = 2*k

    a12 = -1*k
    b12 = 1*k
    a13 = -1*k
    b13 = 1*k
    a23 = -1*k
    b23 = 1*k
    """
        
    return a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23        # a2-b1,b2-a1,a3-b1,b3-a1,a3-b2,b3-a2
    
#If the polytope is a cube or block we have simple case of vol and bdry points.
def ifCube(a1,b1,a2,b2,a3,b3):
    a = (b1-a1)
    b = (b2-a2)
    c = (b3-a3)
    V = a*b*c
    T = (a+1)*(b+1)*(c+1)
    I = (a-1)*(b-1)*(c-1)
    B = T-I
    
    return V,B
    
    
def findAllPts(a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23):
    allPtsList = []
    for x in range(a1,b1+1):
        for y in range(a2,b2+1):
            for z in range(a3,b3+1):
                xyz = (x,y,z)
                if a12 <= y-x and y-x <= b12 and a13 <= z-x and z-x <= b13 and a23 <= z-y and z-y <= b23:
                    allPtsList.append(xyz)
    return allPtsList
    
def intBdryPts(allPtsList):
    intPts = []
    bdryPts = []
    for pt in allPtsList:
        x = pt[0]
        y = pt[1]
        z = pt[2]
        if a12 < y-x and y-x < b12 and a13 < z-x and z-x < b13 and a23 < z-y and z-y < b23 and a1 < x and x < b1 and a2 < y and y < b2 and a3 < z and z < b3:
            intPts.append(pt)
        else:
            bdryPts.append(pt)
            
    return intPts, bdryPts
    
def isMostRound(a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23):
    if b1 == b2 and b1 == b3:
        if b1%2 == 0:
            if a12 == -b1*0.5 and b12 == b1*0.5:
                if a12 == a23 and a12 == a13:
                    if b12 == b23 and b12 == b13:
                        return True
    return False
 
 
def fastTotalPts(a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23):
    tot_pts = 0
    bdry_pts = 0
    for z in range(0,b3+1):
        xmin = max(0,z-b13)
        xmax = min(b1,z-a13)
        
        ymin = max(0,z-b23)
        ymax = min(b2,z-a23)
        
        a = xmax-xmin
        b = ymax - ymin
        min_ab = min(a,b)
        
        x_k1 = ymin - a12
        k1 = min(max(0,xmax-x_k1),min_ab)
        if k1 == min_ab and xmax-x_k1 > min_ab:
            ybig = xmax+a12
            q = ybig-ymin-min_ab
            b = b-q
        
        y_k2 = b12+xmin
        k2 = min(max(0,ymax-y_k2),min_ab)
        if k2 == min_ab and ymax-y_k2 > min_ab:
            xbig = ymax-b12
            q = xbig-xmin-min_ab
            a = a-q
        
        if a <= 0 or b <= 0:  #In this case Pick's theorem is invalid
            A = 0
            B = a+b+1
            tot_pts = tot_pts + A + B
            bdry_pts = bdry_pts+B

        else: #Use Pick's theorem
            A = a*b-(k1*k1+k2*k2)*0.5
            B = 2*a+2*b - (k1+k2)
            tot_pts = tot_pts + A + B*0.5 + 1
    
            if z == 0 or z == b3:
                bdry_pts = bdry_pts + A + B*0.5 + 1
            else:
                bdry_pts = bdry_pts + B

    return tot_pts, bdry_pts


#startTime = time.time()
 
 
 
 
e1 = []
e2 = []
ohps = 0
yay = 0
cout = 0
for i in range(10000):
    if i%100 == 0:
        print(i)
    a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23 = genIntPts(a,b)
    
    tempTotPts = []
    for k in range(1,5):
        allPtsList = findAllPts(k*a1,k*b1,k*a2,k*b2,k*a3,k*b3,k*a12,k*b12,k*a13,k*b13,k*a23,k*b23)
        intPts,bdryPts = intBdryPts(allPtsList)
        tempTotPts.append(len(intPts)+len(bdryPts))
    v = numpy.array([tempTotPts[0],tempTotPts[1],tempTotPts[2],tempTotPts[3]])

    A = numpy.array([[1,1,1,1],[8,4,2,1],[27,9,3,1],[64,16,4,1]])

    A_inv = numpy.linalg.inv(A)
    
    poly = A_inv.dot(v)
    #print(poly)
    e1.append(poly[1])
    e2.append(poly[0])
    #print(poly,e1,e2)
    
    
    #Using convhull
    """
    allPtsList = findAllPts(a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23)
    intPts,bdryPts = intBdryPts(allPtsList)
    try:
        hull = spa.ConvexHull(bdryPts)
    except:
        print(b1,b2,b3,a12,b12,a13,b13,a23,b23)
        ohps = ohps+1
        continue

    else:
        yay  = yay+1
        e1.append(hull.area)
        e2.append(hull.volume)
    """

    
    """ FAST
    fast_tot, fast_bdry = fastTotalPts(a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23)
    if len(intPts)+len(bdryPts) != fast_tot:
        print("Total: ", len(intPts)+len(bdryPts), "!=", fast_tot)
        print(a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23)
        input("Continue?")
    if len(bdryPts) != fast_bdry:
        print("Boundary: ", len(bdryPts), "!=", fast_bdry)
        print(a1,b1,a2,b2,a3,b3,a12,b12,a13,b13,a23,b23)
        input("Continue?")
    """
#print(time.time()-startTime)


x = []
y = []
for i in range(0,140):
    ytemp = (4*i*math.sqrt(i))/(6*math.sqrt(6))
    y.append(ytemp)
    x.append(i)
    




#print("yay = ", yay, "ohps = ", ohps, "count = ",cout)
plt.plot(e1,e2,'.')
plt.plot(x,y)
plt.show()

#You need to consider that the planes may have empty intersection with your current implementation.







    
    
    
    
    
    
    
"""    
e1 = []
e2 = []
for i in range(1000000):
    a1,b1,a2,b2,a3,b3 = intPts(a,b)
    V,B = ifCube(a1,b1,a2,b2,a3,b3)
    e1.append(B*0.5)
    e2.append(V)
    if i%10000 == 0:
        print(i)
    
x = []
y = []
for i in numpy.arange(1,250,0.5):
    x.append(i)
    ytemp = math.sqrt((i-1)/3)*(i-1)/3
    y.append(ytemp)
 
plt.plot(e1,e2,'.')
plt.plot(x,y)
plt.show()
"""