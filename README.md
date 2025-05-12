This is a content-based movie recommender system that suggests similar movies based on the one selected by the user. The recommendations are made using cosine similarity on movie feature vectors.

🚀 Features
Select a movie from a dropdown list.
Get 10 similar movie recommendations.
Posters of recommended movies fetched dynamically via TMDb API.
Simple and interactive frontend using Streamlit.

🧠 How It Works
Each movie is represented as a vector of combined features (such as genres, keywords, cast, etc.).
Using cosine similarity, the app finds how close other movies are to the selected one.
The top 10 most similar movies (excluding the selected one) are returned as recommendations.

🛠️ Technologies Used
Python
Pandas
Scikit-learn
Streamlit
TMDb API
Cosine Similarity

📦 Note
Large files like .pkl models are not included in this repository due to GitHub's file size limit. You'll need to download them separately if you're running the app locally.

💡 Future Enhancements
Add collaborative filtering support
Deploy on a cloud platform (Streamlit Cloud / Heroku)
Add search functionality
Improve UI/UX

