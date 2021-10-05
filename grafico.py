import matplotlib.pyplot as plt
def extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo: 
        conteudo = arquivo.read()


    conteudo = conteudo.splitlines()
    rotulos = conteudo[0]
    conteudo = conteudo[1:]

    rotulos = rotulos.split(',')
    dados = []
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)

    return rotulos, dados

def viaracao_pib():
    rotulos, dados = extrair_dados('pibs.csv')
    indice_pais = rotulos.index('País')
    indice_inicial = rotulos.index('2013')
    indice_final = rotulos.index('2020')

    for elemento in dados:
        paises = elemento[indice_pais]
        pibinicial = float(elemento[indice_inicial])
        pibfinal = float(elemento[indice_final])
        pib = ((pibfinal/pibinicial) - 1) * 100 


        print(f'{paises: <25}Variação de {pib:.2f}% entre 2013 e 2020.')

def exibir_grafico(x, y, paisescolhido):
    plt.plot(x,y)
    plt.title(f'PIB: {paisescolhido} 2013 a 2020')
    plt.show()


def exibir_grafico_evolucao_pib(paisescolhido):
    rotulos, dados = extrair_dados('pibs.csv')
    
    indice_pais = rotulos.index('País')
    

    lista_anos = []     # eixo x do gráfico
    lista_pib = []     # eixo y do gráfico
    for anos in rotulos:
        lista_anos.append(anos)
    lista_anos.remove('País') #remove string 'País'

    # Criei uma lista nova apos remover item string e atualizar todos os outros para numeros inteiros e floats
    lista_anosnovo = []
    for ano in lista_anos:
        lista_anosnovo.append(int(ano))

    for elemento in dados:
        if (elemento[indice_pais]) == paisescolhido:
            lista_pib = elemento
    lista_pib.remove(paisescolhido) #Remove os nomes dos paises, transformando tudo em string

    lista_pibnovo = []
    for pib in lista_pib:
        lista_pibnovo.append(float(pib))   

    return exibir_grafico(lista_anosnovo, lista_pibnovo, paisescolhido)
viaracao_pib()

paisescolhido = input('Informe um país: ')

exibir_grafico_evolucao_pib(paisescolhido)





    


