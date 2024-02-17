#  Класс Авиабилет должен содержать данные о рейсе, дате, месте и стоимости.
#  Методы должны позволять бронировать билеты, отменять
#  бронь и просматривать доступные рейсы.


class Tickets:    
    def __init__(self, flight_number, departure_airport, arrival_airport, flight_date, flight_cost):
        self.flight_number = flight_number
        self.flight_date = flight_date
        self.flight_cost = flight_cost
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
    # действия, которые данный клас может делать
    
    def booking(self):
        print(f'Ticket on flight {self.flight_number} from {self.departure_airport} to {self.arrival_airport} - {self.flight_date} booking')

    def cancellation(self):
        print(f'Ticket on flight {self.flight_number} from {self.departure_airport} to {self.arrival_airport} - {self.flight_date} cancellation')


flight_to_Moskow = Tickets('SU1319', 'Murmansk', 'Moscow','14.02.2024', '13000')
flight_from_Moskow = Tickets('SU1318', 'Moscow', 'Murmansk','14.03.2024', '15700')
flight_to_Moskow.booking()
flight_from_Moskow.cancellation()
