def report(name, value, unit="도(C)"):
    print(f"{name} : {value}{unit}")


report("압축기A", 75.3, "도(C)")
report("압축기A", 75.3)


def is_over_limit(value, limit):
    if value > limit:
        return True
    return False


print(f"위험한가요? {is_over_limit(95,90)}")

# 실습 2
# 함수 안에서 만든 지역변수가 함수 밖에서는 보이지 않음을 확인
