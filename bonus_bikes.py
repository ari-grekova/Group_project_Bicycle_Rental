PRICE_PER_MINUTE = { "звичайний": 2, "електричний": 5}


class Bicycle:
    def __init__(self, number, bike_type, charge): # створює велосипед: номер і тип("звичайний" / "електричний") ++ рівень заряду
        self.number = number
        self.bike_type = bike_type
        self.charge = charge

    def is_low_charge(self): 
        return self.bike_type == "електричний" and self.charge < 20

    def cost(self, minutes): # рахує вартість поїздки
        return minutes * PRICE_PER_MINUTE[self.bike_type]
        

class Station:
    def __init__(self, name, bikes): # створює станцію
        self.name = name
        self.bikes = list(bikes) 

    def find_bike(self, bike_type):  # повертає номер першого велосипеда потрібного типу, який МОЖНА видати + (без низького заряду), або Nonee
        for bike in self.bikes:
            if bike.bike_type == bike_type and not bike.is_low_charge():
                return bike.number
        return None
    def low_charge_bikes(self):  # повертає список для велосипедів з низьким зарядом
        return [(bike.number, self.name, bike.charge)
                for bike in self.bikes if bike.is_low_charge()]
      
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
