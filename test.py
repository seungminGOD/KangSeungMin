# 안녕 인덱스 출력
list = ["안녕", "hi", "hi", "안녕", "hi", "안녕"]

# 리스트의 모든 요소에 접근을 해야 하는 경우가 잦음
# 그래서 python이 반복문에서 이를 쉽게 할 수 있도록 enumerate라는 내장 함수 제공
# enumerate는 리스트의 모든 요소를 앞에서부터 순서대로 하나씩 찍어가며 접근
# 접근해서 각자의 인덱스와 그 값을 뽑아줌
# 값을 두 개 받으니 우리도 변수를 2개 준비하면 각 변수에 쏙쏙 값이 할당

for index, Value in enumerate(list):
    print(Value)

for i in range(len(list)):
    print(list[i])

# 사실 이 두 가지는 동일한 동작


# ==============================================

# 2단 출력하기
for su in range(1, 10):
    print(f"2 X {su} = {2 * su}")

# 1 ~ 5단 출력
# 필요한 변수 : 2개(몇 단을 출력할건지, 얼마나 곱할건지)
# 몇 단을 출력할건지: 1~5
# 거기에 얼마나 곱할건지: 1~9
# for문 중첩 사용
# 1단을 유지한 상태에서 곱할 값은 커져야 함

for i in range(1, 6):  # 1~5단까지 반복
    for j in range(1, 10):  # 1단에서 9까지 곱하고 반복 종료
        print(f"{i} X {j} = {i * j}")
    print(f"--- {i}단 끝 ---")

# 1~9단 사이 2의 배수 단만 구구단 출력
# 2, 4, 6, 8단 출력
# range에 간격 전달
# if문 사용

for i in range(2, 10, 2):
    for j in range(1, 10):
        print(f"{i} X {j} = {i * j}")
    print(f"---{i}단 끝 ---")
