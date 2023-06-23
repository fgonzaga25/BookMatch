import readCsv as r
import pandas as pd
import os
from sklearn.metrics.pairwise import cosine_similarity

ratings_with_name = r.df_ratings.merge(r.df_books, on = 'ISBN')
u = ratings_with_name.groupby('User-ID').count()['Book-Rating'] >= 200
regular_voters_id = u[u].index
filtered_rating = ratings_with_name[ratings_with_name['User-ID'].isin(regular_voters_id)]
m = ratings_with_name.groupby('Book-Title').count()['Book-Rating'] >= 100
relevant_books = m[m].index
final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(relevant_books)]
matrix = final_ratings.pivot_table(index = 'Book-Title', columns = 'User-ID', values =  'Book-Rating')
matrix.fillna(0, inplace = True)
similarity_scores = cosine_similarity(matrix)

df_matrix = pd.DataFrame(matrix)
df_similarity_scores = pd.DataFrame(similarity_scores)

path = os.path.expanduser("data")

df_matrix.to_csv(os.path.join(path, "matrix.csv"), index=True)
df_similarity_scores.to_csv(os.path.join(path, "similarity_scores.csv"), index=False)