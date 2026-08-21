# Advance version of calculator with loop:

def add(a,b):
    return a + b

def subs(a,b):
    return a - b

def multi(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
 
def menu():
    print("1. Addition of numbers")
    print("2. Substraction of numbers")
    print("3. Multiplication of numbers")
    print("4. Division of numbers")

count = 0
play = "YES"

while play == "YES":

    menu()

    choice = int(input("Enter your choice from above in number here: "))

    num1 = int(input("Enter your number here: "))
    num2 = int(input("Enter your number here: "))

    if choice == 1:
        print(f"Your answer is: {add(num1,num2)}")

    elif choice == 2:
        print(f"Your answer is: {subs(num1,num2)}")

    elif choice == 3:
        print(f"Your answer is: {multi(num1,num2)}")

    elif choice == 4:
        print(f"Your answer is: {divide(num1,num2)}")

    else:
        print("Invalide choice")

    count += 1

    play = input("Wanna play again? Type Yes or No: ").upper()

    while play != "NO" and play != "YES":
        print("Please only type Yes or No")
        play = input("Wanna play again? Type Yes or No: ").upper()
        
        if play == "NO":
            break

print(f"You used the calculator for {count} times")
print("Thank you for using calculator")