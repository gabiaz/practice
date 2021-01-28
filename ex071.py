n = int(input('Quantos reais você deseja sacar ? '))
total = n
céd = 50
totced = 0
while True:
    if total >= céd:
        total = total - céd
        totced = totced + 1
    else:
        if totced > 0:
            print(f'Receber {totced} de {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20 :
            céd = 10
        elif céd == 10:
            céd = 1
        totced = 0
        if total == 0:
            break