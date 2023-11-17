
with open('t1.txt', 'r') as file:
    lines = file.read()
i=0
#for j in lines:
#    lines[i]=lines[i].replace("\n", "")
#    lines[i]=lines[i].split(" ")
#    i += 1
lines  = lines.split()
print(lines)


for my_list in lines:

    print(my_list)
    a = my_list[0]
    flag = 0
    count = 0
    if my_list[0] == my_list[-1]:
        flag-=2
    for i in my_list :
        if a != i:
            flag+=1
        a = i
    a = my_list[1]
    if(flag==0):
        for i in my_list[1:-1]:
            if a != i:
                flag += 1
            a = i

    print(flag)
    if flag==-2:
        print("The elements of the sequence are equal")
    elif  flag==1:
        print("If you remove one element, the remaining elements will be equal")
    else:
        print("The elements of the sequence are not equal")
    print("\n")