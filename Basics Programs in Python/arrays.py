import array;
arr=array.array('i',(10,20,30,40,50,60,70,80,90,100))
len=len(arr)
print("The arrays elements are: ")
for i in range(len):
    print(arr[i], end=" ")
print("\r")
arr.append(1000)
print(arr)
arr.insert(5,10000)
print(arr)
arr1=array.array('f',(10,20,30,40,50,60,70,80,90,100))
len1=len(arr1)
print("The arrays elements are: ")
for i in range(len1):
    print(arr1[i], end=" ")
print("\r")
arr1.append(1000)
print(arr1)
arr1.insert(5,10000.0)
print(arr1)
'''1. array(data type, value list) :- This function is used to create an array with data type 
and value list specified in its arguments. 
Some of the data types are mentioned in the table below.
2. append() :- This function is used to add the value mentioned in its arguments at the end of the array.
3. insert(i,x) :- This function is used to add the value at the position specified in its argument.
4. pop() :- This function removes the element at the position mentioned in its argument, and returns it.
5. remove() :- This function is used to remove the first occurrence of the value mentioned in its arguments.
filter_none
6. index() :- This function returns the index of the first occurrence of value mentioned in arguments.
7. reverse() :- This function reverses the array.
'''