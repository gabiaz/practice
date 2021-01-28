n = str(input('Qual o seu sexo (F/M)? ')).strip().upper()[0]
while n not in 'FfMm':
    print('Digite F para feminino e M para masculino')
    n = str(input('Digite novamente o sexo: '))
