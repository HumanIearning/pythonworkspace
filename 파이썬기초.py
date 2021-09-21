# import this
# pep 8

##################################################################################

#파이썬에서 허수는 i가 아닌 j  eg)12.3+3j
# a = 1.5j
# b = 2j              ## -3+0j
# print(a * b)
# type()  자료형 확인
# a = int() 0생성 float() 0.0생성 complex() 0j생성 str() boll() False 생성 
# 무한은 inf ∞
# complex() 는 '1+3j' 이런식의 문자열이 들어와도 1+3j 로 바꿔줌
# bool() 빈문자열,리스트,튜플,딕셔너리 는 False
# c언어에서 하던 system()은 여기선 import os 하고 os.system() 이렇게 써줘야함
# 절대값은 abs()
# divmode(a,b)는 (몫,나머지) 를 반환
# print(type(True + True + True))  -> int형
# type(3) is type(3.1) ##type(3) is not type(3.1)
# 1 and 3 and 1000 -> 1000

# bin() 2진수로 바꿔줌
# x & y -> and  | -> or  ^ -> xor
# 110 << 2 -> 11000    111 >> 1 -> 11

# 변수.bit_length() -> 변수의 2진수 형태에서의 길이를 반환
# 복소수.conjugate() -> 복소수를 켤레복소수로 바꿔줌 3+3j -> 3-3j 
# 복소수.real() imag() 는 각각 실수부분,허수부분 반환

# 문자열안의 \ 는 파이썬이 "알아서" \\로 바꿔줌 터미널에서 확인가능   s = "nice\good"  s , print(s)
# 'I'm python'(X)   'I\'m python'(O)  큰따옴표도 동일
# 그래서 주소써줄때 path = 'C:\\python\\good'로 써야함

# a = input("input : ") input은 str로 받음
# dir() 현재있는 변수들 반환 globals() locals() 각각 전역, 지역변수들 반환
# del 변수이름 으로 변수 삭제 가능
# a == b -> a.__eq__(b)

# a ,b = 10, 20 -> 가능

# 변수, 함수이름을 만들때 파이썬에서 기본지원하는 함수랑 겹치지 않도록 만들기

##################################################################################

# list[a : b : c] a이상 b미만까지 c만큼 증가하면서 즉, [list[a], list[a+c],list[a+2c], list[a+3c], list[a+4c]] 반환
# list[-1] -> 끝에서의 0번쨰 뒤에서부터 인덱싱, 슬라이싱 할때는 -0시작이아니라 -1시작
# index가 list의 길이를 벗어난경우 eg) a= [1,2]  a[99] 오류발생

# 고차원 list의 경우 list[a][b:c]로 인덱싱과 슬라이싱 동시에 가능
# list = [ [1,2,3,4,5],
#          [11,12,13,14,15],
#          [21,22,23,24,25],
#          [31,32,33,34,35],
#          [41,42,43,44,45], ] 
# print(list[1:3][1][0])

# list1 + list2 -> 수학적으로 더해지는 것이아니라 append 됨
# list1 = [123, 456, 789]
# list2 = [[1,2,3], [4, 5, 6], [7, 8, 9]]
# print(list1 + list2)

# list * 3 -> 가능 문자열과 똑같음 
# list = [1,2,3]
# list *= 3
# print(list)

# list1 = list2 -> list1과 list2는 같은 메모리를 공유함 c에서의 포인터 생각하면됨
# list1[1]의 값 변경시 list[2]의 값도 똑같이 변경됨
# 메모리 공유안하려면 즉, c언어 처럼 되길 원한다면 list1 = list2.copy()

# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]
# list1.extend(list2) ## == list1 = list1 + list2
# list1.append(list2) ## == list1 = list1 + [list2]
# print(list1)

# list.remove(a) -> 맨 처음 나오는 a값을 없앰
# list = ['a','a','b','b','b','v','c']
# list.remove('a')
# print(list)
##
# a = ['a','b','c']
# list = ['a','b','c','d','c','d','fg','b',a]
# print(list)
# list.remove(a)
# print(list)
# remove()는 인덱스값은 못받음

