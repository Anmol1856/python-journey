import pie


devices = []
usages = []


print(" PIE CHART VISUALIZATION ")


count = int(input("How many devices?: "))


for i in range(count):

    name = input("\nEnter device name: ")

    usage = float(input("Enter usage percentage: "))

    devices.append(name)

    usages.append(usage)


print("\nGenerating pie chart...")


pie.show_chart(devices, usages)