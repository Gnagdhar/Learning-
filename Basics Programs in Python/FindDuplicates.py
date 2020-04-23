from collections import Counter
print("----------remove Duplicates in String----------")
def remove_duplicate(String):
    newStr=""
    for i in range(len(String)):
        for j in range(len(String)):
            if(String[i]==String[j]):
                break

        if(i==j):
            newStr=newStr+String[i]
    print("String is:",newStr)
remove_duplicate("aabbccddef")

print("----------remove Duplicates in List------------")
def remove_duplicates(List):
    newList=[]
    for i in List:
        if i not in newList:
            newList.append(i)
    print(newList)
remove_duplicates([10, 20, 40, 50, 10, 20])