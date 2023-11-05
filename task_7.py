my_list=[0,1,2,3,4,5,6,7,8,9]
print(my_list)
i=int(input());

i=i%len(my_list)
print(my_list[-i:] + my_list[:-i])

# и в право и в лево двигает