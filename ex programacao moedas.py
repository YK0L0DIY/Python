dinheiro=float(input("Indique a quantia de dinheiro: "))

moeda2=dinheiro // 2.0
resto2=dinheiro % 2.0
resto2=round(resto2, 3)

moeda1=resto2 // 1.0
resto1=resto2 % 1.0
resto1=round(resto1, 3)

moeda50=resto1 // 0.50
resto50=resto1 % 0.50
resto50=round(resto50, 3)

moeda20=resto50//0.20
resto20=resto50%0.20
resto20=round(resto20, 3)

moeda10=resto20//0.10
moeda10=round(moeda10, 3)

print(dinheiro,"euros= ", end="");
if moeda2 != 0:
    print(int(moeda2),"x2 euros ",end="");
if moeda1 !=0:
    print(int(moeda1),"x1 euro ",end="");
if moeda50 != 0:
    print(int(moeda50),"x50 cent ",end="");
if moeda20 != 0:
    print(int(moeda20),"x20 cent ", end="");
if moeda10 != 0:
    print(int(moeda10),"x10 cent",end="");
print(".")

