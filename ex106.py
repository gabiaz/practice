def ajuda(msg):
    help(msg)

#Programa principal
while True:

    comando=str(input('Função ou biblioteca > '))
    if comando.upper()=='FIM':
        break
    else:
        r=ajuda(comando)
