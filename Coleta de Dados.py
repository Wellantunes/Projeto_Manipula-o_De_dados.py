import pandas as pd

# Carregar o DataFrame
df = pd.read_csv('/data/ecommerce_ex4.csv', encoding='utf-8')

# Converter a coluna 'Desconto' para string
df['Desconto'] = df['Desconto'].astype(str)

# Remover o símbolo '%' e texto 'OFF', mantendo apenas o número
df['Desconto'] = df['Desconto'].apply(lambda x: x.split('%')[0].strip() if '%' in x else x.strip())

# Criar coluna 'Condicao_Atual' pegando a primeira parte da condição (antes do " | ")
df['Condicao_Atual'] = df['Condicao'].apply(lambda x: x.split('|')[0].strip() if pd.notnull(x) else 'Nenhum')

# Criar coluna 'Qtd_Vendidos' pegando a parte após o "|", se existir, senão "Nenhum"
df['Qtd_Vendidos'] = df['Condicao'].apply(
    lambda x: x.split('|')[1].strip().split(' ')[0] if pd.notnull(x) and '|' in x else 'Nenhum'
)

# Exibir o resultado
print(df[['Desconto', 'Condicao_Atual', 'Qtd_Vendidos']].head())