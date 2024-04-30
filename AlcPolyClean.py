#Alcoved polytopes 2d cleaned up

from random import randint as ran
import matplotlib.pyplot as plt
import numpy
import math

#The maximal size of a rectangle
#does not effect running time but
#can make plots cluttered or non-responsive
#if too large.
maxa = 0
maxb = 50


#Generates the hyperplanes defining
#the polytope. Note that they are generated
#according to my "assumptions" from thesis
def intPts(a,b):
    a1 = 0
    b1 = ran(1,b)

    a2 = 0
    b2 = ran(1,b)
        
    
    if b1 == b2:
        a12 = ran(-b1,0)
        b12 = ran(1,b2)
    elif b2-a2 < b1-a1:
        a12 = ran(a2-b1,b2-b1)
        b12 = ran(a2-a1,b2-a1)
    else:
        a12 = ran(a2-b1,a2-a1)
        b12 = ran(b2-b1,b2-a1)
    
    return a1,b1,a2,b2,a12,b12
    
    
#Uses Pick's theorem and my resutls
#to quickly find the area and number of
#integer points (boundary + internal)
def bdryPtsAndArea(a1,b1,a2,b2,a12,b12):
    k1 = b1-a2+a12
    k2 = b2-b12-a1
    B = 2*(b1-a1) + 2*(b2-a2) - (k1+k2)
    I = (b1-a1-1)*(b2-a2-1)
    A = (b1-a1)*(b2-a2) - (k1*k1+k2*k2)*0.5
    return A,B,I
    
def pltMaxLine():
    x = []
    y = []
    for i in numpy.arange(0,2*maxb,0.5):
        x.append(i)
        ytemp = i*i/3
        #print(ytemp)
        y.append(ytemp)
    mostRound, = plt.plot(x,y,'orange', label = '$c_{1}^{2} / 3$')
    plt.legend()   
        
def pltSquareLine():
    x = []
    y = []
    for i in numpy.arange(0,2*maxb,0.5):
        x.append(i)
        ytemp = i*i/4
        #print(ytemp)
        y.append(ytemp)
    squareLine, = plt.plot(x,y,'g', label= '$c_{1}^{2} / 4$')
    plt.legend()
        
def pltTriLine():
    x = []
    y = []
    for i in numpy.arange(0,2*maxb,0.5):
        x.append(i)
        ytemp = 2*i*i/9
        #print(ytemp)
        y.append(ytemp)
    plt.plot(x,y,'g')
    plt.legend()

def pltRectangleLines():
    for q in numpy.arange(0,20,1):
        xlim = 2*maxb
        if q%2==0:
            plt.plot([q*q*0.25+2*q+1,xlim],[q*q*q*0.25+5*q*q*0.25+q,xlim*q-3*q*q*0.25],'green')
            plt.plot([q*q*0.25+2*q+1,xlim],[q*q*q*0.25+5*q*q*0.25+q,xlim*(q+1)-(q+1)*(q+1)],'green')
        else:
            plt.plot([q*q*0.25+2*q+3*0.25,xlim],[q*q*q*0.25+5*q*q*0.25+3*q*0.25-0.25,xlim*q-3*q*q*0.25],'red')
            plt.plot([q*q*0.25+2*q+3*0.25,xlim],[q*q*q*0.25+5*q*q*0.25+3*q*0.25-0.25,xlim*(q+1)-(q+1)*(q+1)],'red')
    
def findInvalidPts(maxc1):
    c1list = []
    c2list = []
    validc1 = []
    validc2 = []    
    for c1 in numpy.arange(2, maxc1, 0.5):
        maxxb = int(c1)
        print(c1)
        solutionFound = False
        for c2 in numpy.arange(int(c1*c1*0.25),int((c1*c1)/3),0.5):      #int(c1*c1*0.25)
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
    
    plt.plot(validc1,validc2,'.b')                                
    plt.plot(c1list,c2list,'.r')

    
    
    
    
def main():
    #Lists to keep coefficients (i.e A and B/2)
    c1 = []
    c2 = []
      
    for i in range(2000000):
        a1,b1,a2,b2,a12,b12 = intPts(maxa,maxb)
        
        A,B,I = bdryPtsAndArea(a1,b1,a2,b2,a12,b12)
        if A != 0: #A should never be zero but you can never be sure...
            c1.append(B*0.5)
            c2.append(A)
            
        if i%100000 == 0:
            print(i)
        
    
    
        
        
    plt.plot(c1,c2,'.b')
    findInvalidPts(50) #anything above 50 takes greatly effects runtime.
    pltMaxLine()
    pltSquareLine()
    #pltTriLine()
    #pltRectangleLines()    
    plt.xlabel("$c_{1}$")
    plt.ylabel("$c_{2}$")

    #plt.xlim([0,50.25])
    #plt.ylim([-5,900])
    plt.show()
    
 
main()