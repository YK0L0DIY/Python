import sys

alt=float(input("Introduza a altura de uma pessoa em metros: "));
if alt<1.3:
	print("A pessoa e baixissima");
elif alt>= 1.3 and alt<1.6:
	print("A pessoa e baixa");
elif alt>= 1.6 and alt<1.75:
	print("A pessoa e media");
elif alt>=1.75 and alt<1.9:
	print("A pessoa e alta");
else:
	print("A pessoa e altissima");
