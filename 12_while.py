# while은 특정 조건(횟수 X)이 False가 될 때까지 반복해야 하는 경우 사용

# 무한루프 유의
# count = 1
# hile count <= 3:
# print(count)
# while문은 조건이 거짓이 되는 플래그를 꼭 세워야 함
# 무한로프 강제 종료: Ctrl + C

# while문 사용 체크리스트
# 1. 반복 전 변수 존재 여부
# 2. 반복하다가 언젠가 False가 될 수 있는 종료 조건 포함 여부
# 3. 변수가 거짓 방향으로 값이 변경되는지 여부

# count = 1 # 1번
# while count <= 3: # 2번
# c ount = 0: # 반복문 안에 count 변수를 계산 0으로 재할당
# print(count)
# count += 1 # 3번

answer = 7
guess = 0
while guess != answer:
    guess = int(input("맞혀 보세요: "))
print("정답입니다")

# break
# 반복을 그만 돌고 싶을 때
# 예 1) [1. 1. 3, 3, 2, 1, 1, 1]
# 위 리스트를 돌면서 10 이상이 되면 중단하고 싶을 때
# 예 2) 사용자 입력값을 누적하다가 누적값이 총 15를 넘으면
