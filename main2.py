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

def content_finder():
  target_content = input("검색할 내용을 입력하세요 : ")
  target_content = target_content.strip()

  files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.json')]

  matching_files = []
  count = 0

  for file_name in files:
        with open(file_name, 'r') as file:
            file_data = json.load(file)
            content = file_data.get('content', [])
            if target_content in content:
                matching_files.append(file_name)
                count += 1

  if matching_files:
        print(f"태그 '{target_content}'와 관련된 파일 목록:")
        for matched_file in matching_files:
            print(f'총 {count}개의 파일을 찾았습니다.')
            print("찾은 파일 리스트")
            print(matched_file)

  else:
        print(f"태그 '{target_content}'와 관련된 파일이 없습니다.")

def tag_finder():

  target_tag = input("찾을 태그를 입력하세요 : ")
  target_tag = target_tag.strip()

  files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.json')]

  matching_files = []
  count = 0

  for file_name in files:
        with open(file_name, 'r') as file:
            file_data = json.load(file)
            tags = file_data.get('tags', [])
            if target_tag in tags:
                matching_files.append(file_name)
                count += 1


  if matching_files:
        print(f"태그 '{target_tag}'와 관련된 파일 목록:")
        for matched_file in matching_files:
            print(f'총 {count}개의 파일을 찾았습니다.')
            print("찾은 파일 리스트")
            print(matched_file)

  else:
        print(f"태그 '{target_tag}'와 관련된 파일이 없습니다.")



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
    content_finder()

  elif choice == 4:
    tag_finder()

  else:
    print("프로그램을 종료 합니다.")
    break



