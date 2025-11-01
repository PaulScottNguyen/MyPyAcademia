#A library to help the computer make random decisions
from random import randint

#Options in Game
Options = ["rock","paper","scissors"]


def main():

    #Variables that show scores
    HumanWins = 0
    ComputerWins = 0

    while True:
        UserChoice = str(input("Type rock/paper/scissors or q to quit: ")).strip().lower()
        if UserChoice == "q":
            break
        if UserChoice not in Options:
            continue
        
        #The program will randomly choose a number
        RandomChoice = randint(0,2)
        ComputerPick = Options[RandomChoice] #The number will be the designated item in the list
        print(f"AI has picked {ComputerPick}")
        
        #Chances for HumanWins
        if UserChoice == "rock" and ComputerPick == "scissors":
            print("You won this round!")
            HumanWins += 1
        elif UserChoice == "paper" and ComputerPick == "rock":
            print("You won this round!")
            HumanWins += 1
        elif UserChoice == "scissors" and ComputerPick == "paper":
            print("You won this round!")
            HumanWins += 1
        
        #Chances for a tie
        elif UserChoice == "rock" and ComputerPick == "rock":
            print("You tied this round!")
        elif UserChoice == "paper" and ComputerPick == "paper":
            print("You tied this round!")
        elif UserChoice == "scissors" and ComputerPick == "scissors":
            print("You tied this round!")
        
        #Chances for ComputerWins
        else:
            print("AI won this round")
            ComputerWins += 1
    
    #Break after pressing q
    print(f"You won {HumanWins} times!")
    print(f"AI won {ComputerWins} times!")
    print("\nThank you for playing! Goodbye!")


if __name__ == "__main__":
    main()