def check_device(device):

    print("\n DEVICE REPORT")

    print(f"Device Name : {device['name']}")
    print(f"Battery     : {device['battery']}%")
    print(f"Temperature : {device['temperature']}°C")

    if device["battery"] < 20:
        print("Low Battery")

    if device["temperature"] > 40:
        print("High Temperature Alert")

    if device["battery"] >= 20 and device["temperature"] <= 40:
        print("Device Status Normal")