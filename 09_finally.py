# except들의 연속과 finally 코드

# text = "24.5" # 정상
text = "영크크"  # 비정상

temp = 0

try:
    temp = float(text)
except ValueError:
    print("ValueError 문제가 발생했습니다")
except NameError:
    print("NameError 문제가 발생했습니다")
finally:
    # 오류가 있건 없건 finally의 코드를 실행하 마무리
    print(temp * 2)
