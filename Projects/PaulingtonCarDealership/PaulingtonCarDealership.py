#import necessary stuff
import csv #This thing will help us to read and write CSV files
import os #This thing will help us to manage file paths


# Get the directory where the script is located
#Allocate variable script_dir to the directory of this script
#Allocate variable db_path to the path of Database.csv in the same directory
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, "Database.csv")

#Create an empty list called "CarsList"
CarsList = []

#This function will check if input is "\n" (nothing at all), "/close", valid or invalid input
def CheckCarsList(Car):
    #strip all whitespaces before and after string, then lowercase all characters
    raw_input = Car.strip().lower()

    if raw_input == "": #if input is "\n"
        return False  #Return false for the function. Skip empty input
    
    elif raw_input == "/close": #elif input is "/close"
        print("Saving your file...\n") #prompt user about the file is saved
        
        #Prompt the user about the CarsList
        print(f"The following car list in your possession:\n")
        OutList() #Run OutList() Function to show the CarsList list of dictionaries
        
        #Prompt the user about closing program
        print("\nClosing program...")
        exit() #Shutdown program
    
    else: #all other cases != "\n" or "/close"
        
        #Use try-except block to catch ValueError
        try: #If format is correct
            
            Datas = [Data.strip().title() if Data.strip() else "N/A" for Data in Car.split(",")]
            
            while len(Datas) < 11:
                Datas.append("N/A")
            if len(Datas) > 11:
                raise ValueError

            #Assign each item to a variable
            (brand, type, model, seats, year, price, mileage, condition, fuel, transmission, color) = Datas 
            
            #Create a dictionary
            
            Vehicle_data = {
                "Brand": brand,
                "Type": type,
                "Model": model,
                "Number of Seats": seats,
                "Year": year,
                "Price": price,
                "Mileage": mileage,
                "Condition": condition,
                "Fuel Type": fuel,
                "Transmission": transmission,
                "Color": color
            }

            CarsList.append(Vehicle_data) #Add the dictionary into the CarsList list
            
            #A dict inside a list
            add_data(brand, type, model, seats, year, price, mileage, condition, fuel, transmission, color)

            return True
            #Return True statement
        
        except ValueError: #If format raises ValueError
            print("Invalid format. Please use: brand, type, model, number of seats, year, price, mileage, condition, fuel type, transmission, color")
            return False
            #Return False statement

def OutList():
    for index, name in enumerate(CarsList, start=1):
        #Start printing each car
        print(f"{index}. {name}")

#Function to check if database exist
def check_database():
    if not os.path.exists(db_path):
        with open("Database.csv", "w", newline='') as db:
            writer = csv.writer(db)
            writer.writerow([
                "Brand", "Type", "Model", "Number of Seats", "Year", "Price",
                "Mileage", "Condition", "Fuel Type", "Transmission", "Color"
            ])
            print("Database cannot be found, creating a new database")
    else:
        print("Connected to Database successfully")

#Function that add data into the file
def add_data(brand, type, model, seats, year, price, mileage, condition, fuel, transmission, color):
    with open(db_path, "a", newline='') as db:
        writer = csv.writer(db)
        writer.writerow([brand, type, model, seats, year, price, mileage, condition, fuel, transmission, color])
    print("Successfully added to database!")

def main():
    check_database()
    i = 1
    print("WELCOME USER TO PAULINGTON CAR DEALERSHIP DATABASE WRITER!\n")
    print("*Formatting: brand, type, model, number of seats, year, price, mileage, condition, fuel type, transmission, color")
    print("Example: Toyota, SUV, RAV4, 5, 2020, 25000, 30000, Used, Gasoline, Automatic, White\n")
    print("Type '/close' to save and exit the program\n")
    print("Note: You can leave any field empty by just adding a comma\n")
    print("Please enter vehicle information below:\n\n")

    while True:
        vehicle_input = input(f"Please enter vehicle number {i} information: ")
        if CheckCarsList(vehicle_input):
            i += 1  

if __name__ == "__main__":
    main() #Call main Function