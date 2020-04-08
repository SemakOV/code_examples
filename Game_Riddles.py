import random
# riddles
riddles = {
    'Ножницы': "Два конца, два кольца, Посредине гвоздик",
    'Крапива': "Не огонь, А жжется",
    'Арбуз': "К нам приехали с бахчи полосатые мячи",
    'Гнездо': "Без рук, без топоренка, построена избенка",
    'Гром': "Конь бежит, Земля дрожит",
    'Молния': "Раскаленная стрела дуб свалила у села",
            }


# make_a_riddle
def make_a_riddle(riddles, incorrect_answer):
    key_riddle = random.choice(list(riddles))
    riddle = riddles[key_riddle]
    print(f"Загадка: \n{riddle}")
    answer_user = input("Введите свой ответ: \n")
    while answer_user.lower() != key_riddle.lower():
        print("Ответ неверный, попробуйте еще раз")
        answer_user = input("Введите свой ответ: \n")
        incorrect_answer += 1
    else:
        print("Верно")
    return incorrect_answer


#logic
def main():
    a = ''
    correct_answer = 0
    incorrect_answer = 0
    while a.lower() != str("Выход").lower():
        result = make_a_riddle(riddles, incorrect_answer)
        incorrect_answer = result
        correct_answer += 1
        a = input('Еще раз? (Введите любое значение, либо введите "Выход"): \n')
    print(f"Игра окончена! \nВерных ответов: {correct_answer} \
    \nНеверных ответов: {incorrect_answer} \nВсего ответов: {correct_answer + incorrect_answer}")


main()
