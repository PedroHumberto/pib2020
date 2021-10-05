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


def pais_escolhido(pais,ano):
    rotulos, dados = extrair_dados('pibs.csv')
    
    try:
        indice_ano = rotulos.index(ano)
    except ValueError:
        return print('Ano não disponível.')

    for elemento in dados:
        
        if (elemento[0]) == pais:                
            indice_do_pais = float(elemento[indice_ano])
            return print(f'PIB {pais} em {ano}: US${indice_do_pais} trilhões.')
            
    else:
        return print("País não disponível.")



    
     



pais = input('Informe um país: ')
ano = input('Informe um ano entre 2013 e 2020: ')


pais_escolhido(pais,ano)




    


