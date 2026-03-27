# temperature.py

print("\n Temperature Controller")

try:
    temp = float(input("Enter temperature: "))

    if temp > 30:
        print("Fan ON ")
    elif temp < 15:
        print("Heater ON ")
    else:
        print("System Normal")

except:
    print("Invalid temperature input!")