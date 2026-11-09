class Bicycle:
    def __init__(self, number, bike_type): # створює велосипед: номер і тип("звичайний" / "електричний")
        pass

    def cost(self, minutes): # рахує вартість поїздки
        pass


class Station:
    def __init__(self, name, bikes): # створює станцію
        pass

    def find_bike(self, bike_type): # шукає на станції перший велосипед потрібного тип, повертає його номер або None, якщо такого немає
        pass

    def take_bike(self, number): # прибирає велосипед з цим номером зі станції
        pass

    def return_bike(self, bike):  # додає велосипед на станцію нічого не повертає 
        pass

    def bike_count(self): # повертає кількість велосипедів на станції
        pass
