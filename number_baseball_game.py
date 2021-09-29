import random as rand


def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        random_numbers = rand.randint(1, 9)

        if random_numbers not in numbers:
            numbers.append(random_numbers)

    return numbers


def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    while len(new_guess) < 3:
        new_num = int(input(f'{len(new_guess) + 1}번째 숫자를 입력하세요: '))

        if new_num < 0 or new_num > 9:
            print('범위를 벗어나는 숫자입니다. 다시 입력하세요.')
        elif new_num in new_guess:
            print('중복되는 숫자입니다. 다시 입력하세요.')
        else:
            new_guess.append(new_num)

    return new_guess


def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


ANSWER = generate_numbers()
tries = 0


while True:
    user_guess = take_guess()
    s, b = get_score(user_guess, ANSWER)

    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break

print(f'축하합니다. {tries}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.')


