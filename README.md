🍿 Rahul's Movie Recommender System

A sleek and intelligent Movie Recommendation Web App built using Streamlit, powered by a machine learning similarity model.
Discover movies similar to your favorites with a beautiful, modern UI.

🚀 Live Demo

(Add your deployed link here after hosting)
👉 https://your-app-link.streamlit.app

📌 Features
🎥 Select any movie from the list
🤖 Get top 5 similar movie recommendations
🖼️ Movie posters fetched using TMDB API
🌙 Modern Netflix-style dark UI
⚡ Fast and responsive interface
🛠️ Tech Stack
Frontend/UI: Streamlit
Backend Logic: Python
Machine Learning: Cosine Similarity
API: TMDB (The Movie Database)
Libraries Used:
pandas
pickle
requests
📂 Project Structure
movie-recommender/
│
├── app.py               # Main Streamlit app
├── movies.pkl          # Movie dataset
├── similarity.pkl      # Similarity matrix
├── requirements.txt    # Dependencies
└── README.md           # Project documentation
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/movie-recommender.git
cd movie-recommender
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the App
streamlit run app.py
🔑 TMDB API Setup

This project uses The Movie Database (TMDB) API.

Go to: https://www.themoviedb.org/
Create an account
Generate an API key
Replace this line in app.py:
api_key = "YOUR_API_KEY"
🧠 How It Works
Movies are vectorized using text features (like genres, keywords, cast)
A similarity matrix is created using cosine similarity
When a movie is selected:
The system finds the most similar movies
Fetches posters using TMDB API
Displays them in a visually appealing layout
📸 Screenshots

(Add screenshots here)

🌐 Deployment

You can deploy easily on:

Streamlit Cloud
Render
Railway
Streamlit Cloud Steps:
Push code to GitHub
Go to https://streamlit.io/cloud
Connect repo
Deploy 🚀
🔮 Future Improvements
⭐ Add movie ratings
🎬 Trailer integration
🔍 Smart search with autocomplete
❤️ Favorite/watchlist feature
📱 Mobile optimization
🤖 AI-based recommendations
🤝 Contributing

Contributions are welcome!

Fork the repo
Create a new branch
Commit changes
Open a Pull Request
📜 License

This project is licensed under the MIT License.

🙌 Acknowledgements
TMDB for movie data
Streamlit for the amazing framework
👨‍💻 Author

Rahul Dev
📧 (Add your email)
🌐 (Add LinkedIn/GitHub)
