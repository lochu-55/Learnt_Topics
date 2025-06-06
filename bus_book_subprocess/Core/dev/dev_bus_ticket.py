from datetime import datetime
import sys
from Core.dev.Common_opts import common

class BusTicketBooking(common):

    def home_page(self):
        print("**** WELCOME TO BUS TICKET BOOKING ****")

    def read_src(self):
        print(f"Enter source (default: {self.src}): ")
        user_input = input()
        if user_input and user_input != self.src:
            self.src = user_input
            self.saved = False  # Reset saved flag when a change is made
        return self.src

    def read_dest(self):
        print(f"Enter destination (default: {self.dest}): ")
        user_input = input()
        if user_input and user_input != self.dest:
            self.dest = user_input
            self.saved = False  # Reset saved flag when a change is made
        return self.dest

    def read_date(self):
        print(f"Enter travel date (YYYY-MM-DD, default: {self.d.strftime('%Y-%m-%d')}): ")
        user_input = input()
        if user_input:
            try:
                travel_date = datetime.strptime(user_input, '%Y-%m-%d')
                if travel_date != self.d:
                    if travel_date < datetime.now():
                        print("Travel date cannot be in the past.")
                        return
                    self.d = travel_date
                    self.saved = False  # Reset saved flag when a change is made
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD format.")
        return self.d

    def read_name(self):
        print(f"Enter name (default: {self.nm}): ")
        user_input = input()
        if user_input and user_input != self.nm:
            self.nm = user_input
            self.saved = False  # Reset saved flag when a change is made
        return self.nm

    def read_age(self):
        try:
            print(f"Enter your age (default: {self.age}): ")
            user_input = input()
            if user_input:
                new_age = int(user_input)
                if new_age != self.age and new_age > 0:
                    self.age = new_age
                    self.saved = False  # Reset saved flag when a change is made
        except ValueError:
            print("Invalid age. Please enter a positive integer.")
        return self.age

    def read_phone(self):
        print(f"Enter your phone number (default: {self.ph}): ")
        user_input = input()
        if user_input and user_input != self.ph:
            if user_input.isdigit() and len(user_input) >= 10:
                self.ph = user_input
                self.saved = False  # Reset saved flag when a change is made
            else:
                print("Invalid phone number. It should contain at least 10 digits.")
        return self.ph

    def print_booking_details(self):
        return (
            f"Source: {self.src}\n"
            f"Destination: {self.dest}\n"
            f"Date: {self.d}\n"
            f"Name: {self.nm}\n"
            f"Age: {self.age}\n"
            f"Phone Number: {self.ph}"
        )

    def menu(self):
        print("\n--- Main Menu ---")
        print("1. Enter source")
        print("2. Enter destination")
        print("3. Save entered source and destination details")
        print("4. Save entered details to a file (Save As)")
        print("5. Back to Main Menu")
        print("6. Go to Submenu1")
        print("7. Go to Submenu2")
        print("8. Quit")

    def submenu1(self):
        print("\n--- Date and Name Entry ---")
        print("1. Enter travel date")
        print("2. Enter name")
        print("3. Save entered date and name")
        print("4. Save entered details to a file (Save As)")
        print("5. Back to Main Menu")
        print("6. Go to Next menu")
        print("7. Quit")

    def submenu2(self):
        print("\n--- Age and Phone Number Entry ---")
        print("1. Enter age")
        print("2. Enter phone no.")
        print("3. Save entered age and phone no.")
        print("4. Save entered details to a file (Save As)")
        print("5. Back to Main Menu")
        print("6. Back to Submenu1")
        print("7. Quit")

    def handle_main_menu(self, choice):
        switch = {
            '1': self.read_src,
            '2': self.read_dest,
            '3': self.save_details,
            '4': self.save_as,
            '5': lambda: print("Returning to Main Menu..."),
            '6': lambda: self.set_current_menu('date_name'),
            '7': lambda: self.set_current_menu('age_phno'),
            '8': self.quit,
        }
        switch.get(choice, lambda: print("Invalid option. Please try again."))()

    def handle_submenu1(self, sub_choice):
        switch = {
            '1': self.read_date,
            '2': self.read_name,
            '3': self.save_details,
            '4': self.save_as,
            '5': lambda: self.set_current_menu('main'),
            '6': lambda: self.set_current_menu('age_phno'),
            '7': self.quit,
        }
        switch.get(sub_choice, lambda: print("Invalid option. Please try again."))()

    def handle_submenu2(self, sub_choice):
        switch = {
            '1': self.read_age,
            '2': self.read_phone,
            '3': self.save_details,
            '4': self.save_as,
            '5': lambda: self.set_current_menu('main'),
            '6': lambda: self.set_current_menu('date_name'),
            '7': self.quit,
        }
        switch.get(sub_choice, lambda: print("Invalid option. Please try again."))()

    def set_current_menu(self, menu):
        self.current_menu = menu

    def quit(self):
        print("Exiting the application...")
        sys.exit(0)

    def run(self):
        self.home_page()
        self.current_menu = 'main'

        while True:
            if self.current_menu == 'main':
                self.menu()
                print("Select an option: ")
                choice = input()
                self.handle_main_menu(choice)

            elif self.current_menu == 'date_name':
                self.submenu1()
                print("Select an option: ")
                sub_choice = input()
                self.handle_submenu1(sub_choice)

            elif self.current_menu == 'age_phno':
                self.submenu2()
                print("select an option: ")
                sub_choice = input()
                self.handle_submenu2(sub_choice)


if __name__ == "__main__":
    booking = BusTicketBooking()
    booking.run()
