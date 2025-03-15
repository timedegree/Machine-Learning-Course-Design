import numpy as np
import matplotlib.pyplot as plt

# ax + by + cz = 0
a, b, c = np.random.randint(0, 10, size=3)
print(a, b, c)

origin_x = np.linspace(-10, 10, 200)
origin_y = np.linspace(-10, 10, 200)
origin_z = (a * origin_x + b * origin_y) / (-c + 1e-8) if c != 0 else np.zeros(200)

#print(origin_z)

x = origin_x + np.random.normal(0, 1, 200)
y = origin_y + np.random.normal(0, 1, 200)
z = origin_z + np.random.normal(0, 1, 200)

plt.figure(figsize=(8,6))
plt.subplot(121, projection='3d')
plt.scatter(origin_x, origin_y, origin_z, c='blue')
plt.title("Original Data")
plt.subplot(122, projection='3d')
plt.scatter(x, y, z, c='red')
plt.title("Noise Data")
plt.show()