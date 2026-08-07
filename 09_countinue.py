my_list = ["123", "456", "영크크", "32", "53"]

problems = 0

for text in my_list:

    try:
        my_number = int(text)
    except:
        problems += 1
        continue

    print(my_number)

print(f"문제가 발생한 횟수: {problems}")
