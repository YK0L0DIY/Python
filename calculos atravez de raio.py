def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import math
    
print("Programa de calculo de perimetro, area e volume atravez do raio");
raio=float(input("Indique o raio da esfera ou circulo"));
perimetro=2*math.pi*raio;
area=(math.pi*raio**2)/2;
volume=(4*math.pi*raio**3)/3;
print("Perimetro com " + str(raio) +" de raio, e: " + str(perimetro));
print("Area com " + str(raio) + " de raio, e: " + str(area));
print("Volume da esfera com " + str(raio) + " de raio , e: " + str(volume));	

sys.exit(main(sys.argv))

