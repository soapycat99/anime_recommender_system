import numpy as np
import pandas as pd
import warnings
import scipy as sp
from sklearn.metrics.pairwise import cosine_similarity
import pickle

#default theme and settings

#warning hadle
warnings.filterwarnings("always")
warnings.filterwarnings("ignore")

anime_path = 'anime.csv'
rating_path = 'rating.csv'

anime_df = pd.read_csv(anime_path)
rating_df = pd.read_csv(rating_path)

# deleting anime with 0 rating
anime_df=anime_df[~np.isnan(anime_df["rating"])]

# filling mode value for genre and type
anime_df['genre'] = anime_df['genre'].fillna(
anime_df['genre'].dropna().mode().values[0])

anime_df['type'] = anime_df['type'].fillna(
anime_df['type'].dropna().mode().values[0])

#Filling NaN value
rating_df['rating'] = rating_df['rating'].apply(lambda x: np.nan if x==-1 else x)

#Series only -> TV type
anime_df = anime_df[anime_df['type']=='TV']

#Merge anime and rating df
rated_anime = rating_df.merge(anime_df, left_on = 'anime_id', right_on = 'anime_id', suffixes= ['_user', ''])
rated_anime =rated_anime[['user_id', 'name', 'rating']]
rated_anime_7500= rated_anime[rated_anime.user_id <= 7500]

#Pivot table for similarity
pivot = rated_anime_7500.pivot_table(index=['user_id'], columns=['name'], values='rating')


#Normalization and fill NaN value
pivot_n = pivot.apply(lambda x: (x-np.mean(x))/(np.max(x)-np.min(x)), axis=1)
pivot_n.fillna(0, inplace=True)

#Transpose, drop columns where value = 0, convert to sparse matrix
pivot_n = pivot_n.T
pivot_n = pivot_n.loc[:, (pivot_n != 0).any(axis=0)]
piv_sparse = sp.sparse.csr_matrix(pivot_n.values)

#model based on anime similarity
anime_similarity = cosine_similarity(piv_sparse)

#Df of anime similarities
ani_sim_df = pd.DataFrame(anime_similarity, index = pivot_n.index, columns = pivot_n.index)


ani_sim_df.to_pickle('anime_sim_df.pkl')


def anime_recommendation(ani_name):

    number = 1
    print('Recommended because you watched {}:\n'.format(ani_name))
    for anime in ani_sim_df.sort_values(by=ani_name, ascending=False).index[1:6]:
        print(f'#{number}: {anime}, {round(ani_sim_df[anime][ani_name] * 100, 2)}% match')
        number += 1







# ani_list = anime_rec_list('Naruto')
# for ani in ani_list:
#     print(ani)
