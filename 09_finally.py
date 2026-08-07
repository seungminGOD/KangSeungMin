# text = "24.5"

text = "abc"

try:
    temp = float(text)

except ValueError:
    print("문제가 발생했습니다")
    temp = 0
finally:
    print("종료")
