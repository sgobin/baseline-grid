# Carregar os dados
print('')
print('')
print('SGOBIN Studio Grid Calculator')
print('-' * 30)

rows = int(input("Número de fileiras: "))
leading = float(input("Leading em pontos: "))
hPapel = float(input('Altura do papel em pol: '))

# Converter unidades

#Calcula tamanho do papel em pontos
def convAltura(h):
    return h*72



# Calcular frame
def calculaFrame(r,ld,f):
    #Cabeçalho
    print('')
    print('Tamanho de Frame para %s rows e %spt leading' % (rows, leading))
    print('-' * 60)

    i = 1
    while True:
        tamFrame = ((r*i)+(r-1))*ld
        margens = (f - tamFrame)/2 #calcula margens restantes
        margensMM = round(margens*0.3528, 3) #Converte as margens de pts para mm

        if tamFrame < hPapelPt:
            print(' %s linha/row = %spt e margens de %spt (%smm)' % (i, tamFrame, margens, margensMM))
            i += 1
        else:
            break
    print('-' * 60)
    print('')

#Inicio
hPapelPt = convAltura(hPapel)
calculaFrame(rows,leading,hPapelPt)
