# 행렬 계산 -> numpy
# 그래프 그리기 -> matplotlib
# Function < Module < Package < Library     # package 랑 library는 크게 구별안함

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

M = np.zeros((2,3))
M = np.ones((2,3))

# image size variables
Height = 4
Width = 5
Depth = 3

# black
M = np.ones((Height,Width,Depth))*0

M = np.zeros((Height,Width,Depth))
plt.imshow(M)
plt.grid()

# red
M[:,:,0]=255
plt.imshow(M)
plt.grid()

# green
M = np.zeros((Height,Width,Depth))
M[:,:,1] = 255
plt.imshow(M)
plt.grid()

# blue
M = np.zeros((Height,Width,Depth))
M[:,:,2] = 255
plt.imshow(M)
plt.grid()

# white
M = np.ones((Height,Width,Depth))*255

M = np.zeros((Height,Width,Depth))
M[:,:,:] = 255
plt.imshow(M)
plt.grid()

# top-left pixel to white
M[0,0,:]=255
plt.imshow(M)
plt.grid(False)

# top-lef pixel to green
M[0,0,0]=0
M[0,0,1]=255
M[0,0,2]=0
plt.imshow(M)

# top-lef pixel to blue
M[0,0,0]=0
M[0,0,1]=0
M[0,0,2]=255
plt.imshow(M)

# back to black
M[:,:,:]=0
plt.imshow(M)

# first column to green
M[:,0,1]=255
plt.imshow(M)

# second column from last to blue
M[:,3,2]=255
plt.imshow(M)

# third row to yellow
M[2,:,0]=255
M[2,:,1]=255
M[2,:,2]=0
plt.imshow(M)

# extend in vertical direction
M_vt = np.vstack([M,M])
plt.imshow(M_vt)

# extend in horizontal direction
M_hz = np.hstack([M,M])
plt.imshow(M_hz)

# dim
M_hz = (M_hz/255)*0.5
plt.imshow(M_hz)





























