def show_warning(status):

    print("\n BATTERY STATUS")

    if status == "Battery Full":
        print(" Battery level is high")

    elif status == "Battery Normal":
        print(" Battery working normally")

    elif status == "Low Battery":
        print(" Please charge soon")

    elif status == "Critical Battery":
        print(" Connect charger immediately")

    else:
        print(" System shutting down")