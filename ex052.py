n = int(input('Digite um número inteiro: '))
for c in range (2, n+1):
    if n % (c) != 0:
            r = 'é um número primo'
    else:
            r = 'não é um número primo'
print ('O número {} {}.'.format(n, r))



