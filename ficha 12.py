def ex1():
    def a():
        t = (("jarro", 20.6), ("almofada", 18), ("candeeiro", 45))

        def consulta_preco(artigo, tabela):
            for x in range(len(tabela)):
                w = tabela[x]
                for y in range(len(w)):
                    if w[y] == artigo:
                        return w[y + 1]

        print(consulta_preco("jarro", t))
    def b():
        t = (("jarro", 20.6), ("almofada", 18), ("candeeiro", 45))

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

        print(consulta_elemento(max, t))





def ex2():
    def canto_oposto(pt, largura):
        a,b=pt
        c=a-largura
        d=b+largura
        pt2=c,d
        return pt2
    canto_oposto((1,2),3)

def ex3():
    def meio_segemnto(p1,p2):
        a,b=p1
        c,d=p2
        x=(a+c)/2
        y=(b+d)/2
        pm=x,y
        return pm
    meio_segemnto((1,2),(3,4))

def ex4():
    posicao = [("joao", 300, 20), ("ana", 80, 15), ("patricia", 17, 90)]
    def cordenadas(pos, nome):
        for x in range(len(pos)):
            e=pos[x]
            if e[0]==nome:
                n,x,y=e
                c=x,y
                return c
        else:
            return None
    cordenadas(posicao,"patricia")

def ex5():
    posicao = [("joao", 300, 20), ("ana", 80, 15), ("patricia", 17, 90)]

    def cordenadas(pos, lat):
        c = []
        for x in range(len(pos)):
            e = pos[x]

            if e[2] > lat:
                c.append(e[0])
        return c

    print(cordenadas(posicao, 18))

def ex6():
    posicao = [("joao", 300, 20), ("ana", 80, 15), ("patricia", 17, 90)]

    def cordenadas(pos, lon):
        c = []
        for x in range(len(pos)):
            e = pos[x]

            if e[1] > lon:
                c.append(e[0])
        return c

    print(cordenadas(posicao, 100))

def ex7():
    def conjunsto_de_letras(st):
        lit = []
        for x in range(len(st)):
            if (st[x] in lit) == False:
                lit.append(st[x])
        return lit

    print(conjunsto_de_letras("era uma vez"))

def ex8():
