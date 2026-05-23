import Graph

devices = []
temperatures = []

print("SENSOR DATA VISUALIZATION")

count = int(input("How many devices?: "))

for i in range(count):

    name = input("\nEnter device name: ")

    temp = float(input("Enter temperature: "))

    devices.append(name)

    temperatures.append(temp)

print("\nGenerating graph...")

Graph.show_graph(devices, temperatures)5