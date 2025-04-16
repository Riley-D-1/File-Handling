# TODO: Open "movies.txt" in write mode
f = open("movies.txt", "a")
 # TODO: Ask the user for a favourite movie THREE TIMES. Be efficient in your code.
for i in range(1,4):
        Movie_choice=input(f"Number {i} Favourite Movie: ")
        f.write(f"{Movie_choice} ")
        # TODO: Write the movie to the file with a newline

# TODO: Let the user know movies have been saved to file

f.close()
f = open("movies.txt", "r")
print(str(f.read()))
# TODO: Check the file and ensure it worked!