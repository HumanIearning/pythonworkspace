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
plt.imshow(M_hz)     # 값을 0~1 사이나 1~255 사이로 아무거나 해도 알아서 imshow가 알아서 맞춰줌

# checkerboard image
M = np.zeros((5,5,3))
plt.imshow(M)

# turn into white
# M[:,:,:]=0.1 
M[:]=1
plt.imshow(M)

# turn into black
M[:]=0
plt.imshow(M)

# checkerboard
M[0::2,0::2,:]=1
plt.imshow(M)
M[1::2,1::2,:]=1
plt.imshow(M)

# copy
N = M.copy()
idx = np.where(N==1)
N[idx] = 0.5
plt.imshow(N)

# change black to white
idx = np.where(N<0.1)
N[idx]=1
plt.imshow(N)

# copy again
N = M.copy()
plt.imshow(N)

# color inverse
idx_w = np.where(N==1)
idx_b = np.where(N==0)
N[idx_w] = 0
N[idx_b] = 1
plt.imshow(N)

# change white to green
idx1 = np.where(N==1)
N[idx1[0],idx1[1],0]=0
N[idx1[0],idx1[1],2]=0
plt.imshow(N)

# change black to red
flag_r = (N[:,:,0]==0)
flag_g = (N[:,:,1]==0)
flag_b = (N[:,:,2]==0)

flag_blk = flag_r and flag_g and flag_b
idx_blk = np.where(flag_blk)
N[idx_blk[0],idx_blk[1],0] = 1
plt.imshow(N)

# another way
N = M.copy()

N_sum = np.sum(N,axis=2)
idx_blk = np.where(N_sum == 0)
N[idx_blk[0],idx_blk[1],0]=1
plt.imshow(N)

# change diagonal to green
np.fill_diagonal(N[:,:,0],0)
np.fill_diagonal(N[:,:,1],1)
np.fill_diagonal(N[:,:,2],0)










