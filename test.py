import numpy as np
from main import plot_and_test

x_data1 = np.array([0.25, 0.5, 0.75, 1, 1.25])
y_data1 = np.array([0.5, 0.75, 0.6, 0.8, 1.1])
plot_and_test(x_data1, y_data1, 1)

# _________________________________________________

x_data2 = np.array([1.6, 2, 2.5, 3.2, 4, 4.5])
y_data2 = np.array([2, 8, 14, 15, 8, 2])
plot_and_test(x_data2, y_data2, 2)

# _________________________________________________

x_data3 = np.array([2, 2.75, 4])
y_data3 = np.array([1 / 2, 4 / 11, 1 / 4])
plot_and_test(x_data3, y_data3, 3)

# _________________________________________________

x_data4 = np.array([2, 3, 4, 7, 13])
y_data4 = np.array([10, -1, 2, 3, -3])
plot_and_test(x_data4, y_data4, 4)

# _________________________________________________

x_data5 = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
y_data5 = np.array([31.5, 19.8, 10.9, 4.64, 1.09, 0, 0.89, 3.04, 5.49, 7.04, 6.25])
plot_and_test(x_data5, y_data5, 5)

# _________________________________________________

x_data6 = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])
y_data6 = np.array([0.0384, 0.0588, 0.1, 0.2, 0.5, 1, 0.5, 0.2, 0.1, 0.0855, 0.0384])
plot_and_test(x_data6, y_data6, 6)
