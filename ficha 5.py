def ex1():
    def maximo(a, b, c):
        if a < b and c < b:
            return b
        elif a < c and b < c:
            return c
        elif c < a and b < a:
            return a

    num1 = float(input("Indique o 1 nuemro: "))
    num2 = float(input("Indique o 2 nuemro: "))
    num3 = float(input("Indique o 3 nuemro: "))

    max = maximo(num1, num2, num3)

    print("o maximo e: ", max)
def ex2():
    def minimo(a, b, c):
        if a > b and c > b:
            return b
        elif a > c and b > c:
            return c
        elif c > a and b > a:
            return a

    num1 = float(input("Indique o 1 nuemro: "))
    num2 = float(input("Indique o 2 nuemro: "))
    num3 = float(input("Indique o 3 nuemro: "))

    min = minimo(num1, num2, num3)

    print("o maximo e: ", min)

def ex3():
    def maximo(a, b, c):
        if a < b and c < b:
            return b
        elif a < c and b < c:
            return c
        elif c < a and b < a:
            return a

    def triangulo(a, b, c):
        if a > b + c:
            print("Nao existe triangulo")
        elif (a ** 2) == (b ** 2) + (c ** 2):
            print("triangulo rectângulo")
        elif (a ** 2) > (b ** 2) + (c ** 2):
            print("triangulo obtuso")
        else:
            print("triangulo agudo")

    num1 = float(input("Indique o 1 nuemro: "))
    num2 = float(input("Indique o 2 nuemro: "))
    num3 = float(input("Indique o 3 nuemro: "))

    max = maximo(num1, num2, num3)
    if max == num1:
        triangulo(num1, num2, num3)
    elif max == num2:
        triangulo(num2, num1, num3)
    else:
        triangulo(num3, num1, num2)

def ex4():
    import math

    def raiz1(a, b, c):

        if (b ** 2 - 2 * a * c) >= 0:
            r1 = math.sqrt(b ** 2 - 2 * a * c)
            x1 = (-b + r1 / 2 * a)
            return (x1)
        return

    def raiz2(a, b, c):
        if (b ** 2 - 2 * a * c) >= 0:
            r2 = math.sqrt(b ** 2 - 2 * a * c)
            x2 = (-b - r2 / 2 * a * c)
            return (x2)
        else:
            return

    print(raiz1(2, 3, 2))
    print(raiz2(2, 3, 2))

def ex5():
    def calcula(a,b,c):
        if c=="+":
            r=a+b
            return r
        elif c=="-":
            r=a-b
            return r
        elif c=="*":
            r=a*b
            return r
        else:
            r=a/b
            return r
    v1=float(input("Indique o primeiro valor: "))
    v2=float(input("Indique o segundo valor: "))
    op=str(input("Indique o operador: "))
    print(calcula(v1,v2,op))

def ex6():
    def mdc(a, b):
        if a == b:
            return a
        elif a > b:
            r = b
            while r != 0:
                if a % r == 0:
                    break
                c = r
                r = a % c
                a = c

        else:
            r = a
            while r != 0:
                if b % r == 0:
                    break
                c = r
                r = b % c
                b = c
                print(b)
        return r
    v1=float(input("Indique o 1 valor: "))
    v2=float(input("Indique o 2 valor: "))
    print("O mdc de ",v1," e ", v2," e: ",mdc(v1, v2))

def ex7():
    def mdc(a, b):
        if a == b:
            return a
        elif a > b:
            r = b
            while r != 0:
                if a % r == 0:
                    break
                c = r
                r = a % c
                a = c

        else:
            r = a
            while r != 0:
                if b % r == 0:
                    break
                c = r
                r = b % c
                b = c
                print(b)
        return r
    def mmc(a,b):
        mmc=(a*b)/mdc(a,b)
        return mmc
    v1 = float(input("Indique o 1 valor: "))
    v2 = float(input("Indique o 2 valor: "))
    print("O mmc de ",v1," e ", v2," e: ",mmc(v1, v2))

def ex8():
    def somacubos(a):
        if a==(((a//100)**3)+(((a-(a//100)*100)//10)**3)+((a-((a//100)*100)-(((a-((a//100)*100))//10)*10))**3)):
            b="E igual"
            return b
        else:
            b="Nao e igual"
            return b
    num=float(input("Indique um numero: "))
    print(somacubos(num))

def ex9():
    def serie(a):
        b=0
        c=1
        while c!=20:
            if (c==1)or(c==5)or(c==9)or(c==13)or(c==17):
                b=b+(1/c)*a**c
                c=c+1
            elif (c==3)or(c==7)or(c==11)or(c==15)or(c==19):
                b=b-(1/c)*a**c
                c=c+1
            else:
                c=c+1
        return b
    num=float(input("Indique um numero: "))
    print(serie(num))

def ex10():
    def fatorial(a):
        fat=1
        while a!=0:
            fat=fat*a
            a=a-1
        return fat
    num=float(input("Indique um numero: "))
    print("Fatorial de ",num," e: ",fatorial(num))

inicio=float(input("Qual e o exercicio[1-10]: "))
if inicio==1:
    ex1()
elif inicio==2:
    ex2()
elif inicio==3:
    ex3()
elif inicio==4:
    ex4()
elif inicio==5:
    ex5()
elif inicio==6:
    ex6()
elif inicio==7:
    ex7()
elif inicio==8:
    ex8()
elif inicio==9:
    ex9()
elif inicio==10:
    ex10()
