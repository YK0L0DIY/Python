num=int(input("Indique um numero para calcular fatorial: "));
fatorial=1;
cal=num;
if num<0:
    print("valor negativo");
else:
    while num>1:
        fatorial=fatorial*num;
        num=num-1;

print("O fatorial de ",cal," e: ",fatorial);