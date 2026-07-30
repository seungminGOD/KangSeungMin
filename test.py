temps = [25, 33, 36, 28, 21, 39, 35, 25, 24, 37]
total = 0
for t in temps:
    total += t
print("전체 평균:", total / len(temps))
num = []
for t in temps:
    if t > 30:
        num.append(t)
num_total = 0
for h in num:
    num_total += h
print("고온 개수:", len(num))
print("고온 평균:", num_total / len(num))
