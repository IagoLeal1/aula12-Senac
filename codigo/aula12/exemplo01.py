import pandas as pd

produtos = ['notebook', 'tablet', 'smartphone', 'smartwatch', 'camera']
quantidade_estoque = [15, 30, 20, 10, 25]

estoque = pd.Series(quantidade_estoque, index=produtos)

print("Série Estoque de Produtos:")
print(estoque)

print("\nQuantidade de Notebooks em estoque:")
print(estoque['notebook'])

print("\nQuantidade de Notebooks e Câmera:")
print(estoque[['notebook', 'camera']].values)

print("\nProdutos em Estoque abaixo de 20 unidades:")
print(estoque[estoque < 20])

print("\nAumentando o estoque em 5 unidades para todos os produtos:")
print(estoque + 5)

estoque.loc['headphone'] = None
print("\nEstoque com um valor nulo (Headphone):")
print(estoque)

precos = pd.Series([1500, 800, 1200, 300, 500], index=produtos)
print("\nSérie Preços dos Produtos:")
print(precos * estoque)