# 실습 2. with open으로 파일에 쓰기

import os
import sys
import csv

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])

# 실습 3. a 모드로 기록 이어붙이기

import os
import csv

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "a", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["10:00", "PUMP-02"])

with open(csv_path, "r", encoding="utf-8") as f:
    print(f.read())

# 실습 4. csv.reader로 CSV 읽기

import os
import sys
import csv

with open(csv_path, "r", encoding="utf-8") as f:
    print(f.readlines())
    reader = csv.reader(f)

    for row in reader:
        print(row(0))


# 실습 5. csv.writer로 CSV 쓰기

import os
import csv

csv_path = os.path.join("data", "실습5.csv")

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["15:00", "PUMP-04"])

# 실습 3. 구체적 예외로 입력 검증하기

try:
    num = int(input("숫자 입력: "))
    print(100 / num)

except ValueError:
    print("숫자를 입력하세요.")

except ZeroDivisionError:
    print("0은 입력할 수 없습니다.")

print("프로그램 종료")
