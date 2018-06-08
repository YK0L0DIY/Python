import sys
import math

print("Programa para calcular a raiz quadrada de um numero");
num=float(input("Introduza o numero que pretende calcular a raiz: "));
if num<0:
	print("O valor inroduzido e negativo");
else:
	raiz=math.sqrt(num);
	print("A raiz do numero instroduzido e: " + str(raiz));
