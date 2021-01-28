h = a = m = 0
while True:
    i = int(input('Idade: '))
    s = '.'
    while s not in 'MF':
        s = str(input('Sexo: [F/M]: ')).upper().strip()[0]
        continuar = '.'
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar ? [S/N]: ')).upper().strip()[0]
    if i > 18:
        a = a + 1
    if s == 'M':
        h = h + 1
    if s == 'F' and i > 20:
        m = m + 1
    if continuar == 'N':
        break
print(f'O número de pessoas maiores de 18 anos é {a}.')
print(f'O número de homens cadastrados é {h}.')
print(f'O número de mulheres acima de 20 anos é {m}.')