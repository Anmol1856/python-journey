import devices
import monitoring

print("=== Smart Device Inventory System ===")

name = input("Enter device name: ")

battery = int(input("Enter battery percentage: "))

temperature = float(input("Enter temperature: "))

my_device = devices.create_device(name, battery, temperature)

monitoring.check_device(my_device)