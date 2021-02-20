import numpy as np
from matplotlib import pyplot as plt


def neville_point(x_data, y_data, x_0):
    """
    Interpolates around a point using Neville's method.

    :param x_data: numpy.ndarray of x values
    :param y_data: numpy.ndarray of y values
    :param x_0: x value to interpolate
    :return:
        :returns y_fit:  interpolated y value
        :returns Q: Coefficient matrix
    """
    n = x_data.size
    # Initialising coeff matrix
    Q = np.zeros((n, n - 1))
    Q = np.concatenate((y_data[:, None], Q), axis=1)  # Inserting 'y_data' as first column
    # Building coeff matrix:
    for i in range(1, n):
        for j in range(1, i + 1):
            Q[i, j] = ((x_0 - x_data[i - j]) * Q[i, j - 1] -
                       (x_0 - x_data[i]) * Q[i - 1, j - 1]) / (x_data[i] - x_data[i - j])

    y_fit = Q[n - 1, n - 1]

    return (y_fit, Q)


def neville(x_data, y_data, x_arr):
    """
        Interpolates an entire array using Neville's method.

        :param x_data: numpy.ndarray of x values
        :param y_data: numpy.ndarray of y values
        :param x_0: numpy.ndarray of x values to interpolate
        :return:
            :y_fit:  numpy.ndarray of interpolated y values
            :Q_arr: Array of coefficient matrices
    """

    n = x_arr.size
    Q_arr = np.ndarray((x_data.size, y_data.size, n))
    y_fit = np.ndarray(n)

    for i in range(n):
        y, Q = neville_point(x_data, y_data, x_arr[i])
        y_fit[i] = y
        Q_arr[:, :, i] = Q  # Adding the coeff matrix to an array of coeff matrices

    return y_fit, Q_arr


def plot_and_test(x_data, y_data, index=0):
    x_arr = np.linspace(x_data[0] - 0.25, x_data[len(x_data) - 1] + 0.25, 100)
    y_fit, Q_arr = neville(x_data, y_data, x_arr)

    plt.figure(figsize=(8, 3))
    plt.grid()
    plt.plot(x_arr, y_fit, "--", label="Fit", color=(0.9765625, 0.2265625, 0.4765625, 1), linewidth=3)
    plt.plot(x_data, y_data, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
    plt.legend()
    plt.savefig(f"plots/test{str(index)}.eps", format="eps")
    plt.show()

def plot(x_data, y_data, index=0):
    plt.figure(figsize=(8, 3))
    plt.grid()
    plt.plot(x_data, y_data, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
    plt.savefig(f"plots/plot{str(index)}.eps", format="eps")
    plt.show()
