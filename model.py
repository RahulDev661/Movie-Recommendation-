import pandas as pd
import pickle
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

# Merge datasets
movies = movies.merge(credits, on='title')

# Select important columns
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# Drop null values
movies.dropna(inplace=True)

# Convert string to list
def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)

# Take top 3 cast
def convert_cast(text):
    L = []
    count = 0
    for i in ast.literal_eval(text):
        if count < 3:
            L.append(i['name'])
            count += 1
    return L

movies['cast'] = movies['cast'].apply(convert_cast)

# Fetch director
def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L

movies['crew'] = movies['crew'].apply(fetch_director)

# Convert overview to list
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces
def collapse(L):
    return [i.replace(" ", "") for i in L]

movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)

# Create tags
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# New dataframe
new_df = movies[['movie_id','title','tags']]

# Convert list to string
new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))

# Lowercase
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Similarity
similarity = cosine_similarity(vectors)

# Save files
pickle.dump(new_df, open('movies.pkl', 'wb'))
pickle.dump(similarity, open('similarity.pkl', 'wb'))

print("✅ Real dataset model built successfully!")