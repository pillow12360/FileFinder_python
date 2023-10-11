
# os 모듈을 이용하여 지정된 폴더내의 파일명을 출력하는 프로그램

import pandas

import os

import re

dir = 'C:/Users/ehdck/Desktop/FileFinder_python'

files = os.listdir(dir)

print(type(files))

#파일명 출력하기

for file in files :

    print(file)



# 읽기
# 파일이 없을 경우 그 파일을 만들기 때문에 예외처리
search = "12345"

import os
filename = "new.txt"
if os.path.exists(filename):
    fr = open(filename, "r")
    line = fr.readlines()
    for i in line:
        i = re.sub("\n", "", i)
        print(i)
        if search == i:
            print("해당 문자가 있습니다.")
        else:
            print("해당 문자가 없습니다.")
    fr.close()
else:
    print("파일이 존재하지 않습니다.")


# search 문자열이 있는 경우 문자가 있습니다. 출력


    