# 인덱스값을 받으려면 pop()
# +pop은 반환하면서 삭제함

# 리스트를 빈리스트로 만드려면 clear()

# insert(a, b) -> a번째 인덱스에 b를 넣음
# a를 list의 길이보다 큰 값을 넣을경우 맨 마지막에 추가함
# list1 = [1, 2, 3, 4, 5]
# a = [1,2,3]
# list1.insert(0, a)
# print(list1)
# list.insert(1, 1) ## int값은 못넣음
# print(list1)

# index(a) -> a가 몇번째 인덱스인지 반환함 
# list = [1, 2, 3, 4, 5]
# print(list.index(4))

# count(a) -> a가 몇개 들었는지 반환
# list = [1, 2, 2, 3, 3 ,3, 4, 4, 4, 4]
# print(list.count(2))

# sort() -> 숫자순, 알파벳 순으로 나열함 bool은 False(0)가 앞 True(1) 가 뒤
# list = ['a', 'b', 'ab','aa']
# list.sort()
# print(list)
# list안에 숫자랑 문자가 둘다 있을경우 오류남 
# bool은 0,1 로 쳐서 bool과 숫자가 함께있을때는 sort 가능

# reverse() 는 뒤집음 
# list[-1: :-1]과 같음

##################################################################################

# set 자료형은 중복이 안됨
# set = {1, 2, 3, 4, 5 ,5, 1}
# print(set)
# set= set(list)와 같이 list를 set로 변환시 순서는 뒤죽박죽 됨

# b = set()
# b.add(10)
# print(b)
# b.add(10)

# set = {1, 2, 3}
# a = [4, 5, 6]
# set.add(a)  ##불가능
# set.update(a) ##가능  a는 튜플또는 리스트 형태
# print(set)

# set.dicard(a) a를 없앰 ## set에 a가 이미 없을시 그냥 넘어감
# set.remove(a) a를 없앰 ## set에 a가 이미 없을시 오류냄

# set = {1, 2 ,3}
# set1 = {2, 3 ,4}
# print(set1 | set2) -> 둘이 합친거 반환 ##list는 안됨
# set1.union(set1) ## set1 | set2 과 같은거

# set1 & set2 -> 겹치는 것만 반환
# set1.intersection(set2) ## set1 & set2 과 같은거

# set1 - set2 -> set1에서  set1과 set2가 겹친것을 뺀 걸 반환함
# set1.diffetence(set2) set1 - set2 와 같은거

# set1 ^ set2 -> set1과 set2가 겹치는 것들을 뺀 값들을 전부 보여줌
# set1.symmetric_difference(set2) set1 ^ set2 과 같은거

# set1 = {1, 2 , 3 , 4, 5}
# set2 = {3, 4}
# set1.issubset(set2) -> set1에 있는값이 전부 set2에 있는지 bool형태로 반환
# issuperset은 issubset의 반대

# frozenset(list) -> set의 튜플형태라 보면됨
# set & frozenset 할시 frozenset로 반환됨

# list[0] in list1 -> 왼쪽 인자는 list형식이 아닌 값으로 해줘야함 , bool형태로 반환함 
# list1 = [1, 2, 3]
# list2 = [1, 2, 3 ,4, 5]
# print(list1[0] in list2)
# list2 = [1, 2, 3 ,4, 5, list1]
# print(list1 in list2)

# customer_list = ['cat', 'dog', 'pig', 'panda', 'giraffe', 'lion', 'alligator']
# customer_list = frozenset(customer_list)
# customer_from_door1 = input('customer_from_door1 : ').split(',')
# # customer_from_door1 = customer_from_door1.split(',')
# customer_from_door2 = input('customer_from_door2 : ').split(',')
# D1 = set(customer_from_door1)
# D2 = set(customer_from_door2)
# attendance = D1 | D2
# if not(attendance.issubset(customer_list)) :
#     print("stranger : {}".format(attendance - customer_list))
# else :
#     print("clear")
# if attendance & customer_list ^ customer_list :
#     print("latecomer : {}".format(attendance & customer_list ^ customer_list))
# else :
#     print("all attended")

