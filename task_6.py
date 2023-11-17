def dell(list):
    c_list = []
    flag = 0
    max_c=1
    max_b=list[0]
    for i in list:
        print( i)
        for j in range(len(c_list)):
            if i == c_list[j][0]:
                c_list[j][1] += 1
                flag = 1
                if c_list[j][1]>max_c:
                    max_c+=1
                    max_b =i

        if flag == 0:
            c_list.append([i, 1])
        flag = 0
        print(c_list)
    #for i in range(max_c):
    #    list.remove(max_b)
    list = [x for x in list if x != max_b]
    print(list)
    return len(list)

#[-2, -3, -4, -2]
my_list=[2,3,4,2, 3]
print(my_list)
print(dell(my_list))
print(my_list)
