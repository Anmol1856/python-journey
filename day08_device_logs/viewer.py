def view_logs():

    print("\n-DEVICE LOGS \n")

    try:

       with open("day08_device_logs/device_logs.txt", "r") as file:

            logs = file.read()

            if logs:
                print(logs)
            else:
                print("No logs found")

    except FileNotFoundError:

        print("Log file not found")