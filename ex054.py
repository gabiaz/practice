from datetime import date
for c in range (1, 8):
    nascimento = int(input('Digite seu ano de nascimento: '))
    atual = nascimento - date.today().year
    menores = 0
    maiores = 0
    if atual - nascimento < 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('Existem {} pessoas maiores de idade e {} menores de idade.'.format(maiores, menores))



