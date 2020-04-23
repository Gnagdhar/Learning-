def rotateRight(list,n):
    print(list)
    print(list[-n:]+list[0:-n])

def RotateLeft(list,n):
    print(list[0:n]+list[n:])
list=[10,20,30,40]
n=2
rotateRight(list,n)
list=[50,60,70,80]
n=2
RotateLeft(list,n)
