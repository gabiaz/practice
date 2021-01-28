from time import sleep
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Qual a razão? '))
print('Calculando os 10 primeiros termos: ')
sleep(1)
termo = primeiro_termo
cont = 1
décimo_termo = primeiro_termo + 9 * razão
n = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        termo = termo + razão
        cont = cont + 1
        print('{}'.format(termo), end=' ')
    print('.')
    mais = int(input('Deseja ver mais quantos termos?'))

