




import os
import ast
import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics.pairwise import cosine_similarity


# In[2]:


import pandas as pd
import numpy as np
import ast


credits=pd.read_csv("credits.csv")
def extract_actors(obj):
    L=[]
    count=0
    for a in ast.literal_eval(obj):
        if count!=3:
            L.append(a["name"])
            count+=1
        else:
            break
    return L
credits["cast"]=credits["cast"].apply(extract_actors)
def extract_directer(obj):
    for a in ast.literal_eval(obj):
        if a["job"]=="Director":
            return a["name"]
credits["directer"]=credits["crew"].apply(extract_directer)
credits





credits["cast"]=credits["cast"].apply(lambda x:[a.replace(" ","") for a in x])
credits["cast"]=credits["cast"].apply(lambda x:[a.lower() for a in x])
credits["directer"]=credits["directer"].astype(str)
credits["directer"]=credits["directer"].apply(lambda x:x.lower())
credits["directer"]=credits["directer"].apply(lambda x:x.replace(" ",""))
credits=credits[["id","cast","directer"]]
credits





keywords=pd.read_csv("keywords.csv")
def extracter(obj):
    L=[]
    for a in ast.literal_eval(obj):
        L.append(a['name'])
    return L
keywords["keywords"]=keywords["keywords"].apply(extracter)
keywords=credits.merge(keywords,on="id")
keywords





movies=pd.read_csv("movies_metadata.csv")
movies=movies[["id","original_title","overview","genres","original_language","popularity",
               "vote_average","vote_count","belongs_to_collection","release_date","title"]]
movies["belongs_to_collection"]





movies["genres"]=movies["genres"].apply(extracter)
movies["genres"]=movies["genres"].apply(lambda x:[a.lower() for a in x])
#print(movies["id"].index[movies["id"]=="2014-01-01"].tolist())
movies=movies.drop(35587)
#print(movies["id"].index[movies["id"]=="1997-08-20"].tolist())
movies=movies.drop(19730)
#print(movies["id"].index[movies["id"]=="2012-09-29"].tolist())
movies=movies.drop(29503)
movies["id"]=movies["id"].astype(int)
movies=movies.merge(keywords,on="id")

movies["overview"]=movies["overview"].astype(str)
movies["overview"]=movies["overview"].apply(lambda x:x.split())
movies["overview"]=movies["overview"].apply(lambda x:[a.lower() for a in x])



movies["original_title"]=movies["original_title"].astype(str)
movies["original_title"]=movies["original_title"].apply(lambda x:x.replace(" ",""))
movies["original_title"]=movies["original_title"].apply(lambda x:x.lower())



import json
def extract_name(str):
    try:
        dict = json.loads(str.replace("'", '"'))
        return dict.get('name', 'No Name')
    except (json.JSONDecodeError, AttributeError):
        return ''
movies['belongs_to_collection'] = movies['belongs_to_collection'].apply(extract_name)
movies['belongs_to_collection']=movies['belongs_to_collection'].apply(lambda x:x.replace(" ",""))
movies['belongs_to_collection']=movies['belongs_to_collection'].apply(lambda x:x.lower())





movies





movies["tags"]=movies["genres"]+movies["cast"]+movies["overview"]+movies["keywords"]
titles_to_delete=["Luv","Sur","Lilla Jönssonligan på styva linan"]
movies=movies[~movies['title'].isin(titles_to_delete)]
movies


# In[9]:


content=movies[["id","original_title","belongs_to_collection","tags","directer"]]
content["tags"]=content["tags"].apply(lambda x:" ".join(x))
#content["tags"]=content["tags"].apply(lambda x:x.replace(" ,"," "))
# content["tags"]=content["tags"].apply(lambda x:x.lower())
content=content[:42500]
# for x in content["overview"]:
#     print(type(x))
content["tags"]=content["original_title"]+" "+content["belongs_to_collection"]+" "+content["directer"]+" "+content["tags"]
content.loc[0]


