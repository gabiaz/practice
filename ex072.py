t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número entre 0 e 20: '))
while True:
    if 0 <= n <= 20:
        print(f'Você digitou o número {t[n]}.')
        break
    else:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))