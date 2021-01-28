frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
letras = ''.join(palavras)
inverso = letras[::-1]
if letras == inverso:
    print('Temos um polímedro')
else:
    print('não')


