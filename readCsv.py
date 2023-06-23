import numpy as np
import pandas as pd

#lendo os datasets
org_df_books=pd.read_csv("data/Books.csv", low_memory=False)
org_df_ratings=pd.read_csv("data/Ratings.csv")
org_df_users=pd.read_csv("data/Users.csv")

#fazendo uma cópia
df_books = org_df_books.copy()
df_ratings = org_df_ratings.copy()
df_users = org_df_users.copy()