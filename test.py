temps = [39, 24, 22, 28, 35, 31, 36]
high = []
for t in temps:
    if t > 30:
        high.append(t)
print(high)  # [32, 35]
