# Use groupBy and mean to aggregate the column
ratings_per_film_df = rating_df.groupBy('film_id').mean()

# Join the tables using the film_id column
film_df_with_ratings = film_df.join(
    ratings_per_film_df,
    on='film_id',
    how='inner'
)

# Show the first 5 results
print(film_df_with_ratings.show(5))