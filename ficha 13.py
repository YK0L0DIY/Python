def ex1():list_tel= {"joao":961111, "ana":932222, "carla":913333, "manuel":964444}
    def encontra_telefone(nome,ltel):
        num=ltel.get(nome)
        if num==None:
            return 0
        return num
    print(encontra_telefone("jao",list_tel))

def ex2():
    list_tel = {"joao": 961111, "ana": 932222, "carla": 913333, "manuel": 964444}

    def encontra_telefone(nome, ltel):
        num = ltel.get(nome)
        if num == None:
            return 0
        return num

    def novo_tel(nome, num, ltel):
        ltel[nome] = num

    novo_tel("ana", "91292", list_tel)
    print(encontra_telefone("ana", list_tel))

def ex3():
    list_tel = {"joao": 961111, "ana": 932222, "carla": 913333, "manuel": 964444}
    l = []
    for nome in list_tel:
        m = ("%s : %s" % (nome, list_tel[nome]))
        l.append(m)

    def cliente(num, list):
        for x in range(len(list)):
            if (num in list[x]):
                c = list[x]
                c = c.strip('1234567890.: ')
                return c
            elif num not in list[x]:
                return "DESCONHECIDO"

    print(cliente("961111", l))




def ex4():
    list_tel = {"joao": 961111, "ana": 932222, "carla": 913333, "manuel": 964444}
    l = []
    for nome in list_tel:
        m = ("%s : %s" % (nome, list_tel[nome]))
        l.append(m)

    l.sort()
    for x in range(len(l)):
        print(l[x])

def ex5e6():
    dicEnPt = {"white": "branco", "the": "o", "cat": "gato", "mouse": "rato",
               "chases": "persegue", "black": "preto"}

    def traduz(pal, dic):
        c = dic.get(pal)
        if c == None:
            return pal
        else:
            return c

    print(traduz("bird", dicEnPt))

def ex7():
    dicEnPt = {"white": "branco", "the": "o", "cat": "gato", "mouse": "rato",
               "chases": "persegue", "black": "preto"}

    def traduz(pal, dic):
        c = dic.get(pal)
        if c == None:
            return pal
        else:
            return c

    def palavra_para_portugues(palavra):
        return traduz(palavra, dicEnPt)

    print(palavra_para_portugues("cat"))

def ex8():
    dicEnPt = {"white": "branco", "the": "o", "cat": "gato", "mouse": "rato",
               "chases": "persegue", "black": "preto"}

    def traduz(pal, dic):
        c = dic.get(pal)
        if c == None:
            return pal
        else:
            return c

    def palavra_para_portugues(palavra):
        return traduz(palavra, dicEnPt)

    def lista_para_portugues(pal_list):
        l = []
        for x in range(len(pal_list)):
            c = palavra_para_portugues(pal_list[x])
            l.append(c)
        return l

    print(lista_para_portugues(["cat", "white"]))

def ex9():
    dicEnPt = {"white": "branco", "the": "o", "cat": "gato", "mouse": "rato",
               "chases": "persegue", "black": "preto"}

    def traduz(pal, dic):
        c = dic.get(pal)
        if c == None:
            return pal
        else:
            return c

    def palavra_para_portugues(palavra):
        return traduz(palavra, dicEnPt)

    def lista_para_portugues(pal_list):
        l = []
        for x in range(len(pal_list)):
            c = palavra_para_portugues(pal_list[x])
            l.append(c)
        return l

    def fraze_para_portugues(frase):
        c = ""
        l = []
        frase = str(frase) + str(" ")
        for x in range(len(frase)):

            if (frase[x] == " "):
                l.append(c)
                c = ""
            else:
                c = str(c) + str(frase[x])
        tra = lista_para_portugues(l)
        print(tra)
        frase_tra = ""
        for y in range(len(tra)):
            frase_tra = str(frase_tra) + str(tra[y]) + str(" ")
        return frase_tra

    print(fraze_para_portugues("the white cat chases the black mouse"))

def ex10():
    def exa():
        adeptos = {"benfica": ["joao", "ana", "carla"], "sporting": ["hugo", "patricia"],
                   "porto": ["jose"]}

        def consulta_clube(nome, d):
            lista_adep = list(d.values())
            lista_clubes = list(d.keys())
            for x in range(len(lista_clubes)):
                if (nome in lista_adep[x]):
                    return lista_clubes[x]
            return "NAO TEM CLUBE"

        print(consulta_clube("hugo", adeptos))

    def exb():
        adeptos = {"benfica": ["joao", "ana", "carla"], "sporting": ["hugo", "patricia"],
                   "porto": ["jose"]}

        def mais_adeptos(dic):
            lista_adeptos = list(dic.values())
            lista_clubes = list(dic.keys())
            h = 0
            for x in range(len(lista_adeptos)):
                t = lista_clubes[x]
                k = lista_adeptos[x]
                g = len(k)
                if g > h:
                    h = g
                    best = t
            return best

        print(mais_adeptos(adeptos))
