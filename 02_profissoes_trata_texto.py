import pandas as pd

linhas_limpas = []

# Caminho do arquivo CBO2002_LISTA.txt
caminho_arquivo = 'out/CBO2002_LISTA.txt'

# Abrir o arquivo e ler as linhas
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    # Ignorar as X primeiras linhas do arquivo
    for _ in range(5):
        next(arquivo)

    # Filtrar apenas as linhas que não contêm 'CBO2002'
    linhas_filtradas = [linha.strip().split(' ', 2) for linha in arquivo if 'CBO2002' not in linha]

# Adicionar as linhas filtradas à lista linhas_limpas
linhas_limpas.extend(linhas_filtradas)

# Converter a lista para um DataFrame
df = pd.DataFrame(linhas_limpas, columns=['Tipo', 'Código', 'Descrição'])

# Filtrar o DataFrame para incluir apenas linhas que contêm 'Família'
# df_familia = df[df['Tipo'] == 'Família']

# Somente ocupações e sinonimos
df_validos = df.loc[df['Tipo'].str.startswith('Ocupação') | df['Tipo'].str.startswith('Sinônimo')]

# Usar .loc para evitar o SettingWithCopyWarning
df_validos.loc[:, 'Descrição'] = df_validos['Descrição'].str.replace("'", "")

# Filtrar o DataFrame para incluir apenas linhas que começam com 'Ocupação'
# df_ocupacao = df[df['Tipo'].str.startswith('Ocupação')]

# Obter os tipos únicos na coluna 'Tipo'
# tipos_unicos = df['Tipo'].unique()

# Mostrar os tipos únicos
print(df_validos.head())
# print(tipos_unicos)
# print(df_ocupacao.head())
# print(df_familia.head())
# print(df.head())

# Salvar o DataFrame em um arquivo CSV sem cabeçalho e sem índice
df_validos.to_csv('out/profissoes.csv', header=False, index=False)

# criar o arquivo txt com o seguinte formato '(tipo,codigo,descricao),'
with open('out/profissoes.txt', 'w', encoding='utf8') as arquivo:
    for linha in df_validos.itertuples(index=False):
        arquivo.write(f"('{linha.Tipo}','{linha.Código}','{linha.Descrição}'),\n")

# fechar o arquivo
arquivo.close()