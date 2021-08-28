# colab에서 해야 그래프 볼수있음


import matplotlib.pyplot as plt
import numpy as np


# 주피터 노트북을 사용하는 경우 노트북 내부에 그림 표시
# %matplotlib.pyplot inline


# 점 그래프
x_data = np.random.rand(100)
y_data = np.random.rand(100)

plt.title('scatter plot')
plt.grid()
plt.scatter(x_data, y_data, color='b', marker='o')
plt.show



# 선그래프
x = [x for x in range(-5,5)]
y = [y*y for y in range(-5,5)]

plt.title("line plot")
plt.grid()
plt.plot(x,y,color="b")
plt.show()