import os
import csv
import pyfiglet
import secrets
import string
from cryptography.fernet import Fernet
import base64
import hashlib
from collections import defaultdict


def main():
    check_database()
    welcome_message()
    fernet = get_master_key()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_password_manual(fernet)
        elif choice == "2":
            add_password_auto(fernet)
        elif choice == "3":
            view_passwords(fernet)
        elif choice == "4":
            delete_password(fernet)
        elif choice == "5":
            update_password(fernet)
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")


def get_master_key():
    master_password = input("Enter your Master Password: ").strip()
    key = hashlib.sha256(master_password.encode()).digest()
    fernet_key = base64.urlsafe_b64encode(key)
    return Fernet(fernet_key)


def check_database():
    if not os.path.exists("Database.txt"):
        with open("Database.txt", "w", newline="") as db:
            writer = csv.writer(db)
            writer.writerow(["ID", "Website", "Username", "Password"])
            print("Database cannot be found, creating a new database")
    else:
        print("Connected to Database successfully")


def welcome_message():
    banner = pyfiglet.figlet_format("Pass Paulito Manager", font="slant")
    print(banner)
    print("Made by Paul Scott Nguyen")


def show_menu():
    print("\nOptions:")
    print("1. To add Password manually")
    print("2. To add Password automatically")
    print("3. To see all passwords")
    print("4. To delete a password")
    print("5. To update a password")
    print("6. To exit")


def add_password_manual(fernet):
    website = input("Enter Website URL: ").strip().lower()
    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()
    encrypted_password = fernet.encrypt(password.encode()).decode()

    new_id = get_next_id()
    with open("Database.txt", "a", newline="") as db:
        writer = csv.writer(db)
        writer.writerow([new_id, website, username, encrypted_password])

    print("Successfully added to database!")


def add_password_auto(fernet):
    website = input("Enter Website URL: ").strip().lower()
    username = input("Enter Username: ").strip()

    while True:
        input_length = input("Enter Password Length (int): ").strip()
        if input_length.isdigit():
            password_length = int(input_length)
            if password_length <= 0:
                print("Please enter a positive integer!")
                continue
            break
        else:
            print("Please enter a valid integer")

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(password_length))
    encrypted_password = fernet.encrypt(password.encode()).decode()

    new_id = get_next_id()
    with open("Database.txt", "a", newline="") as db:
        writer = csv.writer(db)
        writer.writerow([new_id, website, username, encrypted_password])

    print(f"Successfully added to database!\nGenerated password: {password}")


def view_passwords(fernet):
    print("\nView Passwords:")
    print("1. View by ID")
    print("2. View grouped by Website")

    while True:
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_by_id(fernet)
            break
        elif choice == "2":
            view_by_website(fernet)
            break
        else:
            print("Invalid option, Please try again!")


def view_by_id(fernet):
    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            headers = next(reader, None)
            data = list(reader)

            if not data:
                print("Database is empty.")
                return

            print(f"\n{headers[0]:<4} | {headers[1]:<20} | {headers[2]:<15} | {headers[3]}")
            print("-" * 65)
            for row in data:
                decrypted_password = fernet.decrypt(row[3].encode()).decode()
                print(f"{row[0]:<4} | {row[1]:<20} | {row[2]:<15} | {decrypted_password}")
    except FileNotFoundError:
        print("Database file not found.")


def view_by_website(fernet):
    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            next(reader, None)
            data = list(reader)

            if not data:
                print("Database is empty.")
                return

            grouped = defaultdict(list)
            for row in data:
                website = row[1]
                decrypted_password = fernet.decrypt(row[3].encode()).decode()
                grouped[website].append((row[2], decrypted_password))

            print()
            for website in sorted(grouped):
                print(f"Website: {website}")
                for username, password in grouped[website]:
                    print(f"  - {username}: {password}")
                print()
    except FileNotFoundError:
        print("Database file not found.")


def delete_password(fernet):
    website = input("Enter Website URL to delete: ").strip().lower()
    username = input("Enter Username: ").strip()

    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            header = next(reader)
            data = list(reader)
    except FileNotFoundError:
        print("Database file not found.")
        return

    found = False
    new_data = []

    for row in data:
        if row[1].strip().lower() == website and row[2].strip() == username:
            found = True
            print(f"\nProfile found: {row}")
            confirm = input("Do you want to delete this profile? (Y/N): ").strip().lower()
            if confirm in ["y", "yes"]:
                print("Profile deleted.")
                continue
            else:
                print("Deletion cancelled.")
                new_data.append(row)
        else:
            new_data.append(row)

    if not found:
        print("Profile not found.")
        return

    with open("Database.txt", "w", newline="") as db:
        writer = csv.writer(db)
        writer.writerow(header)
        for i, row in enumerate(new_data, start=1):
            writer.writerow([i, row[1], row[2], row[3]])


def update_password(fernet):
    website = input("Enter Website URL to update: ").strip().lower()
    username = input("Enter Username: ").strip()

    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            header = next(reader)
            data = list(reader)
    except FileNotFoundError:
        print("Database file not found.")
        return

    found = False
    new_data = []

    for row in data:
        if row[1].strip().lower() == website and row[2].strip() == username:
            found = True
            print(f"\nProfile found: {row}")
            new_password = input("Type your new password: ").strip()
            row[3] = fernet.encrypt(new_password.encode()).decode()
            print("Password updated successfully.")
        new_data.append(row)

    if not found:
        print("Profile not found.")
        return

    with open("Database.txt", "w", newline="") as db:
        writer = csv.writer(db)
        writer.writerow(header)
        for i, row in enumerate(new_data, start=1):
            writer.writerow([i, row[1], row[2], row[3]])


def get_next_id():
    try:
        with open("Database.txt", "r", newline="") as db:
            reader = csv.reader(db)
            next(reader, None)
            data = list(reader)
            if data:
                last_id = int(data[-1][0])
            else:
                last_id = 0
    except FileNotFoundError:
        last_id = 0
    return last_id + 1


if __name__ == "__main__":
    main()
