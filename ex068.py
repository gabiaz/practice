from random import randint
s = 0
while True:
    n = int(input('Digite um número: '))
    c = randint(0, 10)
    total = c + n
    t = 'a'
    while t not in 'PpIi':
        t = str(input('Par ou ímpar? [P/I] : ')).lower().strip()[0]
    if t == 'p':
        if total % 2 == 0:
            print (f'Parabéns! O computador escolheu {c} e você {n} . Você ganhou!')
            s = s + 1
        else:
            print('Você perdeu')
            break
    elif t == 'i':
        if total % 2 != 0:
            print(f'Parbéns! O computador escolheu {c} e você {n} . Você ganhou!')
            s = s + 1
        else:
            print('Você perdeu')
            break
print(f'Você ganhou {s} vezes e agora perdeu. game over..')