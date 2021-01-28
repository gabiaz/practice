def situação(num):
    from datetime import date
    atual= date.today().year
    idade = atual - ano
    if idade<16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 18>idade>16 or idade>65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


#Programa Principal
ano=int(input('Em que ano você nasceu? : '))
print(situação(ano))
