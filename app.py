import streamlit as st
import pickle
import pandas as pd
import requests

# Set page configuration
st.set_page_config(page_title="Movie Recommender", layout="wide", page_icon="🍿")

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url).json()
        poster_path = data.get('poster_path', '')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"
    except Exception as e:
        return "https://via.placeholder.com/500x750?text=Error"

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Load data
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Custom CSS for aesthetics
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #e50914;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 8px;
    padding: 10px 24px;
    border: none;
    transition: 0.3s;
}
div.stButton > button:first-child:hover {
    background-color: #f40612;
    transform: scale(1.05);
}
h1 {
    text-align: center;
    font-family: 'Arial Black', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.title("🍿 Rahul's- Movie Recommender")
st.markdown("<h4 style='text-align: center; color: grey;'>Discover your next favorite movie!</h4>", unsafe_allow_html=True)
st.markdown("---")

selected_movie = st.selectbox(
    "Type or select a movie you like:",
    movies['title'].values
)

if st.button("Recommend"):
    with st.spinner('Finding the best movies for you...'):
        names, posters = recommend(selected_movie)
        
        st.markdown("<br>", unsafe_allow_html=True)
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                st.image(posters[idx], use_container_width=True)
                st.markdown(f"<h5 style='text-align: center;'>{names[idx]}</h5>", unsafe_allow_html=True)