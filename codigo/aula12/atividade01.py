import pandas as pd

livros = ['L.Brasileira', 'L.Estrangeira', 'Ciência', 'Matemática', 'História']
quantidade_estoque = [12, 9, 18, 14, 20]
quantidade_emprestados = [4, 2, 7, 5, 6]

lista_estoque = pd.Series(quantidade_estoque, index=livros)
lista_emprestados = pd.Series(quantidade_emprestados, index=livros)

estoque = lista_estoque - lista_emprestados

estoque.loc['filosofia'] = None

print("\nSérie Estoque de Livros:")
print(estoque)

print("\nProdutos em Estoque acima de 5 unidades:")
print(estoque[estoque > 5])

