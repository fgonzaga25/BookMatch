import numpy as np
import pandas as pd
import readCsv as r
import json

org_matrix = pd.read_csv("data/matrix.csv", index_col=0)
org_df_similarity_scores = pd.read_csv('data/similarity_scores.csv')

matrix = org_matrix.copy()
df_similarity_scores = org_df_similarity_scores.copy()

similarity_scores = df_similarity_scores.to_numpy()

def recomendar(nome_livro, qtd_recomendacoes=3):
  index = np.where(matrix.index == nome_livro)[0][0]
  livros_similares = sorted(list(enumerate(similarity_scores[index])), key = lambda x:x[1], reverse = True)[1:qtd_recomendacoes+1]
	
  dados = []

  for i in livros_similares:
    obj = []
    linha_livro = r.df_books[r.df_books['Book-Title'] == matrix.index[i[0]]]
    obj.extend(list(linha_livro.drop_duplicates('Book-Title')['Book-Title'].values))
    obj.extend(list(linha_livro.drop_duplicates('Book-Title')['Book-Author'].values))
    obj.extend(list(linha_livro.drop_duplicates('Book-Title')['Year-Of-Publication'].values))
    obj.extend(list(linha_livro.drop_duplicates('Book-Title')['Image-URL-L'].values))
    
    dados.append(obj)
  
  # df_dados = pd.DataFrame(dados, columns=['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Image-URL-L'])
  return json.dumps(dados) # ordem: título, autor(a), ano, img