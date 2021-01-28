def LeiaInt(num):
    while True:
        correto = False
        valor = 0
        try:
            valor=int(input(num))
        except Exception as erro:
            print('\033[0:31mOps! Ocorreu um erro!\033[m')
        else:
            correto=True
            return valor
        if correto:
            break

def LeiaFloat(num):
    correto=False
    resp=0
    while True:
        try:
            resp =float(input(num))
        except Exception as erro:
            print('\033[0:31mOps! Ocorreu um erro!\033[m')
        else:
            correto=True
            return resp
        if correto:
            break


#Programa principal
n = LeiaInt('Digite um número inteiro : ')
n2 = LeiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {n2}')