litros=float(input("Quantos litros pretede meter de combustivel? "));
print("1) Gasolina 98");
print("2) Gasolina 95");
print("3) Gasoleo");
escolha=int(input("Qual pretende meter? "));
dia=int(input("Em que dia vai abastecer o carro? "));
if (dia<1) and (dia>31):
    print("Dia nao compativel");
elif dia<15:
    if escolha==1:
        apagar=litros*1.414;
        apagar=round(apagar);
        print("Por ",litros," de gasolina98 vai pagar ",apagar);
    elif escolha==2:
        apagar=litros*1.364;
        apagar=round(apagar);
        print("Por ", litros, " de gasolina95 vai pagar ", apagar);
    else:
        apagar = litros * 1.149;
        apagar = round(apagar);
        print("Por ", litros, " de gasoleo vai pagar ", apagar);
else:
    if escolha==1:
        apagar=litros*1.414;
        apagar=round(apagar);
        print("Por ",litros," de gasolina98 vai pagar ",apagar);
    elif escolha==2:
        apagar=litros*1.343;
        apagar=round(apagar);
        print("Por ", litros, " de gasolina95 vai pagar ", apagar);
    else:
        apagar = litros * 1.126;
        apagar = round(apagar);
        print("Por ", litros, " de gasoleo vai pagar ", apagar);