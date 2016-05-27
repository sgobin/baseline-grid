#Calculadora de Grid
Uma calculadora em Python 3 que usa a linha de base (baseline), o números de fileiras (rows) desejados e o tamanho da página, para gerar opções de linhas de texto/fileiras e as respectivas margens.

### Exemplo
```

SGOBIN Studio Grid Calculator
------------------------------
Número de fileiras: 12
Leading em pontos: 14
Escolha a unidade (1 para polegadas ou 2 para milímetros): 2
Altura do papel em milímetros: 297

Tamanho de Frame para 12 rows e 14.0pt leading
------------------------------------------------------------
 1 linha/row = 322.0pt e margens de 259.946pt (91.709mm)
 2 linha/row = 490.0pt e margens de 175.946pt (62.074mm)
 3 linha/row = 658.0pt e margens de 91.946pt (32.439mm)
 4 linha/row = 826.0pt e margens de 7.946pt (2.803mm)
------------------------------------------------------------

```

Usando a opção 3 para gerar as guias no Indesgin como exemplo:

![Grid](http://i.imgur.com/3qR7cOg.png)


##todo
- ~~Calcular somente quando a margem for positiva~~
- ~~Adicionar opção de unidade (milímetros ou polegadas)~~
- Tratar entrada da unidade
- Guardar os dados em um arquivo
