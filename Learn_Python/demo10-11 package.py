import numpy as np
import matplotlib.pyplot as plt
# 读取图片
n1 = plt.imread('google.png')
print(type(n1), n1)             # <type 'numpy.ndarray'> <numpy.ndarray object at 0x000002A2D7E4F5C8>
plt.imshow(n1)

# 编写一个灰度公式
n2 = np.array([0.2989, 0.5870, 0.1140])
x = np.dot(n1[...,:3], n2)
plt.imshow(x, cmap='gray')
plt.show()
