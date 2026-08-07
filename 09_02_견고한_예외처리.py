# 09_02_견고한_예외처리

# [실습 2] 반복문에서 불량 줄 건너뛰기
# - 소숫점 이하의 숫자가 포함된 숫자들을 20개정도 만들어 문자로 리스트에 담아주세요 "123.45"
# - 그 사이에 엉뚱한 글자들이 포함된 내용도 포함시켜 주세요. "영크크"
# - 위 리스트 데이터를 사용해서 문제를 풀어주세요

my_list = [
    "123.45",
    "67.89",
    "영크크",
    "45.12",
    "999.99",
    "안녕",
    "12.34",
    "56.78",
    "파이썬",
    "100.50",
    "88.88",
    "코딩",
    "3.14",
    "250.75",
    "테스트",
    "77.77",
    "1.23",
    "오류",
    "500.01",
    "42.42",
]

total = 0

for text in my_list:
    try:
        my_number = float(text)
    except ValueError:
        continue

    total += my_number
    print(my_number)

print(f"합계: {total}")


# [실습 3] 여러 파일 묶어 처리하기
# - 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다
# - 다음과 같은 식의 리스트를 만들어 반복문으로 처리해봅시다
# - for문으로 리스트의 문자열을 꺼내어 해당 이름의 파일들을 열어보기 시도하면 됩니다

# file_names = ["08_press.csv", "09_ict.csv", "09_ict_dirty.csv"]

file_names = ["08_press.csv", "09_ict.csv", "09_ict_dirty.csv"]

count = 0

for file in file_names:
    try:
        f = open(file, "r", encoding="utf-8")
        print(file, "처리 완료")
        f.close()
        count += 1

    except FileNotFoundError:
        continue

print("처리한 파일 수:", count)
