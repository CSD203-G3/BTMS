# main.py
from system import BusTicketSystem

def print_menu():
    print("\n" + "="*40)
    print(" BUS TICKET MANAGEMENT SYSTEM (BTMS)")
    print("="*40)
    print("1. Load Route Data")
    print("2. Insert New Route")
    print("3. Display Routes (In-order)")
    print("4. Display Routes (BFS)")
    print("5. Delete Route by Code")
    print("6. Balance BST Routes")
    print("7. Add New Passenger")
    print("8. Display Passengers")
    print("9. Process New Booking")
    print("10. Display All Bookings")
    print("11. Sort Bookings (Route + Passenger)")
    print("12. View Daily Revenue")
    print("13. View Popular Routes")
    print("14. Cancel Booking")
    print("0. Exit")
    print("="*40)

def main():
    sys = BusTicketSystem()
    while True:
        print_menu()
        choice = input("Select an option: ")
        
        if choice == '1': sys.load_routes()
        elif choice == '2':
            sys.add_route(
                input("Code: "), input("Name: "), input("Capacity: "), 
                input("Available Seats: "), input("Fare: "), input("Time: ")
            )
        elif choice == '3': sys.display_routes_inorder()
        elif choice == '4': sys.display_routes_bfs()
        elif choice == '5': sys.delete_route(input("Enter Route Code to delete: "))
        elif choice == '6': 
            sys.routes_bst.balance()
            print("BST Balanced!")
        elif choice == '7': sys.add_passenger(input("ID: "), input("Name: "), input("Phone: "))
        elif choice == '8': sys.display_passengers()
        elif choice == '9': sys.process_booking(input("Booking ID: "), input("Route Code: "), input("Passenger ID: "), input("Seats: "))
        elif choice == '10': sys.display_bookings()
        elif choice == '11': 
            sys.bookings_ll.sort_bookings()
            print("Bookings sorted!")
            sys.display_bookings()
        elif choice == '12': sys.daily_revenue()
        elif choice == '13': sys.popular_routes()
        elif choice == '14': sys.cancel_booking(input("Enter Booking ID to cancel: "))
        elif choice == '0':
            print("Exiting BTMS. Don't forget to push to Git!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()