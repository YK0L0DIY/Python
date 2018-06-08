def ex3():
    def ciclo_while():
        n=6
        c=0
        while c<=n:
            print (2**c)
            c+=
    def ciclo_for():
        for n in range(0,):
            print (2**n)

def ex4():
    def fatorial(a):
        fat=1
        for x in range(2,a+1):
            fat=fat*x
        return fat
    num=int(input("que fatorial pretende calcular: "))
    print (fatorial(num))

def ex5():
    def fibonacci(a):
        st = "1 1"
        k = 1
        c = 1
        for x in range(3, a + 1):
            soma1 = k + c
            c = k
            k = soma1
            st = str(st) + " " + str(soma1)
        return st
    n=int(input("Indique um n: "))
    print(fibonacci(n))

def ex6():
    def fibonacci_ate(a):
        st = "1 1"
        k = 1
        c = 1
        for x in range(3, a):
            soma1 = k + c
            if soma1 > a:
                break
            c = k
            k = soma1
            st = str(st) + " " + str(soma1)
        return st

    n = int(input("Indique um n: "))
    print(fibonacci_ate(n))

def ex7():
    def e_primo(a):
        for x in range(2, a):
            if a % x == 0:
                falso = "nao e primo"
                return falso
        verdade = "e primo"
        return verdade
    n=int(input("indique um num para teste: "))
    print(e_primo(n))

def ex8():
    def e_primo(a):
        for x in range(2, a):
            if a % x == 0:
                return False
        return True

    def mostra_primos(a):

        for x in range(2, a):
            if True == e_primo(x):
                print(x)

    n = int(input("indique um num para teste: "))
    mostra_primos(n)

def ex9():
    def e_primo(a):
        for x in range(2, a):
            if a % x == 0:
                return False
        return True
    def conta_primos(a):
        c=0
        for x in range(2, a):
            if True == e_primo(x):
                c=c+1
        return c
    print(conta_primos(10))
