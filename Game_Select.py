import Snake as snake
import os.path

games = ["Snake", "Frogger"]
scores = []


def select():
    global user
    global scores
    print("\n"*3)
    print("What game would you like to play?")
    for game in games:
        print(game)
    choice = input()
    file = open("Scores.txt", "a")
    if choice == "Snake":
        result = snake.play()
        result.insert(0, "Snake")
        result.insert(1, user)
        scores.append(result)
        file.write(str(result).replace("[", "").replace("]", ""))
    else:
        print("Unknown game!")
    file.close()
    select()


user = input("Please enter a name: ")
if not os.path.exists("Scores.txt"):
    file = open("Scores.txt", "w")
    file.write("Snake, user, Score, Length, Time, Speed")
    file.close()
select()
