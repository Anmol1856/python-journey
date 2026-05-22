def show_devices(devices):

    print("\n DEVICE DASHBOARD ")
 
    if len(devices) == 0:
        print("No devices found")
        return

    for i, device in enumerate(devices, start=1):

        print(f"\nDevice {i}")

        print(f"Name        : {device['name']}")
        print(f"Battery     : {device['battery']}%")
        print(f"Temperature : {device['temperature']}°C")

        if device["battery"] < 20:
            print("⚠ Low Battery")

        if device["temperature"] > 40:
            print(" High Temperature")