"""
Создайте новый класс Buiding с атрибутом total
Создайте инициализатор для класса Buiding,
который будет увеличивать атрибут количества созданных объектов класса Building total
В цикле создайте 40 объектов класса Building и выведите их на экран командой print
Полученный код напишите в ответ к домашнему заданию
"""


class Building:
    total = 0

    def __init__(self):
        self.builds: int = 0

    def builded(self):
        while 39 >= Building.total:
            Building.total += 1
            print(f'Здание {Building.total} готово')


b = Building()
b.builded()
