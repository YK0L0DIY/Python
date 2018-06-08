st=input("Frase: ")
st=st.lower()
n=len(st)
a=0
k="#"
while n!= a:
    if st[a]==" ":
        k=str(k)+str(" #")
        a=a+1
    elif st[a]=="a"or"b"or"c"or"d"or"e"or"f"or"g"or"h"or"i"or"j"or"k"or"l"or"m"or"n"or"o"or"p"or"q"or"r"or"s"or"t"or"u"or"v"or"w"or"z"or"y"or"x":
        k=str(k)+str(st[a])
        a=a+1
    else:
        a=a+1
