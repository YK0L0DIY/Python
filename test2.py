###############
# analise_resultado- esta funcao analisa o resultado fornecido pelo jogador aproveitando apenas os touros e os porcos
#
# argumentos:
# resultado- input do resultado do numero fornceido pelo computador, string
#
# valor de retorno:
# geral- tupulo com o numero de touros e porcos, tupulo de inteiros
#
#################
def analise_resultado(resultado):
    resultado = list(resultado)
    touros=resultado[0]
    porcos=resultado[3]
    geral=int(touros),int(porcos)
    return (geral)

#################
# lista- esta funcao gera uma lsita com todos os nuemros possiveis
#
# argumentos:
# nem tem
#
# valor de retorno:
# lista- lista com todas as ipoteces de numeros, lista
#######################
def lista():
    lista = []
    while len(lista) != 5040:
        for x in range(0, 10):
            for y in range(0, 10):
                if x != y:
                    for w in range(0, 10):
                        if x != w and y != w:
                            for z in range(0, 10):
                                if z != x and z != y and z != w:
                                    e = str(x) + str(y) + str(w) + str(z)
                                    if e not in lista:
                                        lista = lista + [e]
    return lista

######################
# calculador_ten- esta funcao tenda em funcionar como o programa criado individualmente, ira comparar o resultado fornecido da lista com o anterior fornecido ao jogaro
#
# argumentos;
# possiveis- numero existenete na lista, string
# escolhido- numero anterior forncido pelo computador, string
#
# valor de retorno
# tupulo de 2 variaveis, touros e porcos em comparacao com os numeros, tupulo de inteiros
#################
def calculador_ten(possiveis,escolhido):
    touros=0
    porcos=0
    for x in range(len(escolhido)):
        for y in range(len(escolhido)):
            if escolhido[x]==possiveis[x] and x==y:
                touros=touros+1
    for x in range(len(escolhido)):
        if escolhido[x] in possiveis:
            porcos=porcos+1
    porcos=porcos-touros
    return touros,porcos

##################
# retirar_lista- esta funcao tende em retirar os numeros que estao a mais na lista atraves de uma comparca entre o numero fornecio anteriormente e o seu resultado
#
# argumentos:
# lista- lista total de escolhas,lista
# escolhido- numero escolhido anteriormnte , string
# score- resposta do utilzador, tupulo de inteiros
#
# valor de retorno:
# lista_nova- lista aualizada com os numeros que podem ser que o utilizador quer, lista
####################
def retirar_lista(lista,escolhido,score):
    lista_nova=[]
    for c in range(len(lista)):
        if (calculador_ten(lista[c],escolhido)==score):
            lista_nova=lista_nova+[lista[c]]
    return lista_nova

lista_total = lista()
tent_comp = []
pontuacoes = []
respostas=[]
print("SERA QUE ADEVINHO?\n")

while True:
    escolha_pc = lista_total[0]
    tent_comp=tent_comp+[escolha_pc]

    pontuacao = str(input("Tentativa %2s e %s. como foi? (xT, xP)? "% (len(tent_comp),escolha_pc)))
    respostas=respostas+[pontuacao]
    pontuacao = analise_resultado(pontuacao)
    pontuacoes=pontuacoes+[pontuacao]

    if pontuacao == (4, 0):
        print("ACERTEI!!")
        break
    lista_total = retirar_lista(lista_total,escolha_pc,pontuacao)

    if not lista_total:
        print("Nenhum numero certo!")
        break

print( "As suas respostas as tentativas foram:")
for x in range(len(tent_comp)):
    print(("%s : %s")%(tent_comp[x],respostas[x]))