# main.py

while True:
    print("\n Day2_Programs ")
    print("1. Calculator")
    print("2. Login System")
    print("3. Temperature Controller")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        import calculator
    elif choice == "2":
        import login
    elif choice == "3":
        import temperature
    elif choice == "0":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again!")