PRICE_PER_MINUTE = { "звичайний": 2, "електричний": 5}


class Bicycle:
    def __init__(self, number, bike_type): # створює велосипед: номер і тип("звичайний" / "електричний")
        self.number = number
        self.bike_type = bike_type

    def cost(self, minutes): # рахує вартість поїздки
        return minutes * PRICE_PER_MINUTE[self.bike_type]
        

class Station:
    def __init__(self, name, bikes): # створює станцію
        self.name = name
        self.bikes = list(bikes) 

    def find_bike(self, bike_type): # шукає на станції перший велосипед потрібного тип, повертає його номер або None, якщо такого немає
        for bike in self.bikes:
            if bike.bike_type == bike_type:
                return bike.number
        return None

    def take_bike(self, number): # прибирає велосипед з цим номером зі станції
        for bike in self.bikes:
            if bike.number == number:
                self.bikes.remove(bike)
                return bike
        return None

    def return_bike(self, bike):  # додає велосипед на станцію (нічого не повертає )
        self.bikes.append(bike)


    def bike_count(self): # повертає кількість велосипедів на станції
        return len(self.bikes)
