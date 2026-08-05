# 실습 1. import 세 방식으로 모듈 가져오기

import math

print(math.sqrt(16))
from math import sqrt

print(sqrt(16))
import math as m

print(m.sqrt(16))

# 실습 2. 표준 라이브러리로 센서값 만들기

import random
import math

num = random.randint(1, 100)
print("센서값:", num)

print("제곱근:", math.sqrt(num))

# 실습3. os로 폴더 목록 살펴보기

import os

path = os.getcwd()
print("현재 경로:", path)

files = os.listdir()

for file in files:
    print("목록:", file)

    if file.endswith(".csv"):
        print("csv파일:", file)

# 실습4. os로 파일 존재 확인하기

import os

path = os.path.join(os.getcwd(), "08_press.csv")
print("파일 경로:", path)

result = os.path.exists(path)
print(result)

if result:
    print("파일 있음")
else:
    print("파일 없음")

# 실습5. datetime으로 점검 기록 남기기

import os
from datetime import datetime

files = os.listdir()
count = len(files)

now = datetime.now()

print(f"파일 {count}개, 점검 시각 {now}")
