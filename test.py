# 실습 2. 다중 매개변수로 센서값 계산하기


def sensor(name, temp):
    print(name, temp, "도")


sensor("모터", 78)
sensor("펌프", 92)


# 실습 3. 키워드 인자로 함수 호출하기


def report(name, temp):
    print(name + str(temp))


report(name="모터", temp=78)
report(temp=92, name="펌프")

# 실습 4. 반환값으로 간단 계산기 만들기


def add(a, b):
    return a + b


result = add(80.0, 5.0)
print(result)

result = add(result, 5.0)
print(result)


# 실습 3. 처리 흐름 만들기


def avg(a, b):
    return (a + b) / 2


def check(score):
    if score >= 80:
        print("정상")
    else:
        print("점검")


result = avg(80, 90)
print("평균", result)

check(result)
