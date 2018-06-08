import sys
 
print("Introduza 2 numeros inteiros para identificar se um e multiplo de outro");
num1=int(input("numero 1: "));
num2=int(input("numero 2: "));
if num1%num2==0:
	print("Numero 1 e multiplo do numero 2");
elif num2%num1==0:
	print("Numero 2 e multiplo do numero 1");
else:
	print ("Os numeros nao sao multiplos um do outro");
