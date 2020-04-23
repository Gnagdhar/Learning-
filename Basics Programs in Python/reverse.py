def len(String):
    count=0;
    for i in String:
        count=count+1
    print("String length is:", count)
def reverse(String):
    print(String[::-1])
def palindrome(String):
    rev=String[::-1]
    if(rev==String):
        print("Given string is palindrome")
    else:
        print("Given string is not a palindrome")
len("Naman@123")
reverse("Naman@123")
palindrome("gadagaa")
'''The operator “==” compares values of two objects
    is compares adress'''