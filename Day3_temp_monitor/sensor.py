def read_temperature():
    try:
        temp = float(input("Enter temperature: "))
        return temp
    except:
        print("Invalid input")
        return None