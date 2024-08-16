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

#find mean
mean = musicalMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = int(musicalMovieData["audience_rating"].median())
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Create histogram
plt.hist(musicalMovieData["audience_rating"], range = (0, 100), bins = 20, color = "gold")

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Musical Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Musical Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most of the movies are very highly rated, with the largest bin being from 84-88%, which is where my favourite movie lies! This is above the mean audience rating of the data set and the histogram appears to have a very steep pyramid shape before dropping down rapidly in the last 2 bins. This may mean that generally musical & performing arts movies are not considered good enough to be rated above 88%. "
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = musicalMovieData, x = "audience_rating", y = "critic_rating", color = "crimson", label = "Musical Movies")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a positive correlation between critic rating and audience rating, with points being very dispersed towards te lower ratings, showing that often lower rated movies are very subjective and based on the viewer/critic, and points being very close together towards higher ratings, showing that higher-rated movies are probably more obviously high-rated. The closer points could also be due to how higher rated movies are often watched more and are more popular than lower rated movies, and the audience generally tends to act similarly to each other, with previous ratings influencing their rating. There are some strange outliers, however, as some movies ranked low by the audience are ranked very high by the critics and some movies ranked high by the audience are ranked very low by the critics."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

plt.scatter(data = favMovieData, x = "audience_rating", y = "critic_rating", label = favMovie, color = "dodgerblue")
plt.legend()
plt.grid(True)
plt.title("Audience rating vs Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.show()

print("\nThank you for reading through my data analysis!")
