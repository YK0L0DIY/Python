valor=float(input("valor= "));
contador=valor;
moeda2=0;

while contador!=0:
    if contador/2>=0:
        moeda2=(contador//2)
        contador=contador%2
    if contador/1>=0:
        print(contador)
print(moeda2)
print(contador)