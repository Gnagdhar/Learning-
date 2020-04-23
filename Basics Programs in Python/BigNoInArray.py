def big_no():
    arr=[10,20,40,50,1234,60,70,80,8909,9090,6678,999909]
    big=arr[0]
    for i in range(len(arr)):
        if(arr[i]>big):
            big=arr[i]
    print("Big no is:",big)
big_no()

def small_no():
    arr=[10,20,40,50,1234,60,70,80,8909,9090,6678,999909]
    big=arr[0]
    for i in range(len(arr)):
        if(arr[i]<big):
            big=arr[i]
    print("Big no is:",big)
small_no()

def asecnding_order():
    arr = [10, 20, 40, 50, 1234, 60, 70, 80, 8909, 9090, 6678, 999909]
    temp=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j]<arr[i]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    for i in range(len(arr)):
        print(arr[i], end=" ")
asecnding_order()

def desecnding_order():
    print()
    arr = [10, 20, 40, 50, 1234, 60, 70, 80, 8909, 9090, 6678, 999909]
    temp=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j]>arr[i]):
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    for i in range(len(arr)):
        print(arr[i],end=" ")
desecnding_order()