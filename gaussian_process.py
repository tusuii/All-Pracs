import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

X = np.array([[-1, 0], [-0.5, 0.5], [0, 1], [1, 0]])
y = np.array([-1, 0.5, 2, 0])

kernel = RBF(length_scale=1.0)

model = GaussianProcessRegressor(kernel=kernel)

model.fit(X, y)

new_input = np.array([[-0.2, 0.2]])
prediction, std_dev = model.predict(new_input, return_std=True)

print("Prediction: ", prediction[0])
print("Standard deviation: ", std_dev[0])

x_plot = np.linspace(-1.5, 1.5, 100)
X_plot = np.vstack((x_plot, np.zeros(100))).T
y_plot, std_plot = model.predict(X_plot, return_std=True)

plt.plot(x_plot, y_plot)
plt.fill_between(x_plot, y_plot - std_plot, y_plot + std_plot, alpha=0.2)
plt.scatter(X[:, 0], y, c='r', marker='x')
plt.show()
