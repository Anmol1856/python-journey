import logger
import viewer

while True:

    print("\n-SMART DEVICE LOG SYSTEM ")

    print("1. Save Device Log")
    print("2. View Logs")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        name = input("Enter device name: ")

        battery = int(input("Enter battery percentage: "))

        temperature = float(input("Enter temperature: "))

        logger.save_log(name, battery, temperature)

    elif choice == "2":

        viewer.view_logs()

    elif choice == "3":

        print("Exiting system...")
        break

    else:

        print("Invalid choice")