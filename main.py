import numpy as np


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


def lagrange_point(x_data, y_data, x0):
    """
       Interpolates around a point using Lagrange's method.

       :param x_data: numpy.ndarray of x values
       :param y_data: numpy.ndarray of y values
       :param x_0: x value to interpolate
       :returns y_fit:  interpolated y value
    """

    n = x_data.size
    y_fit = 0

    for i in range(0, n):
        p = y_data[i]
        for j in range(0, n):
            if i != j:
                p = p * (x0 - x_data[j]) / (x_data[i] - x_data[j])
        y_fit += p

    return y_fit


def lagrange(x_data, y_data, x_arr):
    """
        Interpolates an entire array using Lagrange's method.

        :param x_data: numpy.ndarray of x values
        :param y_data: numpy.ndarray of y values
        :param x_0: numpy.ndarray of x values to interpolate
        :return y_fit:  numpy.ndarray of interpolated y values
    """

    n = x_arr.size
    y_fit = np.ndarray(n)

    for i in range(n):
        y = lagrange_point(x_data, y_data, x_arr[i])
        y_fit[i] = y

    return y_fit
