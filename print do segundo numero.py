import sys

print("Introduza 3 numeros"); 
num1=float(input("Introduza o 1 numero "));
num2=float(input("Introduza o 2 numero "));
num3=float(input("Introduza o 3 numero "));
if (num1<num2  and num2<num3) or (num3<num2  and num2<num1):
	print("O numero do meio e : " + str(num2));
elif (num1>num2 and num1<num3) or (num1>num3 and num1<num2):
	print("O numero do meio e : " + str(num1));
else:
	print("O numero do meio e : " + str(num3));
