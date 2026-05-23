import graph


times = []
temperatures = []


print(" LINE GRAPH ANALYSIS ")


count = int(input("How many readings?: "))


for i in range(count):

    time = input("\nEnter time: ")

    temp = float(input("Enter temperature: "))

    times.append(time)

    temperatures.append(temp)


print("\nGenerating line graph...")


graph.show_graph(times, temperatures)