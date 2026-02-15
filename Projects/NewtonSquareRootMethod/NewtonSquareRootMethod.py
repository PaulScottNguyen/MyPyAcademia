"""
Newton's Square Root Method
x[n+1]=1/2(x[n] + a/x[n])
The solution will double in accuracy in each iteration
"""
def main():
    while True:
        try:
            XRoot = (float(input("Enter X root number: ")))
            if XRoot == 0:
                print("\nPlease enter a number different than 0!\n")
            else:
                break
        except ValueError: 
            print("\nPlease enter a number!\n")

    while True:
        try:
            FindRoot = (float(input("Enter a number: ")))
            if FindRoot <= 0:
                print("\nPlease enter a positive number!\n")
            else:
                break
        except ValueError: 
            print("\nPlease enter a number!\n")
        
    while True:
        try:
            Iterations = (int(input("Enter number of iterations (accuracy): ")))
            if Iterations <= 0:
                print("\nPlease enter a positive integer!\n")
            else:
                break
        except ValueError:
            print("\nPlease enter an integer!\n")
    
    while True:
        try:
            print("\nMake a guess of root(", FindRoot, ") = ", end="")
            Guess = (float(input()))
            if Guess <= 0:
                print("\nPlease enter a positive number!\n")
            else:
                break
        except ValueError:
            print("\nPlease enter a number!\n")

    for i in range(Iterations):
        RootValue = (((XRoot-1)/XRoot)*Guess) + ((FindRoot/(XRoot* pow(Guess,(XRoot-1)))))
        Guess = RootValue
        EstimatedNum = RootValue
    
    print("\nEstimated value is: ", EstimatedNum)
    
if __name__ == "__main__":
   main()