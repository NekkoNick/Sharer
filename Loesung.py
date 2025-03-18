def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Division durch Null ist nicht erlaubt!"

def main():
    while True:
        print("Wähle eine Operation:")
        print("1. Addition")
        print("2. Subtraktion")
        print("3. Multiplikation")
        print("4. Division")
        print("5. Beenden")
        
        choice = input("Gib deine Wahl ein (1/2/3/4/5): ")
        
        if choice == '5':
            print("Programm beendet.")
            break
        
        num1 = float(input("Gib die erste Zahl ein: "))
        num2 = float(input("Gib die zweite Zahl ein: "))
        
        if choice == '1':
            print(f"Ergebnis: {add(num1, num2)}")
        elif choice == '2':
            print(f"Ergebnis: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Ergebnis: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Ergebnis: {divide(num1, num2)}")
        else:
            print("Ungültige Eingabe. Bitte versuche es erneut.")

if __name__ == "__main__":
    main()
