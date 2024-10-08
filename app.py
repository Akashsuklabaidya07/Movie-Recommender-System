
import pickle
import streamlit as st
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=89d3253dc7dc25b951c36c8f3644e9c5&language=en-US'.format(movie_id), timeout = 10)
     ## add a timeout of 10 second
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

## making the function for movie recommandation
def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x:x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = i[0]
        
        recommended_movies.append(movies.iloc[i[0]].title)
        ## fetch movie poster from API
        recommended_movies_posters.append(fetch_poster(i[0]))
    return recommended_movies, recommended_movies_posters
        
    
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies= pd.DataFrame(movies_dict)

st.title("Movie Recommender System")  ## title of the website

selected_movie_name= st.selectbox(
    "Select Movie Name",

    
    movies['title'].values  ## text box add
)


if st.button("Recommended Movies"):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2]) 
    with col4:
        st.text(names[3])
        st.image(posters[3])  
    with col5:
        st.text(names[4])
        st.image(posters[4])