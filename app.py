import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response=requests.get()
def recommend (movie):
    movie_index=movies_list_df[movies_list_df['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]


    recommended_movies=[]


    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies_list_df.iloc[i[0]].title)
    return recommended_movies


st.title("Movie recommender system")
movies_list_df=pickle.load(open('movies.pkl','rb'))
movies_titles=movies_list_df['title'].values

similarity=pickle.load(open('similarity.pkl','rb'))


selected_movies=st.selectbox('select a movie',(movies_titles))

if st.button('Recommend'):
    pass
    recommendations=recommend(selected_movies)
    for i in recommendations:
        st.write(i)
