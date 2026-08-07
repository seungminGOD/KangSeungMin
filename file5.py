import os
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

# 위 경로의 파일을 찾지 못하면 강제종료시키기
if not os.path.exists(csv_path):
    print("파일이 없습니다")
    sys.exit(1)  # 비정상 종료시 보통 0이 아닌 값(예 1) 전달

print("파일이 있습니다")

with open(csv_path, "r", encoding="utf-8") as f:
    # print(f.readlines()) # 이제 csv 전문가에게 맡깁시다
    reader = csv.reader(f)

    # DictReader가 아닌 그냥 reader를 사용한다면
    # 보통 csv파일의 첫줄인 헤더줄도 읽어버린다
    # reader에게 첫줄은 건너뛰라고 말하는 방법이 필요하다
    # next(reader)는 한줄 건너뛰고 reader가 반응하게 한다
    header = next(reader)
    # header는 따로 리스트로 챙겨진다
    # ['설비ID', '시각', '진동X', '진동Y', '전류', '상태']
    print(header)

    for row in reader:

        print(row[0])  # 각 행(row)마다 리스트로 출력됨
