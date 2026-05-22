devices = []

def add_device():

    name = input("Enter device name: ")

    battery = int(input("Enter battery percentage: "))

    temperature = float(input("Enter temperature: "))

    device = {
        "name": name,
        "battery": battery,
        "temperature": temperature
    }

    devices.append(device)

    print(" Device added successfully")


def get_devices():

    return devices