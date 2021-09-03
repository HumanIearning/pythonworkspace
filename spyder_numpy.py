# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## spyder file임
## numpy 공부
## spyder에선 %reset -f 를 하면 변수선언했던것들을 전부 초기화함

import numpy as np

# numpy의 자료형 array는 행렬 계산을함 e.g) [3,4] * [6,7] == [18, 28]
# 행렬곱은 np.dot(a,b)

# array는 행렬의 크기가 다른경우에도 사칙연산(dot product는 안됨)이 가능한데
# e.g)[[1,2],[3,4]] + [5,6] -> [[1,2],[3,4]] + [[5,6],[5,6]]
# 이를 broadcast라고 칭함

# iterator 라고 반복하는게 있는데 뭔지 잘 모르겟음
# it = np.nditer(a, flags=['multi_index'], op_flags=['readwrite'])
# while not it.finished:
#     idx = it.multi_index
#     print(a[idx])
#     it.iternext()
    
# loaded_data = np.loadtxt('./data-01.csv', delimeter=',', dtype='float32')
# data-01.csv에 담긴 데이터를 delimeter 값으로 split해서 array로 갖고옴
# 머신러닝 코드에서 입력데이터와 정답데이터를 분리하는 프로그래밍 기법


# a = np.array([[10, 20, 30],[1., 2., 3.]])  # 리스트(# tuple도 됨)를 numpy의 array로 만듬
# a

# a.shape # a의 사이즈를 반환
# a.ndim # a의 차원을 반환
# a.dtype # a에 있는 데이터들의 자료형을 반환
# a.itemsize # a에 있는 데이터가 몇바이트의 메모리를 차지하는지 반환
# a.size # a에 값이 몇개가 들어갔는지 반환
# type(a) # numpy.ndarray     N-dimensional array
# a[2] = 30.1 # a에 float자료형인 30.1을 넣음
# a # 그런데? a에는 그대로 30만 있음
# a = a.astype('float64')
# a[2] = 30.1
# a
# a.dtype
# b = np.array([10, 20., 30.])
# b # 10도 10. 으로 바뀜
# np.shape([[1,2,3,4],[10,20,30,40]])
# np.size([[1,2,3,4],[10,20,30,1],[1,2,3,1]])

# a = np.eye(6,4,0) # 단위행렬 만들어줌
# a

# a = np.array([1.1,2.2,3.3,4.4],'int32') # float여도 소숫점 날리고 int로 바꿈
# y = a/2 # 자동으로 y는 float형 됨

# # int32 vs int64
# # 2147483647
# # 9223372036854775807

# x = np.array([0])
# x[0] = 2147483647   
# x[0] += 1   # overflow
# x.dtype
# x

# x = np.array([0],'int64')
# x[0] = 2147483647
# x[0] += 1   # workwell
# x.dtype
# x

# x = np.array([0],'int64')
# x[0] = 9223372036854775807
# x[0] += 1  # overflow
# x.dtype
# x

# a = np.array([10,20,30]) 
# a = np.array([1,2,'arr'])
# 2*a # 오류발생

# a = np.array([ [ [1],[2],[3],[ 11 ] ],
#                [ [4],[5],[6],[44] ] ])

# a = np.array([1 + 1j, 2 + 2j])
# a.dtype
# a = np.array([1,2,3],'complex')
# a.dtype

# a = np.array([1,2,3,4])
# a = np.insert(a,0,5) # array, 인덱스, 값

# a = np.delete(a,0) # array, 인덱스
# a





## array 자동생성
# a = np.zeros([2,3]) # 매개변수 크기의 영행렬을 만들어줌 # tuple도 됨
# a
# a = np.ones((2,3)) # 매개변수 크기의 1행렬을 만들어줌
# a
# a = np.linspace(0,1,4) # 0부터 1까지 4개로 쪼개서 array를 만들어줌
# a
# a = np.logspace(0,5,8) 
# a 
# array = np.arange(10.1) # 매개변수 미만의 정수 리스트를 만듬  # arrange 오타난거아님 arange 맞음
# array
# np.random.randint(1,100,5) # 1~100 사이의 5개의 무작위정수 생성
# np.random.rand(a,b) # 0부터 1까지의 임의의실수로 a by b 행렬을 만듬 
# np.random.randn(a,b) # 0부터 1까지의 표준 정규분포를 이루는 임의의실수로 a by b 행렬을 만듬 
# np.random.normal(평균, 표준편차, 행렬크기) # 평균과 표준편차를 지정할수있음
# np.random.seed(0) # random함수의 seed를 고정해 random 함수로 나오는 값들이 동일해진다

## array는 element-wise operation 을 사용함
## 즉 array끼리 연산식 각 원소들끼리 게산함
## array 연산
# a = np.array([1,2,3])
# b = np.array([4.,5.,6.])
# c = b + a   # np.add(b,a)
# c = b - a   # np.subtract(b,a)
# c = c * 4   # np.multiply(c,4)
# c = c / 4   # np.divide(c,4)
# c = c**4    
# # np.divmode(a,b) # 몫array와 나머지array를 각각 반환
# # c = np.exp(a)  # 자연상수e의 a제곱 한것을 반환
# np.log(a) # a의 e에 대한 log값을 반환   # e^np.log(a) = a 의 log형
# # np.sqrt([4, -1, -3+4J]) # 허수로 반환
# # np.sqrt([4, -1, np.inf]) # nan, inf로 반환
# a += b # int = int + float 는 되지만 int += float 는 안됨 float += int는됨
# a = b + a

