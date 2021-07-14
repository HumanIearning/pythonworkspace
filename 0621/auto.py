##필요한 함수들 import
from os import listdir,makedirs
from os.path import isdir
from shutil import copyfile   


##변수에 경로 저장
origin_dir = "C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621\\scan"
out_dir = "C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621\\out"
##file_list에 origin_dir에 있는것들 list화
file_list = listdir(origin_dir)
#print(file_list)

for file_name in file_list:
    ##년도 월 날짜로 파일 찾으려고 슬라이싱
    year = file_name[:4]
    month = file_name[4:6]
    day = file_name[6:8]
    ##년도 월 날짜로 나눠진 파일경로 만듬
    target_dir = out_dir + "\\" + year + "\\" + month + "\\" + day
    #print(target_dir)
    if not isdir(target_dir):
        ##target_dir에 있는 경로에 파일만듬
        makedirs(target_dir)
    ##원래 있던 파일들을 만든 경로에 복사시켜줌
    copyfile(origin_dir + "\\" + file_name, target_dir + "\\" + file_name)