##################################################################################

# for i in dic  할경우 키값을 받아옴

# dic = {'A' : 1, 'B' : 2}
# print(dic['B'])
# print(dic.get('A'))
# list와 마찬가지로 없는키로 인덱싱할경우 오류발생

# dic['a'] = 1
# dic.update({'a' : 1})

# 'a' = in dic -> bool형태로 반환  ##a라는 "KEY"가 있는지 값은 안됨
# dic = {'a' : 1, 'b' : 2}
# print(1 in dic)   ##False
# print('a' in dic)  ##True

# dic.pop('a') -> a키의 값을 반환하면서 a키를 없앰

# dic.clear() -> list와 똑같이 빈딕셔너리로 만듬

# dic.items    키, 값
# dic.keys()   키
# dic.values() 값
##################################################################################

# list = [1, 2, 3, 4, 5]
# tuple = (1, 2, 3, 4, 5)
# set = {1, 2, 3, 4, 5}
# print(len(list))      # 길이 반환             
# print(max(list))      # 최대값반환         
# print(min(list))      # 최소값반환
# flag = 3 in list      # bool 형태의 값을 넣어줌
# print(flag)


# info = {17, 'dohyeon', 'Ai'}
# age, name, major = info
# print(age,name,major)

# list = [1, 2, 3, 4, 5, 5]
# a, b, c, *rest = list      ##*변수 에는 나머지가 전부 들어감    ##tuple이나 set이여도 리스트 형태로 들어감
# print(a, b, c, rest)
# first, *rest, last = list
# print(first, rest, last)

# tuple, set에서도 모두 적용됨

# r = range(0, 10 ,2)
# print(type(r))
# print(1 in r)
# print(r[1])
# print(r.index(5)) ##없는값을 매개변수로 넣으면 오류
# rr = range(10, 0 ,-2)

##################################################################################

# 문자열도 인덱싱, 슬라이싱 가능

# str변수.capitalize() -> 첫글자를 대문자로 바꿔줌 cap -> Cap
# str변수.count('a') -> a가 몇개 들어가있는지 반환해줌
# str변수.split('t') -> t는 사라지고 t기준으로 문자열이 나뉨 python -> ['py', 'hon'] ##매개변수가 아무것도 없으면 공백을 기준으로 나눔
# dongsoo 를 o로 스플릿하면 ['d', 'ngs', '', '']
# srt변수.splitlines() -> \n 기준으로 문자열 나눔

# 문자열.find('a') 처음으로 나오는 a가 몇번째 인덱스인지 반환 ## 문자열안에 a가 없으면 -1 반환
# 문자열.index('a') find와 동일 ## 문자열안에 a가없으면 오류
# a = 'ababab'
# print(a.find('c') )

# 문자열.isalpha() -> 문자가 있는지 bool형태로 반환
# 문자열.isalnum() -> 문자또는 숫자만 있으면 True 공백이나 특수기호가 껴있으면 False
# str = 'python3__'
# print(str.isalnum())
# 문자열.isdecimal() -> 문자열안에 정수만 있을때 True ##유니코드는 False
# 문자열.isdigit() ##유니코드의 정수도 True
# 문자열.isnumeric()  ##유니코드의 분수도 true
# a = '0' 
# print(a.isdecimal())

# 문자열.islower() -> 전부 소문자인지 아닌지 bool형태로반환
# 문자열.isupper() -> 전부 대문자인지 아닌지 bool형태로반환
# 문자열.lower() -> 문자열을 전부 소문자로 변환
# 문자열.upper() -> 문자열을 전부 대문자로 변환

# 문자열.replace('a', 'b') -> 문자열안의 모든 a를 b로 변환

# 문자열.format('a', 'b') 문자열의 첫번째 {}에 a 두번쨰 {}에 b를 넣어줌 ## 넣어줘야할 값보다 매개변수 개수가 적으면 오류
# format_ = 'hi {1} {0} {1}'
# format_ = format_.format('a', 'b')
# print(format_)

