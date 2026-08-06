import os
import sys
import csv

csv_path = os.path.join("data", "result.csv")

with open(csv_path, "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["09:00", "PUMP-01"])

    # 실습 5. csv.writer로 CSV 쓰기

import os
import csv

csv_path = os.path.join("data", "실습5.csv")

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["시각", "설비"])
    writer.writerow(["15:00", "PUMP-04"])