# In[10]:


'''from sklearn.feature_extraction.text import CountVectorizer
count_vectorizer = CountVectorizer(max_features=10000,stop_words="english")
count_matrix = count_vectorizer.fit_transform(content["tags"])
count_array = count_matrix.toarray()
feature_names = count_vectorizer.get_feature_names_out()
count_df = pd.DataFrame(count_array, columns=feature_names)
print(count_df)'''




from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=10000,stop_words="english")
tfidf_matrix = tfidf_vectorizer.fit_transform(content["tags"])
tfidf_array = tfidf_matrix.toarray()
feature_names = tfidf_vectorizer.get_feature_names_out()
tfidf_df = pd.DataFrame(tfidf_array, columns=feature_names)
print(tfidf_matrix.shape)


ids=movies[["id"]][:42500]
tfidf_df=ids.merge(tfidf_df,left_index=True, right_index=True)
# tfids_df=tfidf_df.set_index(ids)
tfidf_df


# In[11]:


def centroid(obj):
    title_to_id=dict(zip(movies['original_title'], movies["id"]))
    ids=[title_to_id[title] for title in obj]
    centroid=tfidf_df.loc[tfidf_df['id'].isin(ids)].mean()
    return centroid
    
L=["ironman","ironman2"]
centroid_vector=centroid(L)
centroid_vector
centroid_vector=pd.DataFrame([centroid_vector], columns=tfidf_df.columns)
tfidf_df=pd.concat([tfidf_df,centroid_vector], ignore_index=True)
tfidf_df


# In[12]:


from sklearn.metrics.pairwise import euclidean_distances
query_vector = tfidf_df.iloc[-1, 1:].values.reshape(1, -1)
other_vectors = tfidf_df.iloc[:-1, 1:].values
distances = euclidean_distances(query_vector, other_vectors)
k=100
# min_distance = distances.min()  # Get the minimum value from the distances array
# print(min_distance)
# max_distance = distances.max()  # Get the minimum value from the distances array
# print(max_distance)
k_indices = np.argsort(distances)[0][:k]
# print(f"Indices of nearest neighbors: {k_indices}")
recs=tfidf_df["id"][k_indices]
# print(recs)




# In[14]:


title_to_id=dict(zip(movies['id'], movies['title']))
recommendations_title_id=[title_to_id[id] for id in recs]
(recommendations_title_id)




def get_recs_title(obj,movies,tfidf_df):
    title_to_id=dict(zip(movies['original_title'], movies["id"]))
    ids=[title_to_id[title] for title in obj]
    centroid=tfidf_df.loc[tfidf_df['id'].isin(ids)].mean()
    centroid_vector=pd.DataFrame([centroid], columns=tfidf_df.columns)
    tfidf_df=pd.concat([tfidf_df,centroid_vector], ignore_index=True)
    query_vector = tfidf_df.iloc[-1, 1:].values.reshape(1, -1)
    other_vectors = tfidf_df.iloc[:-1, 1:].values
    distances = euclidean_distances(query_vector, other_vectors)
    k=1000
    k_indices = np.argsort(distances)[0][:k]
    recs=tfidf_df["id"][k_indices]
    return recs[:5]


# In[30]:


def get_recs_lang(lang,movies):
    L = []
    for i, x in enumerate(movies["original_language"]):
        if lang==x:
            L.append(i)
    if not L:
        print("Movie not found lang")
        return ["Empty"]
    return movies['id'].iloc[L]


# In[31]:


def get_recs_genre(genre,movies):
    L = []
    for i, x in enumerate(movies["genres"]):
        if genre in x:
            L.append(i)
    if not L:
        print("Movie not found genre")
        return ["Empty"]
    return movies['title'].iloc[L]


# In[32]:


