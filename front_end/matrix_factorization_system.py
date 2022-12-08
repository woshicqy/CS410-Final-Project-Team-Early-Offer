# -*- coding: utf-8 -*-
"""matrix_factorization.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oINK21dyfwZk1sMKKejcOGksP6WLyXim
"""

# !pip install scikit-surprise

import random
import numpy as np
import pandas as pd
from surprise import Reader, Dataset, SVD
from surprise.model_selection import cross_validate, GridSearchCV, train_test_split

random.seed("CS410")

# Read in data
movie_credits = pd.read_csv('dataset/tmdb_5000_credits.csv')
movies = pd.read_csv('dataset/tmdb_5000_movies.csv')
# print(df2.head(3)) # 20 columns
movie_data = movies.rename(columns={'id': 'movie_id'})
movie_data = movie_data.merge(movie_credits, on='movie_id')  # 20 columns -> 23 columns
movie_data['user_id'] = np.random.randint(1, 100, movie_data.shape[0])  # 100 random user id for rating

reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(movie_data[["user_id", "movie_id", "vote_average"]], reader)

algo = SVD(n_epochs=10)
results = cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=10, verbose=True)

# print("Average MAE: ", np.average(results["test_mae"]))
# print("Average RMSE: ", np.average(results["test_rmse"]))

# # Grid-Search for best params
# param_grid = {
#   'n_factors': [20, 50, 100, 200, 500],
#   'n_epochs': [5, 10, 20, 50]
# }

# gs = GridSearchCV(SVD, param_grid, measures=['rmse', 'mae'], cv=10)
# gs.fit(data)

# print(gs.best_score['rmse'])
# print(gs.best_params['rmse'])

# build svd model
# best_factor = gs.best_params['rmse']['n_factors'] # 500
# best_epoch = gs.best_params['rmse']['n_epochs'] # 5

trainset = data.build_full_trainset()
svd = SVD(n_factors=500, n_epochs=5, lr_all=0.005, reg_all=0.02, init_std_dev=0.05)
svd.fit(trainset)


def get_user_info(user_id):
    """ Get user info
    ### Input: user id
    ### Return: a list of movie that user watched [[movie name, user rating]]"""
    print(type(user_id))
    user_movie = movie_data.loc[movie_data["user_id"] == user_id][["original_title", "vote_average"]]
    user_movie = user_movie.values.tolist()
    return user_movie


def recommend_movie(user_id, n_items=10):
    """ Generate recommendations
    ### Input: user id, number of recommendations default 10
    ### Return: a list of movie recommended to the user, based on his rating.
    ### [[movie name, recommendation rating]]"""
    movie_ids = movie_data["movie_id"].unique()
    movie_pred = movie_data.loc[movie_data["user_id"] != user_id]["movie_id"]

    testset = []
    for id in movie_pred:
        testset.append([user_id, id, 5])

    # prediction and recommendation
    pred = svd.test(testset)

    ratings = []
    for p in pred:
        ratings.append(p.est)
    ratings = np.array(ratings)

    # rank top n
    max_ind = (-ratings).argsort()[:n_items]
    recommend_list = []
    for i in max_ind:
        movie_id = movie_pred[i]
        recommend_list.append(
            [movie_data[movie_data["movie_id"] == movie_id]["original_title"].values[0], np.round(ratings[i], 2)])

    return recommend_list

if __name__ == '__main__':
    recommend_list = recommend_movie(16)
    for movie_name, rating in recommend_list:
        print(movie_name, rating)