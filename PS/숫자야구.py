import random
answer = f"{random.randint(0, 999):03d}"
attempts = 0

while True:
    guess = input("입력: ")
    if len(guess) != 3 or not guess.isdigit():
        print("세 자리 숫자만 입력하세요.")
        continue

    attempts += 1
    strike = 0
    ball = 0
    for i in range(3):
        if guess[i] == answer[i]:
            strike += 1
        elif guess[i] in answer:
            ball += 1

    if strike == 0 and ball == 0:
        print("result: out")
    else:
        print(f"result: {strike} Strike, {ball} Ball")

    if strike == 3:
        print(f"succeed! attempts: {attempts}회")
        break