def get_recs_dir(dir,movies):
    L = []
    for i, x in enumerate(movies["directer"]):
        if dir==x:
            L.append(i)
    if not L:
        print("Movie not found dir")
        return ["Empty"]
    return movies['id'].iloc[L]


# In[33]:


def get_recs_actor(cast,movies):
    L = []
    for i, x in enumerate(movies["cast"]):
        if cast in x:
            L.append(i)
    if not L:
        print("Movie not found actor")
        return ["Empty"]
    return movies['id'].iloc[L]


# In[34]:


ratings = pd.read_csv('ratings_small.csv')
movie_id_to_title = dict(zip(movies['id'].astype(str), movies['title']))
# movie_title_to_id = {v: k for k, v in movie_id_to_title.items()}
movie_title_to_id = dict(zip(movies['original_title'].astype(str), movies['id']))
ratings = ratings.drop('timestamp', axis=1)
ratings['rating'].fillna(0, inplace=True)
ratings = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
ratings.columns = ratings.columns.astype(str)


# In[35]:


def get_recs(titles,lang,a,combo,movies,tfidf_df):
    titles=titles.split(',')
    titles = [x.replace(" ", "").lower() for x in titles]
    if len(titles)==1:
        return []
    rec_ids=get_recs_title(titles,movies,tfidf_df)
    movs=movies.loc[movies['id'].isin(rec_ids)]

    id_to_title=dict(zip(movies['id'], movies['title']))

    
    if lang!="skip":
        rec_ids=get_recs_lang(lang,movs)
        movs=movies.loc[movies['id'].isin(rec_ids)]
    
    if a==0 and combo!="skip":
        rec_ids=get_recs_genre(combo,movs)

    elif a==1 and combo!="skip":
        rec_ids=get_recs_dir(combo,movs)

    elif a==2 and combo!="skip":
        rec_ids=get_recs_actor(combo,movs)
        
    # recs=[title_to_id[id] for id in rec_ids]
    recs = [id_to_title.get(id) for id in rec_ids if id in id_to_title]
    # return recs

    input_movie_titles = titles
    if len(input_movie_titles) == 0:
        print("No movie titles provided. Cannot make recommendations without input.")
    else:
        valid_movie_ids = [movie_title_to_id[title] for title in input_movie_titles if title in movie_title_to_id]

        if len(valid_movie_ids) == 0:
            print("None of the provided movie titles were found in the database. Cannot make recommendations without valid input.")
        else:
            combined_similarities = np.zeros(ratings.shape[0])
            for movie_id in valid_movie_ids:
                if movie_id in ratings.columns:
                    highest_rated_users = ratings[movie_id].idxmax()
                    similarities = cosine_similarity(ratings)
                    combined_similarities += similarities[highest_rated_users]
                # else:
                #     print(f"Warning: Movie ID {movie_id} not found in ratings.")

            most_similar_users = ratings.index[np.argsort(combined_similarities)[::-1]]
            recommended_movies = set()
            for user in most_similar_users:
                unseen_movies = ratings.columns[(ratings.loc[user] == 0) & (~ratings.columns.isin(valid_movie_ids))]
                for movie in unseen_movies:
                    recommended_movies.add(movie)
                    if len(recommended_movies) >= 10:
                        break
            
                # reco_ids = list(recommended_movies)[:10]
                # recs2= [id_to_title.get(id) for id in reco_ids if id in id_to_title]

                recommended_movie_ids = list(recommended_movies)[:10]
                rec_title = [movie_id_to_title[movie_id] for movie_id in recommended_movie_ids if movie_id in movie_id_to_title]
        
        return recs ,rec_title


# In[36]:


L="Harry Potter and the Prisoner of Azkaban,Harry Potter and the Goblet of Fire"
reccs,reccs2=get_recs(L,"skip",0,"skip",movies,tfidf_df)
reccs=reccs[:11]
reccs2=reccs2[:11]
print(reccs)
print(reccs2)

