import numpy as np
from matplotlib import pyplot as plt
from main import neville, lagrange


def plot(x_data, y_data, index=0):
    """
        Generates an 'eps' file of the data points.

        :param x_data: numpy.ndarray of x values
        :param y_data: numpy.ndarray of y values
        :param index: index of the plot
    """

    plt.figure(figsize=(8, 3))
    plt.grid()
    plt.plot(x_data, y_data, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
    plt.savefig(f"plots/plot/{str(index)}.eps", format="eps")
    plt.show()


def plot_and_test(x_data, y_data, index=0):
    """
        Generates an 'eps' file of the data points and the Neville interpolation polynomial.

        :param x_data: numpy.ndarray of x values
        :param y_data: numpy.ndarray of y values
        :param index: index of the plot
    """

    x_arr = np.linspace(x_data[0] - 0.25, x_data[len(x_data) - 1] + 0.25, 10000)
    y_fit, Q_arr = neville(x_data, y_data, x_arr)

    plt.figure(figsize=(8, 3))
    plt.grid()
    plt.plot(x_arr, y_fit, "--", label="Fit", color=(0.9765625, 0.2265625, 0.4765625, 1), linewidth=3)
    plt.plot(x_data, y_data, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
    plt.legend()
    plt.savefig(f"plots/test/{str(index)}.eps", format="eps")
    plt.show()


def plot_and_compare(x_data, y_data, index=0):
    """
        Generates an 'eps' file of the data points and compares
        the Neville interpolation polynomial with Lagrange and np.polyfit.

        :param x_data: numpy.ndarray of x values
        :param y_data: numpy.ndarray of y values
        :param index: index of the plot
    """

    x_arr = np.linspace(x_data[0] - 0.25, x_data[len(x_data) - 1] + 0.25, 10000)
    y_fit_neville, Q_arr = neville(x_data, y_data, x_arr)
    P = np.polyfit(x_data, y_data, x_data.size - 1)
    y_fit_polyfit = np.polyval(P, x_arr)
    y_fit_lagrange = lagrange(x_data, y_data, x_arr)

    plt.figure(figsize=(8, 3))
    plt.grid()
    plt.plot(x_arr, y_fit_neville, "--", label="Neville", color=(0.9765625, 0.2265625, 0.4765625, 1), linewidth=3)
    plt.plot(x_arr, y_fit_polyfit, label="np.polyfit")
    plt.plot(x_arr, y_fit_lagrange, label="Lagrange")
    plt.plot(x_data, y_data, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
    plt.legend()
    plt.show()
