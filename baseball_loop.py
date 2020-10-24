def baseball(goal):
    for inning in range(9):
        ball = 0
        strike = 0
        print("%d회 공격" %(inning+1))
        guess = input("입력해주세요 : ")
        for index in range(4):
            letter = guess[index]
            if (letter in answer):
                if (letter == answer[index]):
                    strike += 1
                else:
                    ball += 1
        if (strike > 3):
            print("You win!")
        else:
            print("%dB%dS" %(ball, strike))

while True:
    answer = input("맞춰야 할 값을 입력해 주세요 : ")
    if (answer == "끝"):
        break
    print('\n'*40)
    baseball(answer)
