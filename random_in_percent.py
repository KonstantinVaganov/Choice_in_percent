import random
import timeit


def choice_in_percent(percent, arg1, arg2):
    ''' Для работы нужно импортировать модуль random.
        percent = указать проценты
        arg1 = с шансом (percent) выпадет arg1
        arg2 = с шансом (100 - percent) выпадет arg2 '''
    full = 100
    result = []
    full -= percent
    for i in range(full):
        result.append(arg2)
    for j in range(percent):
        result.append(arg1)
    return random.choice(result)


def choice_in_percent2(percent, arg1, arg2):
    ''' Для работы нужно импортировать модуль random.
        percent = указать проценты
        arg1 = с шансом (percent) выпадет arg1
        arg2 = с шансом (100 - percent) выпадет arg2 '''
    result = random.choice(range(1, 101))
    if 1 <= result <= percent:
        return arg1
    else:
        return arg2


print(choice_in_percent(10, 'Шанс выпода 10%', 'Шанс выпода 90%'))
print(choice_in_percent2(10, 'Шанс выпода 10%', 'Шанс выпода 90%'))
