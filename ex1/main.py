import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return 10*x + 2

x = np.linspace(0, 10, 100)
y = f(x) + np.random.normal(0, 4, 100)
x = x + np.random.normal(0, 4, 100)

x_normalized = (x - np.mean(x)) / np.std(x)
y_normalized = (y - np.mean(y)) / np.std(y)

cov_mat = np.cov(x_normalized, y_normalized)
eigvals, eigvecs = np.linalg.eig(cov_mat)
sorted_eigvals = np.argsort(eigvals)[::-1]

k = 1
selected_eigvecs = eigvecs[:, sorted_eigvals[:k]]
x_redused = np.dot(selected_eigvecs.T, np.array([x_normalized, y_normalized]))

plt.figure(figsize=(12,6))
plt.subplot(121)
plt.scatter(x, y)
plt.subplot(122)
plt.scatter(x_redused, np.zeros(x_redused.shape))
plt.show()