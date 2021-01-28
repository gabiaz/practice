preço = total = mil = menor = cont = 0
baratero = '.'
while True:
    nome = str(input('Nome do produto: '))
    preço = int(input('Preço: '))
    total = total + preço
    cont =+ 1
    if preço > 1000:
        mil = mil + 1
    if cont == 1 or preço < menor:
        menor = preço
        baratero = nome
    continuar = '.'
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':
        break
print(f'O valor total da compra foi {total}, e {mil} produtos custaram mais de mil reais. O produto de menor valor foi {baratero}')
