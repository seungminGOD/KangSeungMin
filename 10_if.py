# 조건문 = if
# 항상 실행되지 않고, 조건에 따라 실행되는 코드가 달랐으면 할 때 사용
# 코드의 분기라고도 표현
# 조건문의 조건은 True와 False로 결과가 나와야 함

# if 조건식:
#   실행할 코드(한 칸 들여쓰기)

# if문의 :은 그 다음 올 코드가 if문 조건식의 결과가 True일 때만 실행하라는 의미
# 즉, 여기서부터 이 조건에 속한다라는 신호
# 조건에 속하는 코드는 모두 들여쓰기가 적용되어 있어야 함

# 들여쓰기 한 코드는 if문의 조건식 결과가 True일 때 실행

temp = 85

if temp > 80:
    print(f"온도가 {temp}보다 크다")  # 들여쓰기 된 코드 실행
else:
    print(" 점검 요망")
print("이건 항상 실행되는 코드")


temp = 50

if temp > 80:
    print("temp 변수의 값이 80보다 크다")  # 들여쓰기 된 코드 실행
    print(" 점검 요망")
print("이건 항상 실행되는 코드")


temp = 70
temp = 90

if temp > 80:
    print("경고")  # if문 밖의 코드는 무조건 실행
print("정상")  # 이 경우 temp 변수 값이 90이이도 실행

if temp > 80:  # if문의 조건이 True일 때만 출력
    print("경고")
else:  # if문의 조건이 False일 때만 출력
    print("정상")  # 항상 실행되지 않음
# 2개의 분기로 코드를 실행해야할 때 사용

# if문 실습
# 사용자에게 나이를 입력받아 성인인지 출력하는 조건문 작성

age = 15

if age >= 19:
    print("성인입니다.")
else:
    print("미성년자입니다.")

# 지금 나는 무엇을 하고 있는지 모르겠다.
# 현재 날짜 2026.07.29
# 현재 시각 10:26 AM
# 과연 내가 이걸 할 수 있을까?
# IF문은 아주 쉽다.
# 하지만 내 코드가 맞을까?
# 컴활때 주구장창한 IF
# 수료식까지 까마득하다.
# 취업은?

num = 30

if num == 30:
    print("정답입니다! 축하드려요!")
else:
    print("틀렸습니다.")
print("게임이 종료되었습니다.")

answer = 50
user_answer = int(input("정답을 입력해주세요.: "))

if answer == user_answer:
    print("정답!")

else:
    print("틀렸습니다!")
print("게임 종료")

while True:
    color = input("신호등 색을 입력하세요: ")

    if color == "초록색" or color == "초록":
        print("건너가세요!")
        break

    elif color == "빨간색" or color == "빨강":
        print("기다리세요!")
        break

    else:
        print("다시 입력하세요!")

    # if 조건문 색깔 말고 다른 색깔 넣으면 자동으로 종료됨
    # 그래서 정답 맞출 때까지 색 입력 반복되게 만들었음
    # if문은 재밌음
    # 응용하는 것도 더 재밌음

    # 사람 체온 판단
    # 정상 체온 범위: 36.3 ~ 36.9

    # ========================================================
user_a = float(input("체온을 입력해주세요: "))

if user_a >= 36.3 and user_a <= 36.9:
    print("당신은 정상 체온입니다.")
else:
    if user_a > 36.9:
        print("당신은 열이 나고 있습니다.")
    else:
        print("당신은 저체온입니다.")

print("체온 판단 완료")


# elif
# else와 if만으로 분기하기에는 불편하고 if 중첩이 너무 많아져서 생김
if user_a <= 36.3:
    print("당신은 저체온입니다.")
elif user_a >= 36.9 and user_a < 37.8:
    print("당신은 미열입니다. 주의하세요.")
elif user_a >= 37.8:
    print("당신은 고온입니다. 병원에 방문하세요.")
else:
    print("당신은 정상 체온입니다.")
print("체온 확인 완료")

score = 50

if score >= 90:
    print("우수")
elif score >= 70:
    print("보통")
elif score >= 50:
    print("미흡")
else:
    print("비상")

if not (3 == 5):
    print("출력됩니다")
# 3과 5는 같지 않아 False가 되지만 앞에 not이 있어서 True로 뒤집어 if로 인식

# if문은 줄바꿈을 하지 않아도 :을 기준으로 동작 자체 가능

# =============================================
temp = int(input("측정 온도를 입력하세요: "))

if temp > 80:
    print("위험")
elif temp > 60:
    print("주의")
else:
    print("정상")

# ================================================
id = "admin"
pw = "1234"

input_id = input("아이디를 입력하세요:")
input_pw = input("비밀번호를 입력하세요:")

if input_id == id and input_pw == pw:
    print("로그인 성공")
else:
    print("로그인 실패")

# GPT의 도움 없이는 못 해
# 응용이 더 어려워지니까 흥미가 떨어지는 중....
