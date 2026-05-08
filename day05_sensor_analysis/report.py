def generate_report(avg, highest, lowest, status):

    print("\n===== SENSOR REPORT =====")

    print(f"Average Temperature : {avg:.2f}°C")
    print(f"Highest Temperature : {highest}°C")
    print(f"Lowest Temperature  : {lowest}°C")
    print(f"System Status       : {status}")