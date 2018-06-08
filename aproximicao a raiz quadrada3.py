import math
num=float(input("Indique o numero que pretende calcular a raiz quadrada: "));
est=float(input("Introduza a estimatova: "));
paragem=0.0001;
while paragem<1:
    y=(est+num/est)/2;
    print(y);
    if abs(est-y)<paragem:
        break
    est=y;
print("A aproximacao e: ",est," o valor exato e :", math.sqrt(num));