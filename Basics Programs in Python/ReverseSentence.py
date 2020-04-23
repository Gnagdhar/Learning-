def rev_each_word(String):
    eachValue=String.split()
    newList=""
    for i in eachValue:
        word=i;
        newList=newList+ ' '+(word[::-1])
    print("-----------------------------")
    print(newList)

def rev_sentence(String):
    eachValue = String.split()
    newList = ""
    for i in eachValue:
        newList=i+ ' '+newList
    print("-----------------------------")
    print(newList)

def rev_senetnce_word(String):
    eachValue = String.split()
    newList = ""
    for i in eachValue:
        word = i;
        newList =(word[::-1]) +' '+newList
    print("-----------------------------")
    print(newList)
rev_each_word("Kannada is great langugage")
rev_sentence("Kannada is great langugage")
rev_senetnce_word("Kannada is great langugage")