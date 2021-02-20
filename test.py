import numpy as np
from matplotlib import pyplot as plt
from main import neville

x_data1 = np.array([0.25, 0.5, 0.75, 1, 1.25])
y_data1 = np.array([0.5, 0.75, 0.6, 0.8, 1.1])
x_arr1 = np.linspace(0.15, 1.5, 100)
y_fit1, Q_arr1 = neville(x_data1, y_data1, x_arr1)
plt.figure()
plt.grid()
plt.plot(x_data1, y_data1, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
plt.plot(x_arr1, y_fit1, "--", label="Fit", color=(0.9765625, 0.2265625, 0.4765625, 1), linewidth=3)
plt.legend()
plt.show()

# _________________________________________________

x_data2 = np.array([1.6, 2, 2.5, 3.2, 4, 4.5])
y_data2 = np.array([2, 8, 14, 15, 8, 2])
x_arr2 = np.linspace(1.5, 4.9, 100)
y_fit2, Q_arr2 = neville(x_data2, y_data2, x_arr2)
plt.figure()
plt.grid()
plt.plot(x_data2, y_data2, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
plt.plot(x_arr2, y_fit2, "--", label="Fit", color=(0.9765625, 0.2265625, 0.4765625, 1), linewidth=3)
plt.legend()
plt.show()

# _________________________________________________

x_data3 = np.array([2, 2.75, 4])
y_data3 = np.array([1 / 2, 4 / 11, 1 / 4])
x_arr3 = np.linspace(1.9, 4.9, 100)
y_fit3, Q_arr3 = neville(x_data3, y_data3, x_arr3)
plt.figure()
plt.grid()
plt.plot(x_data3, y_data3, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
plt.plot(x_arr3, y_fit3, "--", label="Fit", color=(0.9765625, 0.2265625, 0.4765625, 1), linewidth=3)
plt.legend()
plt.show()

# _________________________________________________

x_data4 = np.array([2, 3, 4, 7, 13])
y_data4 = np.array([10, -1, 2, 3, -3])
x_arr4 = np.linspace(1.9, 13.9, 100)
y_fit4, Q_arr4 = neville(x_data4, y_data4, x_arr4)
plt.figure()
plt.grid()
plt.plot(x_data4, y_data4, "o", label="Data", color=(0, 0.52734375, 0.94921875, 1))
plt.plot(x_arr4, y_fit4, "--", label="Fit", color=(0.9765625, 0.2265625, 0.4765625, 1), linewidth=3)
plt.legend()
plt.show()
