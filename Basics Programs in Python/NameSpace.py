s=10
def scopes():
    s=5
    print(s)
print(s)
scopes()

'''def f(): 
	print s 

	# This program will NOT show error 
	# if we comment below line. 
	s = "Me too."

	print s 
# Global scope 
s = "I love Geeksforgeeks"
f() 
print s 
To make the above program work, 
we need to use “global” keyword.
We only need to use global keyword in a function if we want to do assignments / change them. 
global is not needed for printing and accessing. 
Why? Python “assumes” that we want a local variable due to the assignment to s inside of f(), 
so the first print statement throws this error message. Any variable which is changed or created inside of a function is local,
if it hasn’t been declared as a global variable.
To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example:'''
# This function modifies global variable 's'
def f():
	global s
	print (s)
	s = "Look for Geeksforgeeks Python Section"
	print (s)

# Global Scope
s = "Python is great!"
f()
print (s)
