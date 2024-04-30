#A small script to determine all solutions
#to the system of equations
# 2a+2b-k1-k2 = 0
#2ab -k1^2 - k2^2 = 0
#reduced modulo p.


def checkForSols(p):
    for a in range(p):
        for b in range(p):
            for k1 in range(p):
                for k2 in range(p):
                    if (2*a+2*b - k1 - k2)%p == 0 and (2*a*b - k1*k1-k2*k2)%p == 0:
                        print("(a, b, k1, k2) = ", a, b, k1, k2)

def main():
    p = int(input("Solve equations mod p, where p = "))
    checkForSols(p)

main()