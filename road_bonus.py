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
  # БОНУС Знижка 10%
  if getattr(client, 'trips_count', 0) >= 3:
        price = price * 0.9  # Знижка 10%
  end_station.return_bike(bike)

  #списати гроші + порахувати заробіток
  if client.money_paid(price):
      total_revenue += price
   #щоб додати +1 до лічильника поїздок клієнта
    if hasattr(client, 'trips_count'):
            client.trips_count += 1
      
      return True
  else:
      return False



#повернути поточний заробіток
def get_total_revenue():
  return total_revenue
