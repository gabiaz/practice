def leiaint(num):
    correto=False
    valor=0
    while True:
        valor=str(input('Digite um número : '))
        if valor.isnumeric():
            correto=True
        else:
            print('\033[0;31m<<< ERRO! Digite um número inteiro válido. >>>\033[m')
        if correto:
            break
    return valor
#Programa principal
n = leiaint('Digite um número : ')
print(f'Você acabou de digitar o número {n}')
