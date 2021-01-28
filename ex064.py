n = 0
s = 0
cont = 0
while n != 999:
    n = int(input('Digite um número inteiro [999 para parar]: '))
    s = s + n
    cont = cont + 1
print('Você digitou {} números e a soma deles é {} .'.format(cont - 1, s - 999))

