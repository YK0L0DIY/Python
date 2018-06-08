import sys

num1=int(input("Indique um numero de 3 algarismos "));
numt1=int(num1*0.01);
numt2=num1-(int(num1*0.1)*10);
if numt1==numt2:
	print("O numero "+str(num1)+" e capicua.");
else:
	print("O numeor "+str(num1)+" nao e capicua.");
