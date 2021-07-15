## 파일 목록 반환하는 listdir
from os import listdir
file_list = listdir('C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621')
print(file_list)

##파일 유무 확인
from os.path import exists
if exists('C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621\\libraries.py') :
    print("있다")

##폴더 생성하기
from os import makedirs
#makedirs('C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621\\test')
if exists('C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621\\test') :
    print("있다")

##파일 복사하기
from shutil import copyfile
copyfile('C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621\\libraries.py',\
    'C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621\\copied.py')
file_name = listdir('C:\\Users\\user\\OneDrive\\바탕 화면\\python\\0621')
print(file_name)

