import math

def exercicio1():
    def ex1(a):
        c=a+1;
        return c;

    b=(float(input("Indique um numeoro: ")));
    sucesor=ex1(b);
    print(sucesor);
def exercicio2():
    def ex2(a):
        c=a+1;
        quadrado=c**2;
        return quadrado;
    b = (float(input("Indique um numeoro: ")));
    sucesor=ex2(b);
    print(sucesor);
def exercicio3():
    def ex3(a,b,c):
        velocidade=a+b*c;
        return velocidade;
    vInicial=float(input("Indique a velocidade inicial: "));
    aceleracao=float(input("Indique a aceleracao: "));
    tempo=float(input("Inddique o tempo de de viajem: "));
    v=ex3(vInicial,aceleracao,tempo);
    print(v);
def exercicio4():
    def ex4(a,b,c,d):
        posicao=a+b*c+0.5*d*c;
        return posicao;
    pInicial=float(input("Indique a posicao inicial"))
    vInicial=float(input("Indique a velocidade inicial"))
    tempo=float(input("Indique o tempo de viajem"))
    acelecarao=float(input("Indique a aceleracao"))
    p=ex4(pInicial,vInicial,tempo,acelecarao);
    print(p);
def exercicio5():
    def ex5(w):
        u=len(w);
        print (u);
        pr=70-u;
        k=0;
        while k!=pr:
            print(" ",end="")
            k=k+1;
        print(w)
    c=str(input("Indique a string: "));
    w=ex5(c);
def exercicio6():
    def ex6(a,b,c):
    if a==1:
        custo=a*b
        return custo
    else:
        custo=1*b+(a-1)*c
        return custo

    liv=int(input("Indique o numero de livros: "))
    custo1=float(input("Indique o custo da primeira copia: "))
    custo2=float(input("Indique o custo unitario dos proximos livros: "))
    print(ex6(liv,custo1,custo2))


    #ex7 perguntar

def exercicio8():
    def tempoDecorrido(a,b):
        t=b/a;
        return t
    velocidade=float(input("Indique a velocidade em km/h: "))
    distancia=float(input("Indique a distancia a percorrer em km: "))
    print("Vai demorar ", tempoDecorrido(velocidade, distancia)," horas")

def exercicio9():
    def tempoDeChegada(a,b):
        t = b / a;
        return t
    c=3;
    tempo=0
    troco=0
    while c!=0:
        velocidade = float(input("Indique a velocidade no em km/h: "))
        distancia = float(input("Indique a distancia a percorrer no em km: "))
        tempo=tempo+tempoDeChegada(velocidade, distancia)
        c=c-1
    print("Vai demorar ",tempo," horas ate percorrer a distancia toda")

def exercicio10():
    def triangulo(a,b,c):
        if a+b>c:
            if a==c and c==b:
                t="equilatero"
                return t
            elif (a==b and c!=a )or(a==c and a!=b)or(b==c and a!=c):
                t="isosceles"
                return t
            else:
                t="escaleno"
                return t
        else:
            t="Nao existe"
            return t

    l1=float(input("Indique o primero lado: "))
    l2=float(input("Indique o segundo lado: "))
    l3=float(input("Indique o terceiro lado: "))
    print(triangulo(l1,l2,l3))

print("Ex 1");
print("Ex 2");
print("Ex 3");
print("Ex 4");
print("Ex 5");
print("Ex 6");
print("Ex 7");
print("Ex 8");
print("Ex 9");
print("Ex 10");

ex=int(input("Qual o exercissio[1 a 10]: "));
if ex==1:
    exercicio1();
elif ex==2:
    exercicio2();
elif ex==3:
    exercicio3();
elif ex==4:
    exercicio4();
elif ex==5:
    exercicio5();
elif ex==6:
    exercicio6();
elif ex==7:
    exercicio7();
elif ex==8:
    exercicio8();
elif ex==9:
    exercicio9();
elif ex==10:
    exercicio10();
