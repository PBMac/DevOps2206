def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG).")
    print("Here you can find many cool games to play.")

def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a game sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game = print(int(input("Please choose a number 1-3: ")))


    diff = print(int(input("Please choose game difficulty from 1 to 5: ")))

    return game, diff
