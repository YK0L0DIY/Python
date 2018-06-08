valor=float(input("valor= "))
c=valor;
k=valor
moeda2e =0
moeda1e =0
moeda50c =0
moeda20c =0
moeda10c =0

while c>0:
    if c/2>=0:
        moeda2e=c//2;
        c=c-moeda2e*2;
        continue
    elif c/1>=0:
        moeda1e=c//1;
        c=c-moeda1e*1;
        continue
    elif c/0.5>=0:
        moeda50c=c//0.5;
        c=c-moeda50c*0.5;
        continue
    elif c/0.2>=0 :
        moeda20c=c//0.2;
        c=c-moeda20c*0.2;
        continue
    else:
        moeda10c=c//0.1;
        c=c-moeda10c*0.1;
        continue

print(valor,"=",moeda2e," de 2 euros")
print(moeda1e ," de 1 euro")
print(moeda50c , " moedas de 50cent")
print(moeda20c," moedas de 20 cent")
print(moeda10c," moedas de 10 cent")