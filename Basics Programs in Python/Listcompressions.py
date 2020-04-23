list_=[print(x/2) for x in range(20)]


list__=[10,20,30,40,50,60,70,80]
size_of_list=len(list__)
print("------------")
print(size_of_list)
new_list=[]
for i in range(size_of_list/2+1):
    new_list.append(list__[i])
    print(new_list)