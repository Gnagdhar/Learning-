print("hello world")
# Relational operators
#Control flow
print("--------If Example-----------")
value=1
if(value):
    print("If block")
    print("2nd line in if")
else:
    print("else block")
    print("2nd line in else")
print("--------while Example---------")
count=5
while(count!=0):
    print(count)
    count=count-1
print("--------For Example---------")
for i in range(5):
    print(i)
print("---------String----------")
string="Hello"
print(string[1])

print("---------Taking inputs in python----------")
select=int(input("Enter age in number\n"))
select2=input("Enter name as string\n")
print(type(select))
print(type(select2))
print(select)
print(select2)