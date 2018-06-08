
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    print("Programa para conversao de usd para euros");
    usd= float(input("Introduza o valor que pretende converter: "));
    eur= usd*0.86;

    print((str(usd)+" usd")+" = "+(str(eur) + " euros"));
    
    sys.exit(main(sys.argv))
