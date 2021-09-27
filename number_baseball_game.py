def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []

    S = 0
    B = 0
    num1 = int(new_guess[0])
    num2 = int(new_guess[1])
    num3 = int(new_guess[2])

    while True:
        guess1 = int(input('1번째 숫자를 입력하세요: '))
        if guess1 == num1:
            S += 1
        elif guess1 == num2 or guess1 == num3:
            B += 1
        elif guess1 < 1 or guess1 > 9:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
            guess1 = int(input('1번째 숫자를 입력하세요: '))
        new_guess.append(guess1)

        guess2 = int(input('2번째 숫자를 입력하세요: '))
        if guess2 == num2:
            S += 1
        elif guess2 == num1 or guess2 == num3:
            B += 1
        elif guess2 < 1 or guess2 > 9:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
            guess2 = int(input('2번째 숫자를 입력하세요: '))
        elif guess2 == int(guess1):
            print('중복되는 숫자입니다. 다시 입력하세요.')
            guess2 = int(input('2번째 숫자를 입력하세요: '))
        new_guess.append(guess2)

        guess3 = int(input('3번째 숫자를 입력하세요: '))
        if guess3 == num3:
            S += 1
        elif guess3 == num2 or guess3 == num1:
            B += 1
        elif guess3 < 1 or guess3 > 9:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
            guess3 = int(input('3번째 숫자를 입력하세요: '))
        elif guess3 == int(guess1) or guess3 == int(guess2):
            print('중복되는 숫자입니다. 다시 입력하세요.')
            guess3 = int(input('3번째 숫자를 입력하세요: '))
        new_guess.append(guess3)
        break
        
    return new_guess

print(take_guess())
