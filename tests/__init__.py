#!/usr/bin/python3
class Airbnb:
    def __init__(self):
        # Initialize dictionaries to store users, listings, and bookings
        self.users = {}
        self.listings = {}
        self.bookings = {}

    def add_user(self, user_id, name, email):
        # Add a new user to the users dictionary
        self.users[user_id] = {"name": name, "email": email}

    def add_listing(self, listing_id, title, location, price_per_night):
        # Add a new listing to the listings dictionary
        self.listings[listing_id] = {"title": title, "location": location, "price_per_night": price_per_night}

    def book_listing(self, booking_id, listing_id, user_id, start_date, end_date):
        # Book a listing and add the booking details to the bookings dictionary
        self.bookings[booking_id] = {"listing_id": listing_id, "user_id": user_id, "start_date": start_date, "end_date": end_date}

    def show_listings(self):
        # Display all listings stored in the listings dictionary
        for listing_id, listing_info in self.listings.items():
            print(f"Listing ID: {listing_id}")
            for key, value in listing_info.items():
                print(f"{key.capitalize()}: {value}")
            print()

    def show_bookings(self):
        # Display all bookings stored in the bookings dictionary
        for booking_id, booking_info in self.bookings.items():
            print(f"Booking ID: {booking_id}")
            for key, value in booking_info.items():
                print(f"{key.capitalize()}: {value}")
            print()


def main():
    # Create an instance of the Airbnb class
    airbnb = Airbnb()

    while True:
        # Display the main menu options
        print("\nAirbnb Clone Command Line Interface")
        print("1. Add User")
        print("2. Add Listing")
        print("3. Book Listing")
        print("4. Show Listings")
        print("5. Show Bookings")
        print("6. Quit")

        # Get user input for choice
        choice = input("Enter your choice: ")

        # Process user choice
        if choice == "1":
            # Add a new user
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            airbnb.add_user(user_id, name, email)
            print("User added successfully.")

        elif choice == "2":
            # Add a new listing
            listing_id = input("Enter listing ID: ")
            title = input("Enter title: ")
            location = input("Enter location: ")
            price_per_night = input("Enter price per night: ")
            airbnb.add_listing(listing_id, title, location, price_per_night)
            print("Listing added successfully.")

        elif choice == "3":
            # Book a listing
            booking_id = input("Enter booking ID: ")
            listing_id = input("Enter listing ID: ")
            user_id = input("Enter user ID: ")
            start_date = input("Enter start date: ")
            end_date = input("Enter end date: ")
            airbnb.book_listing(booking_id, listing_id, user_id, start_date, end_date)
            print("Booking added successfully.")

        elif choice == "4":
            # Show all listings
            print("\nListings:")
            airbnb.show_listings()

        elif choice == "5":
            # Show all bookings
            print("\nBookings:")
            airbnb.show_bookings()

        elif choice == "6":
            # Exit the program
            print("Exiting...")
            break

        else:
            # Handle invalid choice
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Run the main function
    main()

