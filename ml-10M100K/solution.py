#http://files.grouplens.org/datasets/movielens/ml-10m.zip

import pandas as pd

movies_file = 'movies.dat'
ratings_file = 'ratings.dat'

# Define file paths and column names
movies_columns = ['movieid', 'title', 'genres']
ratings_columns = ['userid', 'movieid', 'rating', 'timestamp']

# Read movies and ratings data into DataFrames
movies_df = pd.read_csv(movies_file, sep='::', engine='python', header=None, names=movies_columns)
ratings_df = pd.read_csv(ratings_file, sep='::', engine='python', header=None, names=ratings_columns)

# Merge movies and ratings DataFrames based on "movieid" column
movielens_df = pd.merge(movies_df, ratings_df, on='movieid')

# Print the first few lines of the merged DataFrame to verify that they work normally
# print(movielens_df.head())



# row_count = movielens_df.shape[0]
# print("Number of rows in movielens_df:", row_count)

# column_count = movielens_df.shape[1]
# print("Number of columns in movielens_df:", column_count)

# zero_count = (movielens_df['rating'] == 0).sum()
# print("Number of zeros in the 'rating' column:", zero_count)

# three_count = (movielens_df['rating'] == 3).sum()
# print("Number of threes in the 'rating' column:", three_count)

# num_movies = movielens_df['movieid'].nunique()
# print("Number of different movies:", num_movies)

# num_users = movielens_df['userid'].nunique()
# print("Number of different users:", num_users)



# # Count of movie ratings in the "Drama" genre
# drama_ratings = movielens_df[movielens_df['genres'].str.contains('Drama', case=False)]
# drama_count = drama_ratings.shape[0]
#
# # Count of movie ratings in the "Comedy" genre
# comedy_ratings = movielens_df[movielens_df['genres'].str.contains('Comedy', case=False)]
# comedy_count = comedy_ratings.shape[0]
#
# # Count of movie ratings in the "Thriller" genre
# thriller_ratings = movielens_df[movielens_df['genres'].str.contains('Thriller', case=False)]
# thriller_count = thriller_ratings.shape[0]
#
# # Count of movie ratings in the "Romance" genre
# romance_ratings = movielens_df[movielens_df['genres'].str.contains('Romance', case=False)]
# romance_count = romance_ratings.shape[0]
#
# # Print the counts
# print("Drama:", drama_count)
# print("Comedy:", comedy_count)
# print("Thriller:", thriller_count)
# print("Romance:", romance_count)



# # Group the dataset by movie and count the number of ratings for each movie
# movie_ratings_count = movielens_df.groupby('title')['rating'].count()
#
# # Find the movie with the highest number of ratings
# movie_with_most_ratings = movie_ratings_count.idxmax()
#
# # Print the movie with the highest number of ratings
# print("Movie with the greatest number of ratings:", movie_with_most_ratings)



# Count the occurrences of each rating
rating_counts = movielens_df['rating'].value_counts()

# Get the five most given ratings in order from most to least
five_most_given_ratings = rating_counts.head(5)

# Print the five most given ratings
print(five_most_given_ratings)

