import os
from random import randrange

def check_validity(in_string, init=True):
    if not(in_string.isdigit()):
        if (init):
            print("숫자가 아닙니다")
        return False
    elif len(in_string) != 4:
        if (init):
            print("길이가 4가 아닙니다")
        return False
    else:
        for i in range(3):
            for j in range(i+1, 4):
                if in_string[i] == in_string[j]:
                    if (init):
                        print("중복되는 수가 있습니다")
                    return False
    return True

win_log = [0, 0]
def baseball(target):
    win_switch = True
    drawUI([], win_log)
    log_list = []
    for i in range(9):
        print(i+1, "번째 시도")
        strike = 0
        ball = 0
        while True:
            numbers = input("입력 : ")
            result = check_validity(numbers)
            if (result):
                break
        for j in range(4):
            if (numbers[j] in target):
                if (numbers[j] == target[j]):
                    strike += 1
                else:
                    ball += 1
        if strike > 3:
            win_log[0] += 1
            win_switch = False
            input("win")
            break
        log_list.append([numbers, ball, strike])
        drawUI(log_list, win_log)
    if (win_switch):
        win_log[1] += 1
        input("lose %s" %target)

def drawUI(log_list, results):
    os.system('cls')
    print(results[0]+results[1],"전",results[0],"승",results[1],"패")
    for idx, element in enumerate(log_list):
        print(idx+1, "회 : ", element[0], " ", element[1], "B", element[2], "S")
    for i in range(9 - len(log_list)):
        print("")

win_log = [0, 0]
while True:
    target = str(randrange(1000, 9999))
    result = check_validity(target, False)
    if (result):
        baseball(target)
