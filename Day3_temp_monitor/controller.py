def control_system(temp):
    if temp is None:
        return "No Data"

    if temp > 40:
        return "DANGER"
    elif temp > 30:
        return "FAN ON"
    elif temp < 10:
        return "HEATER ON"
    else:
        return "NORMAL"