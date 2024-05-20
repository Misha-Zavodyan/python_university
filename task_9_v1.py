from random import shuffle
import math
S=[[1,2],[3,4],[5,6],[7,8]]
def DiscCentr(a,b):
    return [((a[0]+b[0])/2),((a[1]+b[1])/2)]
def DiscR(a,b):
    return [math.sqrt((DiscCentr(a,b)[0]+b[0])**2+(DiscCentr(a,b)[1]+b[1])**2)]
def SmallDisk(a,b):
    return [DiscCentr(a,b),DiscR(a,b)]
def inDisk(a,b):
    if DiscR(a,b[0]) <= b[1]:
        return True
    else:
        return False

def DiscFor3point(p1,p2,p3):
    # http://algolist.ru/maths/geom/equation/circle.php
    ma=(p2[1]-p1[1])/(p2[0]-p1[0])
    mb=(p3[1]-p2[1])/(p3[0]-p2[0])
    center_x = (ma*mb*(p1[1]-p3[1]) + mb*(p1[0]+p2[0]) - ma*(p2[0]+p3[0]))/(2*(mb-ma))
    center_y = -(center_x - (p1[0]+p2[0])/2 )/(mb) + (p1[1]+p2[1])/2
    radius = DiscR([center_x,center_y],p1)
    return [[center_x,center_y],radius]
def MinDiscWith2Point(a,p,q):
    D0 = SmallDisk(p, q)
    for i in range(len(a)):
        if not (inDisk(i, D0)):
            D0=DiscFor3point(i,p,q)
    return D0
def MinDiscWithPoint(a,p):
    P = shuffle(a)
    D1 = SmallDisk(P[0],p)
    for i in range(len(P))[1:]:
        if not(inDisk(P[i],D1)):
            D1=MinDiscWith2Point(P[:(i-1)],i,p)

    return  D1

def MinDisc(S):
    P = shuffle(S)
    D=SmallDisk(P[0],P[1])
    for i in range(len(P))[2:]:
        if not(inDisk(P[i],D)):
            D=MinDiscWithPoint(P[:(i-1)],i)

    return D

print(MinDisc(S))



