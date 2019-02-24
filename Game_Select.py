from Frogger import Frogger
from Snake import snake
import os.path

games = ["Snake (Standard)", "Snake (Speed)","Frogger"]
scores = []


def select():
    global scores
    print("\n"*3)
    user = input("What is your name? ")
    print("What game would you like to play? ")
    for game in games:
        print(game)
    choice = input()
    choice=choice.lower()
    file = open("Scores.txt", "a")
    if choice == "standard":
        result = snake.standard()
        result.insert(0, "Snake")
        result.insert(1, user)
        scores.append(result)
        file.write(str(result).replace("[", "").replace("]", "")+str("\r\n"))
    elif choice == "speed":
        result = snake.speed()
        result.insert(0, "Snake")
        result.insert(1, user)
        scores.append(result)
        file.write(str(result).replace("[", "").replace("]", "")+str("\r\n"))
    elif choice == "frogger":
        result = frogger.play()
        result.insert(0, "Frogger")
        result.insert(1, user)
        scores.append(result)
        file.write(str(result).replace("[", "").replace("]", "")+str("\r\n"))

    else:
        print("Unknown game!")
    file.close()
    select()


if not os.path.exists("Scores.txt"):
    file = open("Scores.txt", "w")
    file.write("Snake, user, Score, Length, Time, Speed")
    file.close()
select()
