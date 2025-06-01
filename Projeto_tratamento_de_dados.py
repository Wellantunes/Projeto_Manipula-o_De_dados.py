import requests
from bs4 import BeautifulSoup
import pandas as pd
requests.packages.urllib3.disable_warnings()

url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

extracao = BeautifulSoup(requisicao.text, 'html.parser')

contar_livros = 0
catalogo = []
requisicao.encoding = 'utf-8'

def truncar_titulo(titulo):
    palavras = titulo.split()
    if len(palavras) <= 4:
        return titulo
    return " ".join(palavras[:4]) + " ..."

for artigo in extracao.find_all('article', class_='product_pod'):
    livro = {}

    h3 = artigo.find('h3')
    a = h3.find('a')
    titulo_completo = a['title'].strip() if a and a.has_attr('title') else 'Título não encontrado'
    titulo = truncar_titulo(titulo_completo)
    livro['Título'] = titulo

    preco_tag = artigo.find('p', class_='price_color')
    preco = preco_tag.get_text(strip=True) if preco_tag else 'Preço não encontrado'
    livro['Preço'] = preco

    catalogo.append(livro)
    contar_livros += 1


for livro in catalogo:
    print(f"{livro['Título']} - {livro['Preço']}")

print("contar_livros =", contar_livros)