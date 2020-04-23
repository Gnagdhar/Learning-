import array;
from collections import Counter
arr1 = array.array('i', (10, 20, 30, 40))
print(len(arr1))

arr2 = [None] * len(arr1)
for i in range(0, len(arr1)):
    arr2[i] = arr1[i]

for i in range (len(arr2)):
    print(arr2[i])

def freq_array(arr1):
    wc=Counter(arr1)
    print(wc)
freq_array(arr1)
#comments
