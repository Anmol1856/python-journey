import battery
import warning

while True:

    print("\n===== Battery Monitoring System =====")

    try:
        level = int(input("Enter battery percentage (0-100): "))

        if level < 0 or level > 100:
            print("Invalid battery percentage")
            continue

        status = battery.battery_status(level)

        warning.show_warning(status)

    except:
        print("Invalid input")

    choice = input("\nCheck again? (y/n): ")

    if choice.lower() != "y":
        print("System stopped")
        break