r = 's'
n = cont = soma = maior = menor = 0
while r == 's':
    n = int(input('Digite um número: '))
    r = str(input('Deseja digitar mais um número? [s/n] : ' )).lower().strip() [0]
    cont += 1
    soma += n
    média = soma/cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print ('A média entre os {} números é {}'.format(cont, média))
print ( 'O maior número é {} e o menor {} .'.format(maior, menor))
