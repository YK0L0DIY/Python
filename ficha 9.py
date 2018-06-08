def ex3():
    def letras_f(a):
        for x in range(0,len(a)):
            print(a[x])
    x=input("Indique a str: ")
    letras_f(x)

    def letras_w(a):
        c = 0
        while c <= len(a) - 1:
            print(a[c])
            c = c + 1
        return 0

    x = input("Indique a str: ")
    letras_w(x)

def ex4():
    def letras_f(a):
        for x in range(1, len(a) + 1):
            c = len(a) - x
            print(a[c])

    x = input("Indique a str: ")
    letras_f(x)

def ex5():
    def escala_in(a):
        for x in range(0, len(a)):
            u = len(a) - x
            print(a[0: u])

    a = "aula"
    escala_in(a)

def ex6():
    string = input("Indique a string: ")
    new_string = string
    for x in range(0, len(string)):
        c = len(string) - 1 - x
        new_string = new_string + str(string[c])
    print(new_string)

def ex7():
    def palidrono(a):
        for x in range(0, len(a)):
            c = len(a) - 1 - x
            if a[x] != a[c]:
                return False
        return True

    n = input("Indque a palavra: ")
    if True == palidrono(n):
        print(n)
    else:
        print("nao e palidrono")

def ex8():
    def a():
        def vogal(a):
            c = a.isalpha()
            return c

        b = input("indique uma palavra:")
        print(vogal(b))

    def b():
        def vogal(a):
            y = a.isalpha()
            return y

        b = input("indique uma palavra:")

        def conta_vogais(a):
            c = 0
            for x in range(0, len(a)):
                if True == vogal(a[x]):
                    c = c + 1
            return c

        print(conta_vogais(b))

def ex9():
    def ocorrencias(let,st):
        c=st.count(let)
        return c

    l=input("Indque a letra que pretende procurar:")
    s=input("Indique a vcs string:")
    print(ocorrencias(l,s))

def ex10():






def ex13():
    comp = "abcdefghijklmnopqrstuvwxyz"
    st = input("Indique uma string: ")
    new_st = ""
    st = st.lower()
    for x in range(0, len(st)):
        d = comp.find(st[x])
        f = d + 13
        if f > 25:
            f = f - 26
            new_st = new_st + comp[f]
        else:
            new_st = new_st + comp[f]
    print(new_st)