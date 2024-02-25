class Passenger:
    def __init__(self, name):
        self.name = name
        self.ticket = None
        self.boarding_pass = None
        self.baggage_checked = False
        self.seat_assigned = False

    def set_ticket(self, ticket):
        self.ticket = ticket

    def get_name(self):
        return self.name

    def get_ticket(self):
        return self.ticket

    def set_boarding_pass(self, boarding_pass):
        self.boarding_pass = boarding_pass

    def get_boarding_pass(self):
        return self.boarding_pass

    def set_baggage_checked(self, status):
        self.baggage_checked = status

    def is_baggage_checked(self):
        return self.baggage_checked

    def set_seat_assigned(self, status):
        self.seat_assigned = status

    def is_seat_assigned(self):
        return self.seat_assigned

    def __str__(self):
        return f"Passenger: {self.name}"


class Flight:
    def __init__(self, flight_number, departure_location, arrival_location, scheduled_departure_time, scheduled_arrival_time):
        self.flight_number = flight_number
        self.departure_location = departure_location
        self.arrival_location = arrival_location
        self.scheduled_departure_time = scheduled_departure_time
        self.scheduled_arrival_time = scheduled_arrival_time
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)

    def get_flight_number(self):
        return self.flight_number

    def get_departure_location(self):
        return self.departure_location

    def get_arrival_location(self):
        return self.arrival_location

    def get_scheduled_departure_time(self):
        return self.scheduled_departure_time

    def get_scheduled_arrival_time(self):
        return self.scheduled_arrival_time

    def __str__(self):
        return f"Flight {self.flight_number} from {self.departure_location} to {self.arrival_location}, Departure: {self.scheduled_departure_time}, Arrival: {self.scheduled_arrival_time}"


class Ticket:
    def __init__(self, ticket_number, ticket_type, electronic_ticket_number, passenger, flight):
        self.ticket_number = ticket_number
        self.ticket_type = ticket_type
        self.electronic_ticket_number = electronic_ticket_number
        self.passenger = passenger
        self.flight = flight

    def get_ticket_number(self):
        return self.ticket_number

    def get_ticket_type(self):
        return self.ticket_type

    def get_electronic_ticket_number(self):
        return self.electronic_ticket_number

    def get_passenger(self):
        return self.passenger

    def get_flight(self):
        return self.flight

    def __str__(self):
        return f"Ticket {self.ticket_number} Type: {self.ticket_type}, Electronic Ticket Number: {self.electronic_ticket_number}"


class BoardingPass:
    def __init__(self, flight, passenger, gate, seat_number):
        self.flight = flight
        self.passenger = passenger
        self.gate = gate
        self.seat_number = seat_number

    def get_flight(self):
        return self.flight

    def get_passenger(self):
        return self.passenger

    def get_gate(self):
        return self.gate

    def get_seat_number(self):
        return self.seat_number

    def __str__(self):
        return f"Boarding Pass for {self.passenger} - Flight {self.flight.get_flight_number()}, Gate: {self.gate}, Seat: {self.seat_number}"

# Create a Passenger
passenger1 = Passenger("James Smith")

# Create a Flight
flight1 = Flight("NA4321", "Chicago ORD", "New York JFK", "11:40", "13:30")

# Create a Ticket
ticket1 = Ticket("629", "First class", 123456789, passenger1, flight1)
passenger1.set_ticket(ticket1)

# Create a Boarding Pass
boarding_pass1 = BoardingPass(flight1, passenger1, "Gate 03", "09A")
passenger1.set_boarding_pass(boarding_pass1)

# Display Boarding Pass details
print("Boarding Pass Details:")
print("Passenger:", passenger1.get_name())
print("Flight:", boarding_pass1.get_flight())
print("Gate:", boarding_pass1.get_gate())
print("Seat:", boarding_pass1.get_seat_number())


