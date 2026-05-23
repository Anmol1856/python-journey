import graph


devices = []
temperatures = []


print(" MULTI GRAPH DASHBOARD ")


count = int(input("How many devices?: "))


for i in range(count):

    name = input("\nEnter device name: ")

    temp = float(input("Enter temperature: "))

    devices.append(name)

    temperatures.append(temp)


print("\nGenerating dashboard...")


graph.show_dashboard(devices, temperatures)