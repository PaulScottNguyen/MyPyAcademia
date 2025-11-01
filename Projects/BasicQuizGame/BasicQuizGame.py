#Score counter
Score = 0 
#Prompt the user for their player name to make a friendly greeting
PlayerName = str(input("Hey there, What is your name? ")).lower().title()
#Greetings, prompt the user if they want to play the quiz game
print(f"Bonjour {PlayerName}! My name is Paulito, do you want to play a simple quiz game?")

PlayOptions = str(input("""\t Options (yes/no): """)).lower() #lower case everything
if PlayOptions != "yes": #If its not a "yes"
    quit() #Will exit the program

print(f"OK {PlayerName}! Lets Go! PLUS ULTRA!")

#Questions, could have used a function but meh we dont need to over-complicate stuff
print("Question 1. What is the most used search engine?")
AnswerOptions = str(input("""\t Answer: """)).lower() #lower case everything
if AnswerOptions == "google": 
    Score = Score + 1
    print("Correct!")
else:
    print("Incorrect!")

print("Question 2. What do you use to type?")
AnswerOptions = str(input("""\t Answer: """)).lower() #lower case everything
if AnswerOptions == "keyboard": 
    Score = Score + 1
    print("Correct!")
else:
    print("Incorrect!")
    
print("Question 3. What do you call a portable computer?")
AnswerOptions = str(input("""\t Answer: """)).lower() #lower case everything
if AnswerOptions == "laptop": 
    Score = Score + 1
    print("Correct!")
else:
    print("Incorrect!")
    
print("Question 4. Which line do you use to connect to the internet?")
AnswerOptions = str(input("""\t Answer: """)).lower() #lower case everything
if AnswerOptions == "ethernet": 
    Score = Score + 1
    print("Correct!")
else:
    print("Incorrect!")
    
print("Question 5. Which port is most commonly used to connect stuff?")
AnswerOptions = str(input("""\t Answer: """)).lower() #lower case everything
if AnswerOptions == "usb": 
    Score = Score + 1
    print("Correct!")
else:
    print("Incorrect!")
    
print("Question 6. What is the most used operating system ecosystem?")
AnswerOptions = str(input("""\t Answer: """)).lower() #lower case everything
if AnswerOptions == "windows": 
    Score = Score + 1
    print("Correct!")
else:
    print("Incorrect!")

print(f"You finished all the questions, {PlayerName}, Congratulation!")
print(f"\t Your total points is: {Score} ({(Score/6)*100}%)")