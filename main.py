import svd
import cf_knn
import pandas as pd
import numpy as np
from user_dataframe import ratings, user_movie_matrix, movies

userId = 3

print("USERS TOP MOVIES:")
user_ratings = user_movie_matrix.iloc[userId - 1]
top_user_ratings = user_ratings.sort_values(ascending=False).to_frame()
print(pd.merge(top_user_ratings, movies, on='movieId').head(10).to_string())

svd.recommend(userId)
# cf_knn.recommend(userId)