# models.py

class Route:
    def __init__(self, route_code, route_name, capacity, available_seats, fare, departure_time):
        self.route_code = route_code
        self.route_name = route_name
        self.capacity = int(capacity)
        self.available_seats = int(available_seats)
        self.fare = float(fare)
        self.departure_time = departure_time

    def __str__(self):
        return f"{self.route_code} | {self.route_name} | Cap: {self.capacity} | Avail: {self.available_seats} | Fare: ${self.fare} | Time: {self.departure_time}"

class Passenger:
    def __init__(self, passenger_id, passenger_name, phone):
        self.passenger_id = passenger_id
        self.passenger_name = passenger_name
        self.phone = phone

    def __str__(self):
        return f"{self.passenger_id} | {self.passenger_name} | {self.phone}"

class Booking:
    def __init__(self, booking_id, route_code, passenger_id, seats_booked, booking_time):
        self.booking_id = booking_id
        self.route_code = route_code
        self.passenger_id = passenger_id
        self.seats_booked = int(seats_booked)
        self.booking_time = booking_time

    def __str__(self):
        return f"{self.booking_id} | Route: {self.route_code} | Pass: {self.passenger_id} | Seats: {self.seats_booked} | Time: {self.booking_time}"

# --- Node Classes ---
class BSTNode:
    def __init__(self, route_data):
        self.data = route_data
        self.left = None
        self.right = None

class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None