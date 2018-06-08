valor=float(input("Indique o valor do dinheiro: "));
c=valor;
m2=0;
m1=0;
m050=0;
m020=0;
m010=0;

while c!=0:
    if c//2>=0:
        m2=c%2;
        c=c-m2*2;
    elif c//1>=0:
        m1=c%1;
        c=c-m1*1;
    elif c//0.5>=0:
        m050=c%0.5;
        c=c-m050*0.5;
    elif c//0.2>=0 :
        m020=c%0.2;
        c=c-m020*0.2;
    else:
        m010=c%0.1;
        c=c-m010*0.1;
print(valor)