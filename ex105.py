def notas(*n, situação=False):
    r = dict()
    r['TOTAL']=len(n)
    r['MAIOR']=max(n)
    r['MENOR']=min(n)
    r['MÉDIA']=sum(n)/len(n)
    if situação:
        if r['MÉDIA']>=7:
            r['SITUAÇÃO']='BOA'
        elif r['MÉDIA']>= 6:
            r['SITUAÇÃO']='RAZOÁVEL'
        else:
            r['SITUAÇÃO']='RUIM'
    return r


#Programa principal
resp = notas(5.5, 9.5, 10, 6.5, situação=True)
print(resp)