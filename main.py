
# os 모듈을 이용하여 지정된 폴더내의 파일명을 출력하는 프로그램


'''

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


    
import glob

# 현재 폴더 내 모든 폴더
for folder_name in glob.glob('**/'): ## 또는 glob.glob(*/)
    print(folder_name)

# 현재 폴더 내 모든 폴더와 파일
for f in glob.glob('**'): ## 또는 glob.glob(*)
    print(f)

# 현재 폴더내에 test로 시작하는 파일명 찾기
start_str = 'test'
for f in glob.glob(f'test_folder/{start_str}*.txt'):
    print(f)

'''

# 10월 14일 토요일

# 지정된 디렉터리에서 내가 찾고자 하는 단어를 입력할 시 그 단어가 포함되어있는 파일명을 출력하는 프로그램

# 일단 txt파일만 지원

import os

target_directory = input('검색할 디렉터리명 입력 : ')

target_word = input("파일내 찾고자하는 키워드 입력 : ")

for (path, dir, files) in os.walk(target_directory):
    # 경로
    # 경로 내 디렉터리 리스트
    # files : 해당디렉터리의 파일
    # print(path, dir, files)

    for filename in files:
        # print(path+os.sep+filename)
        with open(path+os.sep+filename, 'r', encoding='UTF8') as f:# 인코딩 utf8로 지정하지 않으면 한글이 깨짐
        # os.sep은 경로구분자 \
        # with, f를 활용하여 자동으로 close
            try: 
                if target_word in f: # 파일에 내용이 포함되어 있으면
                  print("--------------------------")
                  print(f"{filename}파일에 해당 {target_word}내용이 포함되어 있습니다.")
                  
            except: # 파일의 내용을 탐색할 수 없다면
                pass

