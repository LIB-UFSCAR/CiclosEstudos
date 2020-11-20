# Seu objetivo é remover as colunas vazias do arquivo metadados.csv
# Porém, você só pode editar o arquivo usando esse script
# Para isso, você deve alterar a lista dados
# Nela, cada linha do arquivo está contida em uma string

with open('metadados.csv', mode='r') as arquivo:
    dados = arquivo.readlines()

# Remove a última linha (em branco)
dados.pop()

# Converter cada linha de str para list
dados_brutos = []
for linha_str in dados:
    linha_list = linha_str.split(",")
    dados_brutos.append(linha_list)

# Começar todas as colunas como False
coluna_com_dados = []
for cabecalho in dados_brutos[0]:
    coluna_com_dados.append(False)


# Percorrer cada uma das linhas de dados
# Pulando a linha do cabeçalho!
for linha in dados_brutos[1:]:
    # Em cada linha, percorrer os valores
    # Se encontrar algo (não estiver vazio)
    # Mudar o status da coluna para True
    for index, valor in enumerate(linha):
        if valor != "":
            coluna_com_dados[index] = True


# Percorre os dados brutos
dados_limpos = []
for linha in dados_brutos:
    # Inicia a linha como uma lista
    linha_limpa = []

    # Percorre as colunas de status
    # Adiciona dados apenas se tiver algo na coluna
    for index, tem_dados in enumerate(coluna_com_dados):
        if tem_dados == True:
            linha_limpa.append(linha[index])

    # Converte as linhas em str de novo
    linha_str = ",".join(linha_limpa)
    dados_limpos.append(linha_str)

# Por fim, falamos que os dados são os dados_limpos
dados = dados_limpos

with open('metadados_limpos.csv', mode='w+') as arquivo:
    conteudo = "".join(dados)
    arquivo.write(conteudo)