# logic = b >= 5 # bool값들이 리스트로 저장됨
# logic




## array 통계 함수
# a = np.array([1,2,3,4,5,6])
# np.mean(a) # 평균값 반환
# a.mean()

# np.average(a,weights=[1, 1, 0, 2, 0, 3]) # 평균값 구할때 가중치 부여가능

# np.median(a) # 중앙값 반환

# np.cumsum(a)  # cumulative sum # 한칸 전의 원소를 더한값을 현재 원소에 저장함

# np.cov(a)
# np.std(a)
# np.var(a)




## array 정렬 함수
# x = np.array([10 ,15, 0, 5, 20])
# y = np.array([-1, -5, 6, 7])
# x.sum() # 원소들의합
# x.min()  # 최솟값
# x.argmin() # 최솟값이 위치한 인덱스
# x.max(a,axis=1)  # 행 기준인지 열 기준인지 정할수있음 axis가 0이면 열기준 
# x.argmax()
# x.ptp # peak to peak # max - min
# x.sort()  # 바로 업데이트됨
# z = np.sort(x) # x는 업데이트 안됨
# x.argsort # x의 정렬되기 전 값들의 인덱스
# x.searchsorted(x,y) # y의 각원소들이 x의 어디 인덱스에 들어가야 정렬이 유지 되는지 알려줌 
# # x가 정렬 되어있지 않을경우 값이 다르게 나옴




## array 수정 함수
# a = np.array([[5,10,15,20,25]])
# b = np.array([[-5,-10,-15,-20,-25]])

# a = a.reshape(2,3) # a의 size와 2*3이 일치하지않을경우 오류
# c = np.linspace(1,10,6).reshape(2,3)
# c = c.astype('int64')

# np.repeat(c, [1, 2], axis = 0) # 아래로 c[0][*] 는 1번반복 c[1][*]는 2번반복 
# np.repeat(c, [1, 2, 3], axis = 1) # 옆으로 c[*][0]은 1번 반복 c[*][1]는 2번반복 c[*][2]는 3번반복

# array서로 연결해주기 list의 append 같은 느
# c = np.concatenate((a,b), axis = 1) # 매개변수로 들어갈 array들을 tuple로 묶어서 보내줘야함 # a,b를 연결해줌 

# c = np.hstack((a,b)) # concatenate axis = 1
# c = np.vstack((a,b)) # concatenate axis = 0

# c = np.hsplit(c,5) # horizon split 세로로 자름
# c = np.vsplit(c,2) # vertical split 가로로 자름
# # array들을 원소로갖는 list형태의 데이터로 반환

# c = np.transpose(c) # 전치

# c = np.ravel(c)
# c.ravel()         # 2차원 데이터를 1차원으로 만들어줌
# c.ravel(order = 'c') # C-style : row-major
# c.ravel(order = 'f') # Fortran-style : column-major
# c = c.reshape(-1) 
# c.flatten()

# c = np.array([[[[1,2,3]]],[[[4,5,6]]],[[[7,8,9]]],[[[10,11,12]]]])
# c.shape
# c.squeeze()
# c.squeeze() # c.shape을 쳤을때 1을 지워줌
# # 즉 있으나 마나 한 차원들을 줄여줌
# # eg) [ [[1,2]],
# #       [[3,4]]]      -> [[1,2],[3,4]]

# c = c.squeeze()
# c = c[:,np.newaxis]

# A1 = np.array([1,2,3])
# B1 = np.array([4,5,6])
# A2 = A1[:,np.newaxis]
# B2 = B1[:,np.newaxis]
# C = np.concatenate((A2,B2),axis = 1)

# np.vstack((A1,B1)).transpose()

# np.hstack((A1,B1)).reshape((2,3)).transpose()




## Array 복사,보기
# A = np.array([1,2,3,4,5,6])
# B = A      # 메모리주소 공유
# B.base is A     # False
# B[0] = 99
# ## shallow
# B = A.view()
# B is A
# B.base is A     # True
# B.flags.owndata # False
# B[0] = 10
# B.shape = (2,3)
# B[0][1] = 10
# ## deep
# B = A.copy()
# B.base is       # False
# B is A          # Fasle
# B.flags.owndata # True  # 갖고있는 데이터가 나의 데이터인지
# id(A)
# id(B)
# B[0] = 9




## 논리함수
# a = np.array([10, 0, 20])
# a.all()  # a안에 있는 값이 모두 참인지 
# a.any()  # a안에 있는 값 중 하나라도 참인지
# a.nonzero()  # a에서 0을 뺀 값을 튜플로반환 
# b = a.nonzero()
# b = np.array(b).squeeze()
# np.where(a > 0)   # 조건에 맞는 값의 인덱스를 알려줌
# np.where(a == 0)
# np.where(a < 0)


## numpy 의 array 도 인덱싱과 슬라이싱 가능
a = np.array([100,
              200,
              300.,
              400,
              500])
a[[2, 3]]
a[1:3]
a[::2]
a[::-1] 
a[::-2]
a2 = np.linspace(1,6,6).reshape(2,3)
a2[:,:]

## matrix
## matrix는 2차원
# m = np.matrix([1,2,3,4]) # 3차원 생성시 오류
## inverse 등과 같은 함수들이 원래 matrix만 지원했었는데 이제 array도 지원을해서 
## matrix는 거의 쓰지않음



 








