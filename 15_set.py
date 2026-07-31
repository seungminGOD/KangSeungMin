list_ = []
print(type(list_))
tuple_ = ()
print(type(tuple_))

empty_set = {}
print(type(empty_set))
# 빈 중괄호는 딕셔너리라라는 다른 자료형으로 생성

real_empty_set = set()
print(type(real_empty_set))

logs = ["S01", "S02", "S01", "S03", "S01"]
unique = {logs}
print(type(unique))

unique = set(logs)
print(type(unique))
print(unique)

print(unique[0])
# set에서 인덱스 사용 시 Error 발생

# set을 사용해서 리스트에 들어있는 유니크한 값 종류 수를 알 수 있음

# 셋에 값 추가하기
# 셋 .add
# 이미 있는 값을 추가할 경우 무시

alerts = {"S01", "S02"}

# 경고 상태인 S03이 추가될 경우
# .add()를 사용해서 추가
alerts.add("S03")
print(alerts)

# S01에서 또 경고가 발생
# 이미 S01은 경고가 발생한 적이 있고 alerts라는 셋에는 경고가 발생한 센서만 저장하고 싶음
# 횟수 상관없이
alerts.add("S01")
print(alerts)
# S01이라는 값을 또 넣어도 무시하고 한 번만 저장
# 그래서 독립적인 값을 저장하기에는 아주 편리함

sorted = sorted(alerts)
print(sorted)
print(type(sorted))
