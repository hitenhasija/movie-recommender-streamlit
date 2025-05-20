import streamlit as st
import pandas as pd
import numpy as np
import requests
import random
import joblib

# Set up Streamlit page config
st.set_page_config(layout="wide", page_title="Movie Recommender", page_icon="🎬")
st.markdown("<h1 style='text-align:center; color:#f63366;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("##")

# Load data
new_df = pd.read_csv('D:/python/movie recommendation project/new_df.csv')
similarity = joblib.load("D:/python/movie recommendation project/similarity_compressed.pkl")


# Select movie from dropdown
selected_movie = st.selectbox("🎞️ Select a Movie:", new_df['title'].values)

# Function to fetch movie poster from OMDb
def fetch_movie_poster(movie_title):
    try:
        response = requests.get(f"https://www.omdbapi.com/?t={movie_title}&apikey=f6ad9a97")
        data = response.json()
        poster_url = data.get("Poster", "")
        if poster_url == "N/A" or poster_url == "":
            return "https://via.placeholder.com/300x450?text=No+Poster"
        return poster_url
    except:
        return "https://via.placeholder.com/300x450?text=Error"

# Function to get movie recommendations
def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_title = new_df['title'].iloc[i[0]]
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_movie_poster(movie_title))
    return recommended_movies, recommended_posters

# Buttons to trigger recommendation or surprise pick
recommend_triggered = False
if st.button("🎯 Recommend", type="primary"):
    recommend_triggered = True
elif st.button("🎲 Surprise Me"):
    selected_movie = random.choice(new_df['title'].values)
    recommend_triggered = True

# Show recommendations
if recommend_triggered:
    st.markdown("---")
    st.markdown("<h3 style='text-align:center;'>🍿 Recommended Movies for You</h3>", unsafe_allow_html=True)
    
    names, posters = recommend(selected_movie)
    cols = st.columns(5)

    for idx, col in enumerate(cols):
        with col:
            st.image(posters[idx], use_container_width=True)
            st.markdown(f"<p style='text-align:center; font-weight:bold;'>{names[idx]}</p>", unsafe_allow_html=True)
            imdb_url = f"https://www.imdb.com/find?q={names[idx].replace(' ', '+')}"
            st.markdown(f"<p style='text-align:center;'><a href='{imdb_url}' target='_blank'>🔗 IMDb</a></p>", unsafe_allow_html=True)
