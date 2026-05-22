import manager
import display

while True:

    print("\n SMART DEVICE DASHBOARD ")

    print("1. Add Device")
    print("2. View Devices")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        manager.add_device()

    elif choice == "2":

        devices = manager.get_devices()

        display.show_devices(devices)

    elif choice == "3":

        print("Exiting dashboard...")
        break

    else:

        print("Invalid choice")