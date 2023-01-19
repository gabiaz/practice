from random import randint
from time import sleep
print('SORTEANDO 5 NÚMEROS...')
sleep(1.5)
def sorteio(list):
    print('-='*15)
    print('Os números sorteados foram : ', end='')
    for c in range(0,5):
        n = randint(0, 10)
        list.append(n)
        print(n, end=' ', flush=True)
        sleep(0.5)
    print('!')
    print('-='*15)
def somapar(list):
    soma=0
    for c in list:
        if c %2==0:
            soma=soma+c
    print(f'A soma dos números pares é {soma}')


list=[]
sorteio(list)
somapar(list)
