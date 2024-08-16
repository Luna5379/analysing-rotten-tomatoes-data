import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Help!"

print("My favourite movie is", favMovie)
#print(movieData['movie_title'])

print("\nThe data for my favorite movie is:\n")
favMovieBooleanList = movieData["movie_title"] == favMovie
favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

musicalMovieBooleanList = movieData["genres"].str.contains("Musical & Performing Arts")

musicalMovieData = movieData.loc[musicalMovieBooleanList]
numOfMovies = musicalMovieData.shape[0]


print("\n\n")





print("We will be comparing " + favMovie +
      " to other movies under the genre Musical & Performing Arts in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Musical & Performing Arts.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#min
min = musicalMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated "+ str(int(favMovieData["audience_rating"]) - min) +" points higher than the lowest rated movie.")
print()

#find max
max = musicalMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated "+ str(max -int(favMovieData["audience_rating"])) +" points lower than the highest rated movie.")
print()
