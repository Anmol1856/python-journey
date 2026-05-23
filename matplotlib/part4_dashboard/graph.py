import matplotlib.pyplot as plt


def show_dashboard(devices, temperatures):

    plt.figure(figsize=(10, 5))


    # BAR GRAPH

    plt.subplot(1, 2, 1)

    plt.bar(devices, temperatures)

    plt.title("Bar Graph")


    # LINE GRAPH

    plt.subplot(1, 2, 2)

    plt.plot(devices, temperatures, marker="o")

    plt.title("Line Graph")


    plt.tight_layout()

    plt.show()