def ex1():
    def fatorial(a):
        if a == 1:
            return 1
        else:
            f = a * fatorial(a - 1)
        return f

    num = float(input("Indique um numeor para calcular o fatorial: "))
    print(fatorial(num))


def ex2():
    def fibonaci(a):
        if a == 1 or a == 0:
            return 1
        else:
            s = fibonaci(a - 1) + fibonaci(a - 2)
        return s

    num = float(input("Indique um numero para a funcao: "))
    print(fibonaci(num))


def ex3():
    def soma(a):
        if a == 1:
            return 1
        else:
            s = a + soma(a - 1)
        return s

    num = float(input("Indique um numero para calclar a soma: "))
    print(soma(num))


def ex4():



def ex5():
    m = int(input('Insira m: '))
    n = int(input('Insira n: '))

    def mdc(m, n):
        if n == m:
            r = n
        if m > n:
            r = mdc(m - n, n)
        if m < n:
            r = mdc(m, n - m)
        return r

    print(mdc(m, n))


def ex6():
    def a(m, n):
        if m == 0:
            f = n + 1
            return f
        elif m > 0 and n == 0:
            f = a(m - 1, 1)
            return f
        else:
            f = a(m - 1, a(m, n - 1))
            return f

    num = float(input("Indique o primeiro numero para aplicar na funcao: "))
    num2 = float(input("Indique o segundo numero para aplicar na funcao: "))
    print(a(num, num2))


def ex7():
    def pascal(lin,col):
        if col==0 or col==lin:
            return 1
        else:
            f=pascal(lin-1,col-1)+pascal(lin-1,col)
            return f
    print(pascal(4,2))

def ex8():
    def pascal(lin, col):
        if col == 0 or col == lin:
            return 1
        else:
            f = pascal(lin - 1, col - 1) + pascal(lin - 1, col)
            return f

    a = 0
    n = int(input("Indique o numero que linhas do triangulo de pascal: "))
    while n != a:
        b = 0
        k = ""
        while b <= a:
            k = str(k) + str(" ") + str(pascal(a, b))
            b = b + 1
        print(k)
        a = a + 1