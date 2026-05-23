import matplotlib.pyplot as plt


def show_graph(devices, temperatures):

    plt.bar(devices, temperatures)

    plt.title("Sensor Temperature Report")

    plt.xlabel("Devices")

    plt.ylabel("Temperature")

    plt.show()