from Underscore import x,_k,_single_method,__double_method
print(x)
#print(_k) can not access private
#_single_method() cant access bcause of private
#__double_method() cant access bcause of private
'''if we want to access above methods we need to import '''
print(_k)
_single_method()
__double_method()

'''-__ will help in below scenarios'''
class A:
    def _one(self):
        print("one")
class B(A):
    def __two(self):
        print("two")
b=B()
b._one()
#b._B___two()

'''__init__, __eq___ called as magic method '''

class mag:
    def __init__(self):
        print("init")
    def __len__(self):
        print("Length of mag")
    def __eq__(self):
        print("eq in mag functions")
i=mag()
len(i)
