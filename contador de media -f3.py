cont=0;
cont2=0;
x=1;
while x!=0:
    x=int(input("indique um valor: "));
    cont=cont+x;
    cont2=cont2+1;
cont2 = cont2 -1;
media=cont/cont2;
print("A soma e: ",cont);
print("Foram introduzidos",cont2," valores a media e: ",media);