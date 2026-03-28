import sensor
import controller
import alert

while True:
    print("\n Smart Temperature System ")

    temp = sensor.read_temperature()
    status = controller.control_system(temp)
    alert.alert_system(status)

    choice = input("Continue? (y/n): ")
    if choice.lower() != "y":
        print("System shutting down")
        break