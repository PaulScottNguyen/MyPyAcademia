"""
BUZZ
Players take turns counting in sequence, starting with 1.
At every number that is a multiple of 7 or contains the digit 7, the player must say "BUZZ" instead of the number (e.g., 7, 17, 27)
"""

def main():
    while True:
        try:
            Number = int(input("Enter an int number: "))

            if Number % 7 == 0:
                print("\nBUZZ!\n")
            elif "7" in str(Number):
                print("\nBUZZ!\n")
            else:
                print(f"\n{Number}\n")

        except ValueError:
            print("\nPlease enter an int number!\n")


if __name__ == "__main__":
    main()
