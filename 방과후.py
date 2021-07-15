# i = 1
# sum = 0
# while i<=50:
#     if i % 2 == 0:
#         sum += i
#     i += 1
# print("{0}".format(sum))    

##배열
# score = [50,95,100,80,85]
# print(score)
# score.append(10)
# print(score)
# score.reverse()
# print(score)
# score.clear()
# print(score)
# score.remove(100)
# print(score)


# std = []
# sum = 0
# cnt = int(input("몇 개"))
# for i in range(0,cnt,1): 
#     j = input()
#     std.append(j)
# print(std)
# print(sum(std))


#from pickle import TRUE
#from typing import AsyncGenerator


#list1 = ['data1',10000,['data2',500],(100,200),{'key','value'},TRUE]
#print(list)
#list1 = ['you','can','do','it']
#print(list1[2])
#list1.insert(2,'not')
#print(list1)
#print(list1[1:4])

#dic_std = {'name': 'dohyeon', 'age': 17, 'num': '010-7337-3896'}
#print(dic_std)

#std_list = list(dic_std)
#print(std_list)

# data = range(10,20)
# print(data)
# data = range(10)
# print(list(data))
# data = range(10,20,2)
# print(list(data))

# def hello(name):
#     print(name + "! how are you today")
# hello('dohyeon')







# from practice_class import Email

# e = Email()
# e.sender = "comt.knloe@gsm.hs.kr"
# recv_list = ["a@gmail.com","b@gmail.com","c@gmail.com"]

# for recv in recv_list :
#     e.send_mail(recv, " Welcome!","This is content")








# ## 1. 라이브러리 가져오기
# from shutil import copyfile ##폴더,파일 다루는 라이브러리
# from os.path import isdir 
# from os import listdir,makedirs 

# ## 2. 폴더와 파일 목록 조회
# origin_dir = "C:\Users\user\OneDrive\바탕 화면\python\scan"
# out_dir = "C:\Users\user\OneDrive\바탕 화면\python\out"

# file_list = listdir(origin_dir)
# print(file_list)
# print("--------------------------")


# ## 3.파일명 분석하기
# for file_name in file_list :
#     file_date = file_name[:8]
#     print(file_date)

#     year = file_date[:4]
#     month = file_date[4:6]
#     day = file_date[6:]
#     print("year : " + year + "month" + month + "day :\n" + day)





import os
#f = open("test.txt",'w',encoding = 'UTF-8') #r읽기 w처음쓰기 a추가로쓰기
#f.write("파이썬 공부중gg\n")
#f.close()

#filenames = os.listdir("C:/")
#full_filename = os.path.join("C:/", filenames[13])
#ext = os.path.splitext(full_filename)
#print(ext)





import re
# p = re.compile('[a-z]+')  #.match 는 매치하지않는것이 매치하는것보다 먼저나오면 뒤에 무시하고 none 반환

# m = p.match('python4kika') #search는 매치하지 않는것이 나오더라도 처음으로 매치하는곳~처음매치하지않는곳까지 검색
# print(m)
# print(m.group()) ##매치된 문자열
# print(m.start())
# print(m.end())
# print(m.span()) #튜플형태

# m1 = p.search("3python")
# print(m1)

# m2 = p.findall('life 3 is 4 too short') #findall은 매치하지않으면 다음으로 넘기면서 계속 검색
# print(m2)

# m3 = p.finditer('life is too short')   #finditer는 반복문으로 사용시 나오는 객체 생성
# for r in m3:
#     print(r)

# p1 = re.compile('a.b',re.DOTALL)  #re.DORALL 은 .에 개행문자(\n)가 들어가도 매칭됨 re.S로도 가능
# m4 = p1.match('a\nb')
# print(m4)

# p2 = re.compile('[a-z]+', re.IGNORECASE) #re.I 로도 가능, 대소문자 무시해줌
# print(p2.match('pYTHON'))

# p3 = re.compile('^python\s\w+') # ^ <- 맨처음이라는뜻  \s <- 공백이라는 뜻(\n도 잡는듯?) \w <- 알파벳, 숫자, _중의 한 문자 re.M <- 새로운 줄이면 ^있어도 매칭함
# data = """python one  
# life is too short
# python two
# you need python
# python three"""
# print(p3.findall(data))

# p4 = re.compile(r'&[#](0[0-7]+|[0-9]+|x[0-9a-fA-F]+);')
# p4 = re.compile(r"""
# &[#]                # start of a numeric entity reference
# (                   
#     0[0-7]+         # Octal form
#     |[0-9]+         # Decimal form
#     |x[0-9a-fA-F]+  # Hexadecimal form
# )
# ;                   # Trailing semicolon
# """,re.VERBOSE)     #re.VERBOSE <- 긴 정규식 표현시 공백이나 개행을 인식안해서 오류가 나는데 개행이나 공백 무시하고 매칭해줌 따라서 정규식 설명가능

p5 = re.compile('[\s]ection') # \\ -> \   \s -> 공백으로 인식 so, '\section' 으로 할시 오류 발생  r' '으로 할시 뒤 정규식을 rawstring으로 인식해서 \s 같은 문제 해결 가능
m5 = p5.search("s ection")
print(m5)



# p6 = re.compile('Crow|Servo') #|는 or 이라는 의미
# m6 = p6.match('CrowHello')
# print(m6)

# p7 = re.search('^Life','Life is too short, Life')  # ^는 위에 말했듯이 맨처음만 가능 즉 MY life 에서 ^life 찾으면 안나옴
# print(p7.end())                                    # $는 맨 마지막에 있을때만 매칭

# p8 = re.compile(r'\bclass\b')
# m8 = p8.search('no class at all')
# print(m8)

#그루핑
# p9 = re.compile('(ABC)+')
# m9 = p9.search(' ABCABCABCABCABC OK?')
# print(m9)
# print(m9.group(0))

# p10 = re.compile(r"(\w+)\s+\d+[-]+\d+[-]\d+")
# m10 = p10.search("KIM 010-1234-1245")
# print(m10.group(3))

# p11 = re.compile(r'(?P<word>\b\w+)\s+\1') # P 대문자로 해야함
# print(p11.search(' Paris in the the rain rain ').group())

# #전방탐색 : 긍정형 (?=) # 검색에는 포함하지만 결과에는 포함안함
# p12 = re.compile(".+(?=:)") 
# m12 = p12.search('http:google.com')
# print(m12.group())
# #전방탐색 : 부정형 (?!) # (?!  )안에 있으면 찾지만 매치안함
# p13 = re.compile(".*[.](?!bat$).*$", re.MULTILINE)
# m13 = p13.findall("""
# autoexec.exe
# autoexec.bat
# autoexec.jpg
# """)
# print(m13)

# p14 = re.compile('(blue|white|red)')
# m14 = p14.sub('color', 'blue socks and red shoes') # 정규 표현식에 매치되는것을 첫번째 인자로 바꿈
# print(m14)














































































































































































































