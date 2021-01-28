def ficha(jogador, gols):

    print(f'E jogadore {jogador} fez {gols} gol(s) no campeonato.')


#Programa principal
j=str(input('Nome do jogador : '))
if j.strip()=='':
    j='< desconhecido >'
n=str(input('Número de gols : '))
if n.isnumeric():
    n=int(n)
    ficha(jogador=j, gols=n)
else:
    if n.strip()=='':
        ficha(jogador=j, gols=0)
