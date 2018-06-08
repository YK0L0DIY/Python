def arvore(a):
    v=a
    cont=2
    u=a-1
    print(" "*u,"*")
    while(v!=1):
        u=u-1
        print(" "*u,"*"*(1+cont))
        cont=cont+2
        v=v-1
    print(" "*(a-1),"*")
    print(" "*(a-1),"*")
h=int(input("Indique a altura da arvore: "))
arvore(h)
