m = int(input('Insira m: '))
n = int(input('Insira n: '))

def mdc(m, n):
    if n == m:
        r=n
    if m > n:
        r = mdc(m - n, n)
    if m < n:
        r = mdc(m, n - m)
    return r

print(mdc(m, n))