import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies= []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
# st.title('want movies recommendations ?')

st.markdown("""
    <h1 style='text-align: center; color: #F63366;'>🎬 Movie Recommender System</h1>
    <p style='text-align: center;'>Tell us a movie you like, and we'll find your next binge!</p>
""", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "👇 What movie would you like recommendations based on?",
    movies['title'].values)
if st.button("🔍 Recommend Movies"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)  # 5 columns, 2 rows total for 10 movies
    for i in range(10):
        with cols[i % 5]:  # cycle through columns
            st.image(posters[i])
            st.caption(names[i])


# --- Closing Message ---
    st.markdown("""
        <hr>
        <div style='text-align: center;'>
            🍿 Grab your popcorn and dive in — we'll be here with more magic when you're ready for the next showtime! 🎬✨
        </div>
    """, unsafe_allow_html=True)

