import matplotlib.pyplot as plt


def show_chart(devices, usages):

    plt.pie(usages, labels=devices, autopct="%1.1f%%")

    plt.title("Device Usage Distribution")

    plt.show()