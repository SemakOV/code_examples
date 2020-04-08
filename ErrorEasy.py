# 1.Пользователь вводит число, если оно четное - выбрасываем исключение ValueError,
# если оно меньше 0 - TypeError, если оно больше 10 - IndexError. Обрабатываем ошибку,
# говорим пользователю, в чем его ошибка
try:
    value = int(input("Введите число: "))
    if value % 2 == 0 and value <= 10 and value >= 0:
        raise ValueError('Число четное')
    elif value < 0:
        raise TypeError('Число меньше 0')
    elif value > 10:
        raise IndexError('Число больше 10')
    print(value)
except ValueError as e:
    print("Неверное значение!", e)
except TypeError as e:
    print("Неверное значение!", e)
except IndexError as e:
    print("Неверное значение!", e)


#2. Создайте список произвольной длины. Пользователь должен ввести индекс объекта,
# который хочет посмотреть. Если все хорошо - пишите объект в консоль.
# Если нет - обработайте возмозможные ошибки и скажите ему, что не так
lst = [a for a in range(3, 20, 3)]
try:
    ind = int(input("Введите индекс: "))
    print(lst[ind])
except ValueError as e:
    print("Неверное значение индекса,\n{}".format(str(e).capitalize()))
except IndexError as e:
    print("Значение с заданным индексом не найдено,\n{}".format(str(e).capitalize()))
