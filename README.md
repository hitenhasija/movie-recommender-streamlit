# 🎬 Movie Recommender System

A content-based movie recommendation system built with **Streamlit**, powered by cosine similarity and movie metadata.

🔗 **Live Demo** → [Try it now](https://movie-recommender-app-j3nqudjz22tawcvhnzstzr.streamlit.app/)

---

## 🚀 Features

- 🔍 Select any movie from the list
- 🎯 Get top 5 similar movie recommendations
- 🖼️ Displays official movie posters via OMDb API
- 🎲 "Surprise Me" feature for fun recommendations
- ⚡ Fast response using precomputed similarity matrix

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Pandas**, **NumPy**
- **Joblib** (for optimized similarity storage)
- **OMDb API** (for fetching poster images)

---

## 📁 Project Structure

| File                         | Description                             |
|------------------------------|-----------------------------------------|
| `app.py`                     | Main Streamlit app                      |
| `new_df.csv`                 | Cleaned movie title dataset             |
| `similarity_compressed.pkl`  | Precomputed similarity matrix (Joblib)  |
| `requirements.txt`           | All required Python dependencies        |

---

## 💡 How it Works

- A cosine similarity matrix was built offline using TMDb metadata
- On movie selection, the app finds the 5 closest movies in vector space
- Posters are fetched dynamically from the OMDb API

---

## 🙋‍♂️ About Me

I'm **Hiten Hasija**, a final-year engineering student passionate about machine learning and real-world AI applications.

📬 [LinkedIn](https://linkedin.com/in/hitenhasija) | [GitHub](https://github.com/hitenhasija)

---

> Built to learn. Built to share. Built to stand out. 🌟
