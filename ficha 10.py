def ex2():
    def verifica_ordem(a):
        for x in range(len(a) - 1):
            if a[x] > a[x + 1]:
                return False
        return True

    print(verifica_ordem([1, 2, 1]))

def ex3():
    def corta(a):
        a.remove(a[0])
        a.remove(a[len(a) - 1])
        return a

    #print(corta([1, 2, 3, 4, 5, 6]))
    def corta(a):
        a.remove(a[0])
        a.remove(a[len(a) - 1])
        return a

    # print(corta([1, 2, 3, 4, 5, 6]))
    def meio(c):
        v = corta(c[:])
        return v

    l1 = [1, 2, 3, 4]

    l2 = meio(l1)
    print(l1)
    print(l2)

def ex4():
    def contar_elementos(a, b):
        w = 0
        for x in range(len(a)):
            for y in range(len(b)):
                if a[x] == b[y]:
                    w = w + 1
        return w

    print(contar_elementos([1, 2, 3, 4, 5], [2, 4]))

def ex5():
    def soma_colunas(a,b,c):
        k=[]
        for x in range(len(a)):
            j=a[x]+b[x]+c[x]
            k.append(j)
        return k
    print(soma_colunas([1,2,3],[2,3,4],[3,4,5]))

def ex6():
    def matriz_identidade(a, b, c):
        q = [1, 0, 0]
        w = [0, 1, 0]
        e = [0, 0, 1]
        if q == a and w == b and e == c:
            return True
        return False

def ex7():
    def combina(a, b):
        w = ""
        for x in range(len(a)):
            for y in range(len(b)):
                w = str(a[x]) + str(" ") + str(b[y])
                print(w)

    combina(["", ""], ["", ""])

def ex8():
    def descodifica(a, b):
        c = []
        for x in range(len(b)):
            y = b[x]
            w = a[y]
            c.append(w)
        return c

    print(descodifica("x", "y", "z"], [2, 0, 1]))


 def ex10():
    def acumulado(a):
        c = []
        w = 0
        for x in range(len(a)):
            y = a[x]
            w = w + y
            c.append(w)
        return c

    print(acumulado([1, 2, 3]))

def ex11():
    def a():
        t = [["jarro", 20.6], ["almofada", 18], ["candeeiro", 45]]

        def consulta_preco(artigo, tabela):
            for x in range(len(tabela)):
                w = tabela[x]
                for y in range(len(w)):
                    if w[y] == artigo:
                        return w[y + 1]

        print(consulta_preco("jarro", t))
    def b():
        t = [["jarro", 20.6], ["almofada", 18], ["candeeiro", 45]]

        def preco_max(tabela):
            k = []
            for x in range(len(tabela)):
                w = tabela[x]
                for y in range(len(w)):
                    k.append(w[1])
            k.sort()
            m = k[len(k) - 1]
            return m

        max = preco_max(t)

        def consulta_elemento(m, tabela):
            for x in range(len(tabela)):
                w = tabela[x]
                if w[1] == m:
                    return w[0]

        (consulta_elemento(max, t))

def ex12():
    mensagem = "\nindique a sua opcao:\
            \nadicionar nome (1), consultar lista (2), retirar os primeiros n (3), sair (0)"
    k = []
    while True:
        print(mensagem)
        op = int(input("opcao -> "))
        if op == 0:
            break
        if op == 1:
            w = str(input("nome -> "))
            k.append(w)
        if op == 3:
            w = int(input("quantas vagas -> "))
            while w != 0:
                k.pop(0)
                w = w - 1
        if op == 2:
            print(k)
    print("fim de execucao")

def ex13():
    carinho = []
    precot = 0

    def add_carinho():
        if 0 == len(carinho):
            w = []
            w.append(str(input("produto: ")))
            w.append(1)
            preco = str(input("preco: "))
            w.append(preco)
            carinho.append(w)
        else:
            w = []
            w.append(str(input("produto: ")))
            w.append(1)
            preco = str(input("preco: "))
            w.append(preco)
            for x in range(len(carinho)):
                r = carinho[x]
                if w[0] == r[0]:
                    i = r[1]
                    carinho.pop(x)
                    e = w.pop(1)
                    e = i + 1
                    w.insert(1, e)
                    carinho.append(w)
                else:
                    carinho.append(w)

    while True:
        mensagem = "adicionar produto (1), consultar carinho (2), retirar (3), sair (0)"
        print(mensagem)
        op = int(input("Indique a opcao: "))
        if op == 1:
            add_carinho()
        if op == 0:
            break
        if op == 2:
            print(carinho)
            if len(carinho) == 0:
                print("carnho vasio")
            else:
                for k in range(len(carinho)):
                    e = carinho[k]
                    precot = precot + (int(e[1]) * int(e[2]))
                print(str(precot) + " e o total")
        if op == 3:
            r = str(input("que pretende remover: "))
            for x in range(len(carinho)):
                e = carinho[x]
                if r == e[0]:
                    carinho.pop(x)

def ex14():
