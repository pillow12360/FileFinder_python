# 10월 16일

# 파일을 생성하는 함수 정의

import hashlib

import os
import json

def produce_file():
    file_name = input("파일명을 입력하세요 : ")
    tags_input = input("태그를 입력하세요 (띄어쓰기 구분): ")
    tags = [tag.strip() for tag in tags_input.split(' ')]
    file_content = input("파일에 저장할 내용을 입력 : ")

    file_data = {'content': file_content, 'tags': tags}
    
    with open(file_name + '.json', 'w',encoding='UTF8') as file:
        json.dump(file_data, file)

    print(f"파일 '{file_name}.txt'이(가) 생성되었습니다.")

# 파일의 해시값을 구하는 프로그램

def hash_find(filepath, blocksize=8192):
    sha_1 = hashlib.sha1()
    try:
        f = open(filepath, "rb")
    except IOError as e:
        print("file open error", e)
        return
    while True:
        buf = f.read(blocksize)
        if not buf:
            break
        sha_1.update(buf)
    return sha_1.hexdigest()

def content_finder(target_directory, target_word):
  count = 0
  find_list = []

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
                  # print("-----------------------------------------------------------------")
                  # print(f"'{filename}'파일에 해당 '{target_word}' 내용이 포함되어 있습니다.")
                  count += 1
                  find_list.append(filename)

            except: # 파일의 내용을 탐색할 수 없다면
                pass
        if count == 0:
          return print("해당 내용이 포함되어있는 파일이 존재하지 않습니다.")
  print(f'총 {count}개의 파일을 찾았습니다.')
  print("찾은 파일 이름 리스트 출력")
  for name in find_list:
    print(name)

def tag_finder():
  target_tag = input("찾을 태그를 입력하세요 : ")

  pass



print("파이썬 프로젝트 실행")

while True:
  print("=========================================================================================")
  print("1. 파일 생성 2. 파일의 해시 값 찾기 3. 파일의 내용으로 파일 검색 4. 태그 내용으로 파일 검색")
  print("=========================================================================================")

  choice = int(input("기능을 선택하세요 : "))

  if choice == 1:
    produce_file()
  elif choice == 2:
    find = input("해시 값을 찾을 파일의 이름 : ")
    print(hash_find(find))
  
  elif choice == 3:
    dir = "C:/Users/ehdck/Desktop/FileFinder_python"
    tag = input("검색할 내용(콘텐츠) 입력 : ")
    content_finder(dir,tag)

  elif choice == 4:
    tag_finder()

  else:
    print("프로그램을 종료 합니다.")
    break



