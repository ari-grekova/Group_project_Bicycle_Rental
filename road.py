#взяти змінні з файлів дівчат
from bikes import Bicycle, Station
from client import Client

total_revenue = 0.0
#весь процес, коли клієнт бере велосипед, катається та повертає його
def make_trip(client: Client, start_station: Station, end_station: Station, bike_number: int, min: int):
  global total_revenue
  bike = start_station.take_bike(bike_number) #забираємо велік
  if bike is None:
        return False
  
  #повертає велік та рахує ціну
  price = bike.cost(min)
  end_station.return_bike(bike)

  #списати гроші + порахувати заробіток
  if client.money_paid(price):
        total_revenue += price
        return True
    else:
        return False



#повернути поточний заробіток
def get_total_revenue():
  return total_revenue
  
