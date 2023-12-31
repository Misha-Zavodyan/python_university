from random import shuffle
import math
import random
import time
def DiscR(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
def SmallDisk(a,b):
    center=[((a[0]+b[0])/2),((a[1]+b[1])/2)]
    return [center,DiscR(center,b)]
def inDisk(a,b):
    if DiscR(a,b[0]) <= b[1]:
        return True
    else:
        return False

def DiscFor3point(p1,p2,p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    try:
        y0 = (2 * (x1 - x3) * (y2 ** 2 - y1 ** 2 - x1 ** 2 + x2 ** 2) + 2 * (x1 - x2) * (x1 ** 2 - x3 ** 2 - y3 ** 2 + y1 ** 2)) / (4 * (y2 - y1) * (x1 - x3) - 4 * (x1 - x2) * (y3 - y1))
    except ZeroDivisionError:
        return SmallDisk(p1,p2)
    if x1 - x3 != 0:
        x0 = ((x1 ** 2 - x3 ** 2 - y3 ** 2 + y1 ** 2) + 2 * y0 * (y3 - y1)) / (2 * (x1 - x3))
    if x1 - x2 != 0:
        x0 = ((x1 ** 2 - x2 ** 2 - y2 ** 2 + y1 ** 2) + 2 * y0 * (y2 - y1)) / (2 * (x1 - x2))
    r = ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** (1 / 2)

    return [[x0, y0], r]
def MinDiscWith2Point(a,p,q):
    D0 = SmallDisk(p, q)
    for i in range(len(a)):
        if not (inDisk(a[i], D0)):
            D0=DiscFor3point(a[i],p,q)
    return D0
def MinDiscWithPoint(a,p):
    P=a
    shuffle(P)
    D1 = SmallDisk(P[0],p)
    for i in range(len(P))[1:]:
        if not(inDisk(P[i],D1)):
            D1=MinDiscWith2Point(P[:i],P[i],p)
    return D1

def MinDisc(S):
    P=S
    shuffle(P)
    D=SmallDisk(P[0],P[1])
    for i in range(len(P))[2:]:
        if not(inDisk(P[i],D)):
            D=MinDiscWithPoint(P[:i],P[i])

    return D



S=[[5, 6], [3, 4], [7, 8], [1, 2],[1,20]]
print(MinDisc(S))
#b=int(input("Enter the number of Big O time test: "))
#
# S.clear()
# avg_time_100=0
# avg_time_1000=0
# avg_time_10000 = 0
# for i in range(b):
#     print("100 points")
#     for k in range(3):
#         for j in range(100):
#             S.append([random.randint(0, 50),random.randint(0, 50)])
#
#         begin_time = time.perf_counter()
#         print(MinDisc(S))
#         avg_time_100 = (time.perf_counter() - begin_time)*1000
#         print(avg_time_100," ms" )
#         begin_time=0
#         S.clear()
#     print("1000 points")
#     for k in range(3):
#         for j in range(1000):
#             S.append([random.randint(0, 50),random.randint(0, 50)])
#
#         begin_time = time.perf_counter()
#         print(MinDisc(S))
#         avg_time_1000 = (time.perf_counter() - begin_time)*1000
#         print(avg_time_1000," ms" )
#         begin_time=0
#         S.clear()
#
#     print("10000 points")
#     for k in range(3):
#         for j in range(10000):
#             S.append([random.randint(0, 50),random.randint(0, 50)])
#
#         begin_time = time.perf_counter()
#         print(MinDisc(S))
#         avg_time_10000 = (time.perf_counter() - begin_time)*1000
#         print(avg_time_10000," ms" )
#         begin_time=0
#         S.clear()
#
# print("1000/100 point: ",avg_time_1000/avg_time_100 ,"10000/1000 point: ",avg_time_10000/avg_time_1000 , "10000/100 point: ",avg_time_10000/avg_time_100 ,)


import matplotlib.pyplot as plt
S.clear()
for k in range(5):
    fig, ax = plt.subplots()
    for j in range(21):
                S.append([random.randint(0, 50),random.randint(0, 50)])
                ax.plot(S[j][0], S[j][1], 'go')

    D= MinDisc(S)
    ax.add_patch(plt.Circle((D[0][0], D[0][1]), D[1], color='r' ))
    #Use adjustable='box-forced' to make the plot area square-shaped as well.
    ax.set_aspect('equal', adjustable='datalim')
    ax.plot()   #Causes an autoscale update.
    plt.show()
    S.clear()
    D=[[0,0],0]























