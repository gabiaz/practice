maior = 0
somamulher = 0
novo = 0
for pessoa in range (1, 6):
    from statistics import median
    nome = str(input('Qual o nome? '))
    idade = int(input('Qual é a idade ? '))
    sexo = str(input('Qual o sexo [F/M] ? '))
    if sexo == 'M' and pessoa == 1:
        novo = nome
        maior = idade
    if sexo == 'M' and idade > maior:
        novo = nome
        maior = idade
    if sexo == 'F' and idade < 20:
        somamulher = somamulher + 1

print('O nome do homem mais velho é {}.'.format(novo))
print('{} mulheres possuem menos de 20 anos'.format(somamulher))

