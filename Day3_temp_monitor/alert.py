def alert_system(status):
    if status == "DANGER":
        print(" ALERT! Temperature too high!")
    elif status == "FAN ON":
        print(" Cooling system activated")
    elif status == "HEATER ON":
        print(" Heating system activated")
    elif status == "NORMAL":
        print(" System stable")
    else:
        print("No valid data")