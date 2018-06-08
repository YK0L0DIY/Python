def pascal(lin, col):
    if col == 0 or col == lin:
        return 1
    else:
        f = pascal(lin - 1, col - 1) + pascal(lin - 1, col)
        return f
a=0
n=int(input("Indique o numero que linhas do triangulo de pascal: "))
while n!=a:
    b=0
    k=""
    while b<=a:
        k=str(k)+str(" ")+str(pascal(a,b))
        b=b+1
    print(k)
    a=a+1