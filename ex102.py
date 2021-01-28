def fatorial(n, show=False):
    """
    --> Calcula o valor do fatorial de um número:
    param n: Número a ser calculado.
    param show: (Opcional) Mostrar o cálculo.
    return: Retorna o resultado do fatorial de um número.
    """
    c = 1
    for v in range(n, 0, -1):
        if show:
            print(f'{v}', end='')
            if v > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        c = c * v
    return c


#Programa principal
print(fatorial(5, show=True))
help(fatorial)