def analyze_temperature(temps):

    avg = sum(temps) / len(temps)

    highest = max(temps)
    lowest = min(temps)

    if avg > 35:
        status = "HIGH TEMPERATURE"

    elif avg < 15:
        status = "LOW TEMPERATURE"

    else:
        status = "NORMAL"

    return avg, highest, lowest, status