# {:5.0f,} 자료형, 소숫점, 오른쪽 정렬 왼쪽 정렬 가능
# d 인데 실수 넣어주면 오류
# d 인데 소숫점 특정자 넣어주면 오류
# {e}넣으면 4.234e+10 이런식으로 출력함
# s = 123456789.1234
# print('s = {:5,.5f}'.format(s))

# print('Data = %(key값)소숫점자료형' % {'key' : 변수})
# '%(a).2f' % {'a' : data} 

##################################################################################

import math

# print(math.pi, math.e, math.inf, math.nan) pi, 자연상수e, 무한, not a number

# math.floor() -> 버림
# math.ceil() -> 올림
# math.pow() -> 제곱
# math.sqrt() -> 제곱근
# math.log() -> log ## loga(b) a의 log b eg)log10(10) = 1 
# log(a) -> 자연상수 e의 loga  
# math.sin() cos() tan() 기본 삼각함수들에 x값을 넣었을때 y값을 넣어줌
# math.radians(degree) -> 각도를 radian 으로 변환
# math.isinf() -> 무한인지 아닌지 bool로 반환
# math.isnan() -> nan인지 아닌지 bool로 반환
# math.fsum() -> list,tuple,set안의 숫자들 전부 합해줌
# t = {1,2, 3}
# print(math.fsum(t))

##################################################################################

# os -> operating system sys -> system
import os, sys

# cwd -> current_working_directory
# print(os.getcwd()) -> 현재 주소 확인
# chdir -> change_directory
# os.chdir() -> 입력한 주소로 넘어감 ##위에 말했듯이 주소에서 \쓸때 \\로 써줘야함
# 매개변수에'..' 을 넣어주면 상위폴더로 감
# 매개변수에'.'을 넣어주면 이동하지 않음
# mkdir -> make_directory
# os.mkdir() -> 현재 주소에 dir하나를만듬
# listdir -> list_directory
# print(os.listdir()) -> 현재 주소에있는 파일, dir들의 이름을 리스트형태로 반환
# os.rename('dir1', 'dir2') -> dir1의 이름을 dir2로 바꿈
# os.remove() -> 파일을 지움
# os.rmdir() -> dir을 지움


# print(sys.modules)
# print(sys.path)

# f = open('file1.txt', 'w') -> 파일 열기
# f.write('I love python')
# f.write('I love python') -> 파일에 쓰기
# print(f.closed) -> 파일이 닫혀있는지 bool형태로 반환
# f.close() -> 파일닫아줘야함 ## 파일을 두번열면 오류가 나는경우가 있나봄
# print(f.closed) 

# with open('file.txt','w') as f: ->f.close() 안해줘도 됨
#     f.write("good")

# f = open('file', 'r') -> read모드로 염
# f.read() -> 파일안의 내용을 모두 불러옴 ## 전부 불러오고 나서 남아있는게 없기때문에 한번더 read를 하면 빈 텍스트가 나옴
# f.readline() 한줄씩 불러옴

import json

# data = ['1', '2', '3']
# f = open('file.txt','w') 
# json.dump(data,f) -> f에 data의 자료를 덮어씌움

# f = open('file.txt','r')
# a = json.load(f) -> a에 f에 있는 자료를 불러옴
# print(a)

import pickle   ## pickle 을 쓰는 이유? 아스키코드가아닌 이진법으로 저장을해서 자료크기가 겁나 커도 파일크기가 작음

# f = open('file.txt', 'wb')   ## write binary  
# pickle.dump(data,f)  ## json의 dump와 동일
# f.close()

# f = open('file.txt', 'rb') ## 그냥 r로 쓰면 dump 나 load할때 오류 발생
# x = pickle.load(f)
# print(x)


import time
# time.sleep(0.1)



# # iter
# x_str = 'abc'
# x_iter = iter(x_str)
# print(next(x_iter))
# print(next(x_iter))
# print(next(x_iter))



# # enumerate
# import numpy as np
# for cnt, j in enumerate(np.array([10,20,30,40]), start = 1):
#     print(cnt)
#     print(j)


