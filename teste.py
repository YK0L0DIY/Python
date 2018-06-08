import random

def lista():
    r = []

    while len(r) != 5040:
        for x in range(0, 10):
            for y in range(0, 10):
                if x != y:
                    for w in range(0, 10):
                        if x != w and y != w:
                            for z in range(0, 10):
                                if z != x and z != y and z != w:
                                    e = str(x) + str(y) + str(w) + str(z)
                                    if e not in r:
                                        r = r + [e]
    return r

def random_num():
    num = ""

    while len(num) < 4:

        d = str(int(random.random() * 10))

        if d not in num:
            num = num + d
    return num

num =random_num()
numeros=lista()

perguntas=[]


print(r)
print(c)
