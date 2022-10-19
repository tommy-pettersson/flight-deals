class FlightData:
    
    def __init__(self, city_from, airport_from, city_to, airport_to, price, date) -> None:
        self.departure_city = city_from
        self.departure_airport = airport_from
        self.destination_city = city_to
        self.destination_airport = airport_to
        self.price = price
        self.departure_date = date

    