# # zip
# arr = np.array([10,20,30,40])     
# name = ['newton','kepler','euler']
# for i in zip(arr,name):       # 40은 안나옴
#     print(i)       # tuple 로 감싸져서 나옴


# Euler's number
one = 1
x = 1
e = 0
while True:
    x /= 2
    e = (one + x)**(1/x)
    print(e)
    time.sleep(0.5)
    if e == 1.0:
        print(x)
        break
    



##############################################################################
# try and except
age = int(input('enter age : '))
print('Age = {}'.format(age))

while True:
    try:
        age = int(input('enter age : '))
        print(age)
        break
    except ValueError:
        print("input number")
    except:
        print('Exception error occured')

############################################################
# just error in lecture

database = {'u1':'aaa',
            'u2':'bbb',
            'u3':'ccc'}

user_id = 'u1'
user_pw = 'bbb'

if(user_id in database.keys() and user_pw in database.values()):
    print('log in')
else:
    print('not in database')

###############################################################
#list comprehension

i = [i for i in range(10)]
i = [x for x in range(11)
     if x%2==0
     if x%5==0
     ]
even_or_odd = ['even' if i%2==0 else 'odd' for i in range(21)]

# dictionary comprehension
sqr = {x:x**2 if x%2==0 else x for x in range(10)}
###############################################################
# file manage practice
import os, sys # 모듈 가져오기

print(os.getcwd())  # 현재 위치한 파일주소
os.mkdir('my_dir')   # 폴더 하나를 만듬
os.chdir('.\my_dir')  # 하위폴더중 하나인 my_dir로 이동
for i in range(20):    # file+숫자라는 이름의 파일들을 만듬
     f = open('file'+str(i), 'w')
     f.close()
flist = os.listdir('.')  # 하위 파일,폴더들 이름을 반환  . 을 매개변수로 줄시 현재 파일주소를 의미함

for fid in flist:    
    f_name = fid[0:4] # 파일이름의 앞 네글자, file이 들어감
    f_num = fid[4:]   # 파일이름뒤의 숫자 0~19가 들어감
    if int(f_num) < 10: # 파일이름에 0~9는 앞에 2019_를
        os.replace(fid,'2019_'+fid)
    else:               # 10~19는 앞에 2020_을 붙여줌
        os.replace(fid,'2020_'+fid)

os.mkdir('2019_data') # 폴더만듬
os.mkdir('2020_data')

flist = os.listdir('.') 

# filter - method 1
from itertools import compress
idx = list(map(lambda x: 'file' in x,flist))
flist2 = list(compress(flist, idx))

# filter - method 2
flist3 = list(filter(lambda x: 'file' in x,flist))

# filter - method 3
flist4 = [x for x in flist if 'file' in x]

# filter - method 4
import glob
glob.glob('2019_file?')  # ? = 문자하나
glob.glob('2019_file[1,4,5]') # [1,4,5] 정규식이랑 같음
glob.glob('*file*')   # * = 정규식에서의 .

# move files
import shutil
for f_curr in flist4 :
    f_name = f_curr[0:9]
    f_num = f_curr[9:]
    if int(f_num) < 10:
        shutil.move(f_curr, '.\\2019_data') # 2019파일 이동
    else:
        shutil.move(f_curr, '.\\2020_data') # 2020파일이동
##############################################################################


def add10(x):
    global y
    y = x+10
    return y

print(add10(3))
y



def f(*arg):  # 매개변수를 한번에 튜플로 받아옴
    print(arg)
f('af',43,'bb')

def my_add(*args):
    total = 0
    for i in args:
        total += i
    return total
my_add(1,2,3)

def concat(*arg):
    combined = str()
    for a in arg:
        combined += a
    return combined
concat('py','th','on')




a = [1,20,1]
range(*a)

def sqr(x:float,y:float)->float: # -> 뒤는 반환값의  자료형
    """
    

    Parameters
    ----------
    x : FLOAT
        밑
    y : FLOAT
        지수

    Returns
    -------
    result : FLOAT
        x의y제곱

    """
    result = x**y
    return result


print(sqr.__doc__)
print(sqr.__annotations__)
















































