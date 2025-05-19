movies = ["Dora", "Monstrous", "iron man", "x-man", "KGF"]

print(f"My most favourite movie is {movies[0]}.\nMy least favourite movie is {movies[len(movies) - 1]}.")

print(f"My most favourite movie is {movies[-len(movies)]}.\nMy least favourite movie is {movies[-1]}.")

movies.append("Water World")

print(f"Updated new movie list : {movies}")

print(f"Total numbers of movies : {len(movies)}")