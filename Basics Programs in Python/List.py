List1=["Hello",1234,"Geek"]
List2=["How",5678,"areyou"]
print(List1+List2)
List1.append(List2)#it will take as single list
print(List1)
List1.extend(List2)#it will take all teh conenets as diff arsg in list
print(List1)
print(len(List1))
List1.pop()#it will remove lasr items
print(List1)
#List1.sort() it will apply for same type like int
List1.remove(1234)
print(List1)
List=[20,10,5,4,3,1,2]
List.sort()
print(List)