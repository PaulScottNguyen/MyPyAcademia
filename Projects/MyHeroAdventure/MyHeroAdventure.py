import time #Library that will allow the program to pause

def dramatic_pause():
    time.sleep(2) #This will delay the code from executing for 2 second
    print("...")

def intro():
    print("Welcome to: PAULITO QUIRKY ADVENTURE")
    name = input("What's your name, you little crybaby hero-in-training? ")
    print(f"\nOMG {name.upper()}?! That name SLAPS. Let's gooo, PLUSS ULTRAA!!!")
    return name

def choose_path(name):
    print(f"\n{name}, you wake up in U.A. High School dorms. You hear screaming. Typical.")
    
    dramatic_pause()
    print("Do you go:")
    print(" Left (toward the cafeteria, maybe there's drama)")
    print(" Right (toward the training grounds, probs explosions)")
    print(" Up (climb the wall like a cat)")
    print(" Down (crawl into the basement)")
    choice = input("Pick your vibe (left/right/up/down): ").lower()

    if choice == "left":
        cafeteria_scene(name)
    elif choice == "right":
        training_scene(name)
    elif choice == "up":
        cat_scene(name)
    elif choice == "down":
        basement_scene(name)
    else:
        print("Bro what. That wasn't even an option. Try again.\n")
        choose_path(name)

def cafeteria_scene(name):
    print(f"\nYou burst into the cafeteria like a main character, {name}.")
    dramatic_pause()
    print("Bakugo is yelling at a toaster. Deku is crying. Again.")
    dramatic_pause()
    print("Do you intervene? (yes/no)")
    choice = input("Your move: ").lower()
    if choice == "yes":
        print(f"\nYou scream 'SHUT UP BAKUGO' and throw a croissant. You're now class president. Slay, {name}.")
    elif choice == "no":
        print(f"\nYou grab a juice box and vibe. Bakugo respects your chill. Deku cries harder.")
    else:
        print("That wasn't yes or no, bestie. Try again.")
        cafeteria_scene(name)

def training_scene(name):
    print(f"\nYou arrive at the training grounds. All Might is doing TikTok dances and Colgate commercial.")
    dramatic_pause()
    print("Do you join him? (yes/no)")
    choice = input("Your move: ").lower()
    if choice == "yes":
        print(f"\nYou hit the griddy so hard, All Might sheds a tear. You're now his favorite, {name}.")
    elif choice == "no":
        print(f"\nYou walk away in shame. All Might unfollows you on Instagram.")
    else:
        print("That wasn't yes or no, bestie. Try again.")
        training_scene(name)

def cat_scene(name):
    print(f"\nYou climb the wall like a raccoon. Midnight sees you and applauds.")
    dramatic_pause()
    print("Do you meow at her? (yes/no)")
    choice = input("Your move: ").lower()
    if choice == "yes":
        print(f"\nShe gives you extra credit for commitment. You're now top of the class, {name}.")
    elif choice == "no":
        print(f"\nShe’s disappointed. You cry in the vents.")
    else:
        print("That wasn't yes or no, bestie. Try again.")
        cat_scene(name)

def basement_scene(name):
    print(f"\nYou crawl into the basement. It's dark. You hear... Todoroki reciting poetry?")
    dramatic_pause()
    print("Do you listen? (yes/no)")
    choice = input("Your move: ").lower()
    if choice == "yes":
        print(f"\nHis poem is about daddy issue. You cry together. Bonding moment, {name}.")
    elif choice == "no":
        print(f"\nYou interrupt him with a fart noise. He respects the chaos.")
    else:
        print("That wasn't yes or no, bestie. Try again.")
        basement_scene(name)

# Start the game
def main():
    player_name = intro()
    choose_path(player_name)
main()
