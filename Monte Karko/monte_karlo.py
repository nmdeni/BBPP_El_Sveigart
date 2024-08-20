"""Имитационное моделирование парадокса дней рождений, (с) Эл Свейгарт
al@inventwithpython.com Изучаем неожиданные вероятности из "Парадокса
дней рождения". Большие информации - в статье
https://ru.wikipedia.org/wiki/Парадокс_дней_рождения
Код размещен на https://nostarch.com/big-book-small-python-projects
Теги: короткая, математическая, имитационное моделирование"""
import datetime, random

def getBirthdays(numberOfBirdays):
    """Возвращем список объектов дат для случайных дней рождения."""
    birtdays = []
    for i in range(numberOfBirdays):
        # год в нашем имитационном моделтрование роли не играет
        # лишь бы в объектах дней рождения он был одинаков
        startOfYear = datetime.date(2001,1,1)
        # Получаем слуссайный день года
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birtday = startOfYear + randomNumberOfDays
        birtdays.append(birtday)

    return birtdays

def getMathc(birthdays):
    """Возвращаем объект даты дня рождения, встречающегося
    несколько раз в списке дней рождения. """
    if len(birthdays) == len(set(birthdays)):
        return None # Все дни рождения различны, возвращаем None.

    # Сравниваем все дни рождения с друго другом попарно:
    for a, birthdayB in enumerate(birthdays):
        for b, birthdayA in enumerate(birthdays[a+1:]):
            if birthdayA == birthdayB:
                return birthdayA # возвращаем найденное соответствие

# отображения вводной информации
print("""Birthday Paradox, by AI Sweigart ai@inventwithpython.com

The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is serprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this comcept.

(it's not actually a paradox, it's just a surprising result.)""")

# Создаем кортеж названий месяцев по порядку:
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')

while True: # Запрашиваем, пока пользователь не введет допустимое значение.
    print('How many bithdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # Пользователь ввел допустимое значение
print()