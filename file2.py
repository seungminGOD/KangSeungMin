import os
import sys
import csv

csv_path = os.path.join("data", "08_press.csv")

if not os.path.exists(csv_path):
    print("파일 없습니다")
    sys.exit(1)

print("파일이 있습니다")

with open(csv_path, "r", encoding="utf-8") as f:
    print(f.readlines())
    reader = csv.reader(f)

    for row in reader:
        print(row)


# 실습 4. csv.reader로 CSV 읽기

import os
import sys
import csv

with open(csv_path, "r", encoding="utf-8") as f:
    print(f.readlines())
    reader = csv.reader(f)

    for row in reader:
        print(row(0))
