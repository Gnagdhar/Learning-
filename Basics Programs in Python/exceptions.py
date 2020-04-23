DIGIT_maps={"One": 1, "two":2,"Three":3, "Four":4,"Five":5,"Six":6,"seven":7,"Eight":8,"Nine":9}
def convert(s):
    try:
        print(DIGIT_maps[s])
        x=int(DIGIT_maps[s])
        print("Int",x)
    except KeyError:
        print("Key error")
def string_log(s):
    v=convert(s)
    log(v)