#Function to do multiplication, then check condition if over 1000
def multiplication_or_sum(Num1, Num2):
    product = Num1 * Num2
    if product > 1000:
        return Num1+Num2 #return sum
    else:
        return product #return value

Num1 = int(input("Please enter interger Num1: "))
Num2 = int(input("Please enter interger Num2: "))
print(f"Your number is: {multiplication_or_sum(Num1, Num2)}")