#pede numero de rows e leading desejado
rows = int(input("Quantas rows: "))
leading = float(input("Leading em pontos: "))
alturaPapel = float(input('Altura do papel em pol: '))

#Calcula tamanho do papel em pontos
def convAltura(h):
    return h*72

#Calcula tamanho total do frame baseado em linhas de texto por row
def calculaFrame(r,ld,f):
    i = 1
    #Cabeçalho
    print('')
    print('Tamanho de Frame para %s rows e %spt leading' % (rows, leading))
    print('-' * 45)

    #Loop com as fileiras
    for i in range(1,12):
        tamFrame = ((r*i)+(r-1))*ld
        margens = (f - tamFrame)/2 #calcula margens restantes
        margensMM = round(margens*0.3528, 3) #Converte as margens de pts para mm

        if i < 10:
            print(' %s linha/row = %spt e margens de %spt (%smm)' % (i, tamFrame, margens, margensMM))
        else:
            print('%s linha/row = %spt e margens de %spt (%smm)' % (i, tamFrame, margens, margensMM))
    print('')

folha = convAltura(alturaPapel)

calculaFrame(rows,leading,folha)
