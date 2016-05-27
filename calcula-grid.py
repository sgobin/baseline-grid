#Global Vars
hPapelPt = 1.0

# Carregar os dados
print('')
print('')
print('SGOBIN Studio Grid Calculator')
print('-' * 30)

rows = int(input("Número de fileiras: "))
leading = float(input("Leading em pontos: "))

unidade = input('Escolha a unidade (1 para polegadas ou 2 para milímetros): ')

if unidade == '1':
    hPapel = float(input('Altura do papel em polegadas: '))
elif unidade== '2':
    hPapel = float(input('Altura do papel em milímetros: '))
else:
    print('Unidade não definida')

# Converter unidades

#Calcula tamanho do papel em pontos
def convPolToPoints(h):
    return h*72

def convMMToPoints(h):
    return h*2.83465

# Calcular frame
def calculaFrame(r,ld,f):
    #Cabeçalho
    print('')
    print('Tamanho de Frame para %s rows e %spt leading' % (rows, leading))
    print('-' * 60)

    i = 1
    while True:
        tamFrame = ((r*i)+(r-1))*ld
        margens = round((f - tamFrame)/2, 3) #calcula margens restantes
        margensMM = round(margens*0.3528, 3) #Converte as margens de pts para mm

        if tamFrame < hPapelPt:
            print(' %s linha/row = %spt e margens de %spt (%smm)' % (i, tamFrame, margens, margensMM))
            i += 1
        else:
            break
    print('-' * 60)
    print('')

#Inicio
if unidade == '1':
    hPapelPt = convPolToPoints(hPapel)
elif unidade == '2':
    hPapelPt = convMMToPoints(hPapel)


calculaFrame(rows,leading,hPapelPt)
