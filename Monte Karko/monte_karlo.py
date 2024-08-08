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