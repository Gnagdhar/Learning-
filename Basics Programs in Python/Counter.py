from collections import Counter
def duplicate(String):
    wc=Counter(String)
    j=-1
    for i in wc.values():
        j=j+1
        if(i>1):
            print(wc.values()[j],)
duplicate("aabbccddefghijkl")