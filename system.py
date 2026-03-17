# system.py
import os
from datetime import datetime
from models import Route, Passenger, Booking
from data_structures import BinarySearchTree, LinkedList

class BusTicketSystem:
    def __init__(self):
        self.routes_bst = BinarySearchTree()
        self.passengers_ll = LinkedList()
        self.bookings_ll = LinkedList()

    # ================= 1. BUS ROUTES MANAGEMENT =================
    def load_routes(self, filename="routes.txt"):
        if not os.path.exists(filename):
            print("File not found.")
            return
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 6:
                    r = Route(parts[0].strip(), parts[1].strip(), parts[2].strip(), 
                              parts[3].strip(), parts[4].strip(), parts[5].strip())
                    self.routes_bst.insert(r)
        print("Routes loaded successfully.")

    def add_route(self, code, name, cap, avail, fare, time):
        if self.routes_bst.search(code):
            print("Error: Route code must be unique!")
            return
        r = Route(code, name, cap, avail, fare, time)
        self.routes_bst.insert(r)
        print("Route added successfully.")

    def display_routes_inorder(self):
        routes = self.routes_bst.inorder(self.routes_bst.root)
        for r in routes: print(r)

    def display_routes_bfs(self):
        routes = self.routes_bst.bfs()
        for r in routes: print(r)

    def save_routes_inorder(self, filename="routes_saved.txt"):
        routes = self.routes_bst.inorder(self.routes_bst.root)
        with open(filename, 'w') as f:
            for r in routes:
                f.write(f"{r.route_code},{r.route_name},{r.capacity},{r.available_seats},{r.fare},{r.departure_time}\n")
        print("Routes saved.")

    def delete_route(self, code):
        node = self.routes_bst.search(code)
        if node:
            self.routes_bst.delete_by_copy(code)
            print("Route deleted.")
        else:
            print("Route not found.")

    # ================= 2. PASSENGER LIST =================
    def load_passengers(self, filename="passengers.txt"):
        if not os.path.exists(filename): return
        with open(filename, 'r') as f:
            for line in f:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    p = Passenger(parts[0].strip(), parts[1].strip(), parts[2].strip())
                    self.passengers_ll.add_last(p)
        print("Passengers loaded.")

    def add_passenger(self, pid, name, phone):
        if self.passengers_ll.search_passenger(pid):
            print("Error: Passenger ID must be unique!")
            return
        if not phone.isdigit():
            print("Error: Phone must contain digits only!")
            return
        p = Passenger(pid, name, phone)
        self.passengers_ll.add_last(p)
        print("Passenger added.")

    def display_passengers(self):
        for p in self.passengers_ll.get_all(): print(p)

    def save_passengers(self, filename="passengers_saved.txt"):
        with open(filename, 'w') as f:
            for p in self.passengers_ll.get_all():
                f.write(f"{p.passenger_id},{p.passenger_name},{p.phone}\n")
        print("Passengers saved.")

    # ================= 3. BOOKING LIST =================
    def process_booking(self, bid, rcode, pid, seats):
        route_node = self.routes_bst.search(rcode)
        if not route_node:
            print("Error: Route not found.")
            return
        if not self.passengers_ll.search_passenger(pid):
            print("Error: Passenger not found.")
            return
        
        route = route_node.data
        seats = int(seats)
        if seats > route.available_seats:
            print(f"Error: Not enough seats! Only {route.available_seats} available.")
            return

        # Update seats & record booking
        route.available_seats -= seats
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        b = Booking(bid, rcode, pid, seats, now)
        self.bookings_ll.add_last(b)
        print("Booking successful!")

    def display_bookings(self):
        for b in self.bookings_ll.get_all(): print(b)

    def cancel_booking(self, bid):
        bookings = self.bookings_ll.get_all()
        target_booking = next((b for b in bookings if b.booking_id == bid), None)
        if target_booking:
            route_node = self.routes_bst.search(target_booking.route_code)
            if route_node:
                route_node.data.available_seats += target_booking.seats_booked
            self.bookings_ll.delete_booking(bid)
            print("Booking cancelled and seats refunded.")
        else:
            print("Booking ID not found.")

    def daily_revenue(self):
        revenue = 0
        for b in self.bookings_ll.get_all():
            route_node = self.routes_bst.search(b.route_code)
            if route_node:
                revenue += route_node.data.fare * b.seats_booked
        print(f"Total Daily Revenue: ${revenue:.2f}")

    def popular_routes(self):
        counts = {}
        for b in self.bookings_ll.get_all():
            counts[b.route_code] = counts.get(b.route_code, 0) + b.seats_booked
        sorted_routes = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        print("Most Popular Routes (by seats booked):")
        for code, count in sorted_routes:
            route_name = self.routes_bst.search(code).data.route_name
            print(f"- {code} ({route_name}): {count} seats")