def battery_status(level):

    if level > 80:
        return "Battery Full"

    elif level > 40:
        return "Battery Normal"

    elif level > 20:
        return "Low Battery"

    elif level > 0:
        return "Critical Battery"

    else:
        return "System Shutdown"