def SigmaSummation(term, a, b):
    total = 0
    for i in range(a, b+1):
        total = term(i) + total
    return total

def main():
    a =  int(input("Enter start = "))
    b =  int(input("\nEnter end" \
    " = "))
    term = str(input("\nEnter a term with variable x only: ")).strip()
    print(SigmaSummation(lambda x: eval(term), a, b))

if __name__ == "__main__":
    main()