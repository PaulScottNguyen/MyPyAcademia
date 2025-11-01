def main(): #The main function
    #Prompt the user
    print("Hello! My name is Paulito, I will recommend you a game based on your liking!")
    #Choose their options
    difficulty = str(input("Options (Difficult or Casual): ")).strip().lower()
    if not (difficulty == "difficult" or difficulty == "casual"):
        print(f"You entered invalid difficulty! Please enter a valid one!")
        main() #Will rerun main()
    players = str(input("Options (Multiplayer or Singleplayer): ")).strip().lower()
    if not (players == "multiplayer" or players == "singleplayer"):
        print(f"You entered invalid number of players! Please enter a valid one!")
        main() #Will rerun main()

    #There are 4 possible combinations
    if difficulty == "difficult" and players == "multiplayer":
            recommend("Blood and iron")
    elif difficulty == "difficult" and players == "singleplayer":
            recommend("Call of duty")
    elif difficulty == "casual" and players == "multiplayer":
            recommend("Fortnite")
    elif difficulty == "casual" and players == "singleplayer":
            recommend("Ravenfield")
    else:
            recommend("a game that I haven't played before")

def recommend(game):
    print(f"You might like {game}")
main()