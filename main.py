# Домашнее задание по теме "Потоки на классах"
# Задание: Потоки на классах в Python
#
# Цель задания:
# Освоить механизмы создания и потоков в Python.
# Практически применить знания, создав класс наследника от Thread и запустив его в потоке.
#
# Инструкции:
# Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.
#
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени потребуется рыцарю,
# чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.
#
# Пример:
# knight1 = Knight("Sir Lancelot", 10) # Низкий уровень умения
# knight2 = Knight("Sir Galahad", 20) # Высокий уровень умения
# knight1.start()
# knight2.start()
# knight1.join()
# knight2.join()
#
# Результат консоли (из-за гонки потоков может отличаться порядок вывода из потоков):
# Sir Lancelot, на нас напали!
# Sir Galahad, на нас напали!
# Sir Lancelot, сражается 1 день(дня)..., осталось 90 воинов.
# Sir Galahad, сражается 1 день(дня)...., осталось 80 воинов.
# Sir Lancelot, сражается 2 день(дня)..., осталось 80 воинов.
# Sir Galahad, сражается 2 день(дня)...., осталось 60 воинов.
# Sir Lancelot, сражается 3 день(дня)..., осталось 70 воинов.
# Sir Galahad, сражается 3 день(дня)...., осталось 40 воинов.
# Sir Lancelot, сражается 4 день(дня)..., осталось 60 воинов.
# Sir Galahad, сражается 4 день(дня)...., осталось 20 воинов.
# Sir Lancelot, сражается 5 день(дня)..., осталось 50 воинов.
# Sir Galahad, сражается 5 день(дня)...., осталось 0 воинов.
# Sir Galahad одержал победу спустя 5 дней!
# Sir Lancelot, сражается 6 день(дня)..., осталось 40 воинов.
# Sir Lancelot, сражается 7 день(дня)..., осталось 30 воинов.
# Sir Lancelot, сражается 8 день(дня)..., осталось 20 воинов.
# Sir Lancelot, сражается 9 день(дня)..., осталось 10 воинов.
# Sir Lancelot, сражается 10 день(дня)..., осталось 0 воинов.
# Sir Lancelot одержал победу спустя 10 дней!
# Все битвы закончились!
#
# Примечание:
# В классе наследника (Knight), переопределите метод run, именно там будет заложена основная логика работы потоков.
# Используйте функцию sleep из модуля time для задержки времени.

# Создать и запустить поток

import random
import time
from threading import Thread


class Knight(Thread):
    def __init__(self, name, skill, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.skill = skill

    def run(self):
        day = 0
        count_warriors = 100
        print(f'{self.name}, на нас напали!', flush=True)  # flush - небуферизованный вывод
        # while count_warriors:
        while count_warriors != 0:
            day += 1
            count_warriors -= self.skill
            print(f'{self.name}, сражается {day} день(дня)..., осталось {count_warriors} воинов', flush=True)
            time.sleep(1)

        print(f'{self.name} одержал победу спустя {day} дней!', flush=True)


knight1 = Knight("Sir Lancelot", 10)  # Низкий уровень умения
knight2 = Knight("Sir Galahad", 20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print(f'Все битвы закончились!', flush=True)

# FISH = (None, 'плотва', 'окунь', 'лещ')
# Пример из лекции
# class Fisher(Thread):
#
#     def __init__(self, name, worms, *args, **kwargs):
#         super(Fisher, self).__init__(*args, **kwargs)
#         self.name = name
#         self.worms = worms
#
#     def run(self):
#         catch = defaultdict(int)  # catch - это его улов
#         for worm in range(self.worms):
#             print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)  # flush - небуферизованный вывод
#             _ = 3 ** (random.randint(50, 70) * 10000)
#             fish = random.choice(FISH)
#             if fish is None:
#                 print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
#             else:
#                 print(f'{self.name}: Ага, у меня {fish}', flush=True)
#                 catch[fish] += 1
#
#         print(f'Итого: рыбак {self.name} поймал:', flush=True)
#         for fish, count in catch.items():
#             print(f'   {fish} - {count}', flush=True)
#
#
# vasya = Fisher(name='Вася', worms=10)
# kolya = Fisher(name='Коля', worms=10)
#
# print('.' * 20, 'Они пошли на рыбалку')
#
# vasya.start()
# kolya.start()
#
# print('.' * 20, 'Ждем, пока они вернутся...')
#
# vasya.join()
# kolya.join()
#
# print('.' * 20, 'Итак, они вернулись')


# -------------------------------------------------------------------------

# Если нужен результат выполнения, то просто делаем атрибут класса
# class Fisher(Thread):
#
#     def __init__(self, name, worms, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.worms = worms
#         self.catch = defaultdict(int)
#
#     def run(self):
#         self.catch = defaultdict(int)  # catch - это его улов
#         for worm in range(self.worms):
#             print(f'{self.name}: Червяк № {worm} - Забросил, ждем...', flush=True)  # flush - небуферизованный вывод
#             _ = 3 ** (random.randint(50, 70) * 10000)
#             fish = random.choice(FISH)
#             if fish is None:
#                 print(f'{self.name}: Тьфу, сожрали червяка...', flush=True)
#             else:
#                 print(f'{self.name}: Ага, у меня {fish}', flush=True)
#                 self.catch[fish] += 1
#
# vasya = Fisher(name='Вася', worms=10)
# kolya = Fisher(name='Коля', worms=10)
#
# print('.' * 20, 'Они пошли на рыбалку')
#
# vasya.start()
# kolya.start()
#
# print('.' * 20, 'Ждем, пока они вернутся...')
#
# vasya.join()
# kolya.join()
#
# print('.' * 20, 'Итак, они вернулись')
#
# for fisher in (vasya, kolya):
#     print(f'Итого: рыбак {fisher.name} поймал:')
#     for fish, count in fisher.catch.items():
#         print(f'   {fish} - {count}')
