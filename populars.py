import readCsv as l

df_ratings_books = l.df_ratings.merge(l.df_books, on='ISBN')
df_complete = df_ratings_books.merge(l.df_users, on='User-ID')

# número de leituras p/ livro
num_views_df = df_complete.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_views_df.rename(columns={'Book-Rating':'Num_views'},inplace=True)

# número de notas p/ livro
df_complete = df_complete[df_complete['Book-Rating'] >= 1]
num_rating_df = df_complete.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating':'Num_ratings'},inplace=True)

# nota média p/ livro
avg_rating_df = df_complete.groupby('Book-Title').mean(numeric_only=True)['Book-Rating'].reset_index().round(1)
avg_rating_df.rename(columns={'Book-Rating':'Avg_ratings'},inplace=True)

# pegando apenas livros com no mínimo x avaliações e ordenando pela média
popular_df = df_complete.merge(num_views_df, on='Book-Title')
popular_df = popular_df.merge(num_rating_df, on='Book-Title')
popular_df = popular_df.merge(avg_rating_df, on='Book-Title')
popular_df = popular_df.drop(['ISBN', 'Publisher', 'Image-URL-S', 'Image-URL-M', 'User-ID', 'Location', 'Age', 'Book-Rating'], axis=1)
popular_df = popular_df.drop_duplicates('Book-Title')

def populares(quantidade_a_obter = 30, qtd_minima_avaliacoes = 195, filtrar_por='nota', decrescente=False, popular_df = popular_df):

  if filtrar_por == 'nota':
    filtrar_por = 'Avg_ratings'

  elif filtrar_por == 'visualizacoes':
    filtrar_por = 'Num_views'

  elif filtrar_por == 'mais_avaliados':
    filtrar_por = 'Num_ratings'
    
  else:
    filtrar_por = 'Avg_ratings'

  popular_df = popular_df[popular_df['Num_ratings']>=qtd_minima_avaliacoes].sort_values(filtrar_por, ascending=decrescente).head(quantidade_a_obter).reset_index()
  popular_df = popular_df.drop('index', axis=1)
  #populares = popular_df.values.tolist()

  return popular_df # ordem: título, autor(a), ano, img, visualizações, avaliações, nota