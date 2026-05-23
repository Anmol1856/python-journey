def save_log(name, battery, temperature):

    with open("day08_device_logs/device_logs.txt", "a") as file:

        file.write(
            f"Device: {name}, Battery: {battery}%, Temperature: {temperature} Degree Celsius\n"
        )

    print("Log saved successfully")