star_wars_movies = [
    ["The Phantom Menace", "Attack of the Clones", "Revenge of the Sith"],
    ["A New Hope", "The Empire Strikes Back", "Return of the Jedi"],
    ["The Force Awakens", "The Last Jedi", "The Rise of Skywalker"],
]

trilogy_number = int(input("Enter the number of the trilogy (1, 2, or 3): "))

film_number = int(input("Enter the number of the film in this trilogy (1, 2, or 3): "))

film_title = None
if 1 <= trilogy_number <= 3 and 1 <= film_number <= 3:
    film_title = star_wars_movies[trilogy_number - 1][film_number - 1]
    print("The film you selected is: ",film_title)