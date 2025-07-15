# 🎬 Movie Recommendation System Using Machine Learning Algorithms

> A personalized movie recommendation engine that uses Content-Based and Collaborative Filtering, integrated with a Telegram chatbot for interactive user experience.

---

## 📂 Dataset Used

**The Movies Dataset** from [Kaggle](https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset)

---

## 🔧 Data Cleaning

To ensure high-quality input for the recommendation models, we performed:

1. **Handling Missing Values**
   - Removed rows and columns with nulls in essential fields like genres, cast, etc.

2. **Data Type Conversion**
   - Converted `movieId` to string for compatibility.

3. **Standardizing Textual Data**
   - Lowercased text, removed special characters and extra spaces for uniform processing.

---

## 🎯 Content-Based Filtering

### 📥 Feature Extraction
- Extracted `genres`, `cast`, `crew` (directors), `keywords`, and `overview` fields.
- Combined these into a single `tags` column using text processing and merging.

### ✒️ TF-IDF Vectorizer
- Transformed the `tags` column into numerical vectors using **TF-IDF Vectorization**.

### 🎯 Centroid + Euclidean Distance
- Calculated a **centroid** of the selected movies in TF-IDF space.
- Measured **Euclidean distance** between centroid and other movies to rank similarity.

### 🤖 K-Nearest Neighbors (KNN)
- Used KNN to fetch the most similar `k` movies, reducing noise and boosting accuracy.

📌 **Output:** Movies similar to user's favorite titles based on selected Genre/Actor/Director.

---

## 👥 Collaborative Filtering

### 📥 Data Preparation
- Used `ratings.csv` and `movies.csv`.
- Mapped `movieId` to `movieTitle` and ensured all ratings data is string-typed.

### 🧮 Cosine Similarity
- Built a **pivot table** of users vs. movie ratings.
- Applied **cosine similarity** to find similar users.

### 🎁 Unseen Movie Suggestion
- Recommended movies liked by similar users but unseen by the current user.

📌 **Output:** Personalized movie suggestions based on rating behavior of similar users.

---

## 🤖 Telegram Chatbot Interface

A fully interactive **Telegram Bot** (built with `pyTelegramBotAPI`) that collects user inputs and delivers recommendations.

### 💬 Features:
- `/start` - Start interaction  
- `/recommend` - Start movie recommendation flow  
- `/chat` - Casual chat mode with movie-related facts  
- `/fact` - Get a fun movie fact  
- `/skip` - Skip a question  
- `/end` - Exit chat mode  

### 🤖 Chat Features:
- Dynamic replies, emoji support 🎬🍿
- Facts about movies 🎥
- GIF reactions
- Error handling and flexible input parsing

### 📦 Recommendation Flow:
1. User provides favorite movies
2. Selects language
3. Chooses Genre / Actor / Director
4. Bot fetches top 10 movies from both models and returns them in chat

---



## 🧑‍💻 Built With

- Python 🐍
- Pandas, NumPy
- Scikit-learn
- TF-IDF
- Cosine Similarity
- Telebot (pyTelegramBotAPI)
- Matplotlib (for visualizations)

---

## 🏁 Getting Started

### Prerequisites
- Python 3.7+
- `pip install -r requirements.txt`  
(includes `pandas`, `numpy`, `scikit-learn`, `telebot`, etc.)

### Run the Bot
```bash
python bot.py
