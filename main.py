from bikes import Bicycle, Station
from client import Client
from road import make_trip, get_total_revenue

REGULAR = "звичайний"
ELECTRIC = "електричний"
TYPE_NAMES = {REGULAR: "звичайних", ELECTRIC: "електричних"}


def trip(client, start, end, bike_type, minutes):
    name = client.get_name()

    number = start.find_bike(bike_type)
    if number is None:
        return f"{name}: на станції {start.name} 0 {TYPE_NAMES[bike_type]} велосипедів"

    before = get_total_revenue()
    if make_trip(client, start, end, number, minutes):
        cost = get_total_revenue() - before
        return (f"{name}: {bike_type} велосипед, зі станції {start.name} "
                f"на станцію {end.name}, {minutes} хв, {cost:g} грн")
    return f"{name}: не вистачає грошей на поїздку"


def report(stations):
    print("Звіт адміністратора:")
    for station in stations:
        print(f"Станція {station.name}: велосипедів — {station.bike_count()}")
    print(f"Загальна виручка мережі: {get_total_revenue():g} грн")


def run_checks():
    assert Bicycle(1, REGULAR).cost(10) == 20
    assert Bicycle(2, ELECTRIC).cost(10) == 50
    assert Station("Порожня", []).take_bike(1) is None


def main():
    station_1 = Station("1", [Bicycle(1, REGULAR), Bicycle(2, ELECTRIC), Bicycle(3, REGULAR)])
    station_2 = Station("2", [Bicycle(4, ELECTRIC)])
    stations = [station_1, station_2]

    kristina = Client("Крістіна", 500)
    yarik = Client("Ярік", 120)

    print("Початковий стан:")
    for station in stations:
        print(f"Станція {station.name}: велосипедів — {station.bike_count()}")

    print("\nПоїздки:")
    print(trip(kristina, station_2, station_1, ELECTRIC, 20))
    print(trip(yarik, station_2, station_1, REGULAR, 15))
    print(trip(yarik, station_1, station_2, REGULAR, 50))
    print(trip(kristina, station_1, station_2, ELECTRIC, 40))
    print(trip(yarik, station_2, station_1, ELECTRIC, 10))

    print("\nБаланси:")
    for client in (kristina, yarik):
        print(f"{client.get_name()}: {client.get_balance()} грн")

    print()
    report(stations)


if name == "main":
    run_checks()
    main()
