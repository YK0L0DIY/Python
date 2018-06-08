def ex1():
    m = int(input('Insira n: '))
    n = int(input('Insira d: '))

    def mdc(m, n):
        if n == m:
            r = n
        if m > n:
            r = mdc(m - n, n)
        if m < n:
            r = mdc(m, n - m)
        return r

    def simplifica(n, d):
        com = mdc(n, d)
        n = n / com

        d = d / com

        c = str("n=") + str(n) + str(" ") + str("d=") + str(d)
        return c

    print(simplifica(m, n))


def ex2():
    def mdc(m, n):
        if n == m:
            r = n
        if m > n:
            r = mdc(m - n, n)
        if m < n:
            r = mdc(m, n - m)
        return r

    def simplifica(n, d):
        com = mdc(n, d)
        n = n / com

        d = d / com

        c = str("n=") + str(n) + str(" ") + str("d=") + str(d)
        return c

    def soma(n1, d1, n2, d2):
        somaN = (n1 * d2) + (n2 * d1)
        somaD = d1 * d2
        sim = simplifica(somaN, somaD)
        return sim

    n1 = float(input("Indique o numerador do primeiro numero: "))
    d1 = float(input("Indique o denominador do primeiro numero: "))
    n2 = float(input("Indique o numerador do segundo numero: "))
    d2 = float(input("Indique o denominador do segundo numero: "))
    print(soma(n1, d1, n2, d2))


def ex3():
    def revFatorial(n):
        res = n
        a = 1
        while res != 1:
            if res > 1:
                res = res / a

            elif res < 1:
                return 0
            a = a + 1
        return a - 1

    n = int(input("Indique um numero para calcular o revF: "))
    print(revFatorial(n))


def ex4():
    def revFatorialR(n):


def ex5():
    def novoEstado(est, com):
        if est == 1 and com == 1:
            r = "a abrir"
            return r
        elif (est == 1 and com == 2) or (est == 1 and com == 3):
            r = "fechado"
            return r
        elif est == 2 and com == 1:
            r = "a fechar"
            return r
        elif (est == 2 and com == 2) or (est == 2 and com == 3):
            r = "aberto"
            return r
        elif (est == 3 and com == 1) or (est == 4 and com == 1):
            r = "parado"
            return r
        elif (est == 3 and com == 2) or (est == 3 and com == 3):
            r = "fechado"
            return r
        elif (est == 4 and com == 2) or (est == 4 and com == 3):
            r = "aberto"
            return r
        else:
            if com == 2 or com == 3:
                r = "parada"
                return r
            print("1) a abrir")
            print("2) a fechar")
            s = int(input("Qual o estado anterio?"))
            if s == 1:
                r = "a fechar"
                return r
            else:
                r = "a abrir"
                return r

    print("1) fechada ")
    print("2) aberta ")
    print("3) a fechar ")
    print("4) a abrir ")
    print("5) parada ")
    estado = int(input("Indique o estado do porta: "))
    print("")
    print("")
    print("1) clicar")
    print("2) completo")
    print("3) fim")
    comando = int(input("Indique o comando: "))
    print(novoEstado(estado, comando))

def ex6():
    a = 0
    n = 5
    while n >= a:
        b = 0
        k = ""
        c = 1
        while b != a:
            k = str(k) + str(" ") + str(c)
            b = b + 1
            c = c + 1
        print(k)
        a = a + 1

def ex7():
    def arvore(a):
        v = a
        cont = 2
        u = a - 1
        print(" " * u, "*")
        while (v != 1):
            u = u - 1
            print(" " * u, "*" * (1 + cont))
            cont = cont + 2
            v = v - 1
        print(" " * (a - 1), "*")
        print(" " * (a - 1), "*")

    h = int(input("Indique a altura da arvore: "))
    arvore(h)
