c = 0
while True:
    n = int(input('Digite um número inteiro: '))
    if n < 0 :
        break
    while c < 10:
        c = c + 1
        print (f'{n} X {c} = {n*c}')
print('Programa encerrado')