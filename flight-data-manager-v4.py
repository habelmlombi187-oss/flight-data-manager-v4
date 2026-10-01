import json

flights = {
    
    "Flight_1":{"Aircraft":"Boeing 737","Speed":230 ,"Altitude":1000,"Fuel":5000},
    "Flight_2":{"Aircraft":"Airbus A320","Speed":220,"Altitude":9500 ,"Fuel":4800}

    }
def add_flight(flights):
    try:
        name = input("\nEnter the name of the flight :").strip().title()
        aircraft = input("Enter the name of the aircraft :").strip().title()
        velocity = float(input("Enter the speed of the aircraft (m/s) :"))
        altitude = float(input("Enter the altitude of the aircraft (m) :"))
        fuel = float(input("Enter the total capacity of fuel the aircraft carries (kg) :"))
        if name and aircraft :
            flights[name] = {
                "Aircraft" : aircraft,
                "Speed" : velocity ,
                "Altitude" : altitude,
                "Fuel" : fuel
                }
            print("The new fligt :", {name}, "has been added successfully.")
    except ValueError:
        print("Invalid input!! Make sure you fill all the details and that speed,altitude and fuel are digits.")

def save_flights(flights, filename = "flights.json"):
    with open (filename, "w") as file:
        json.dump(flights, file, indent = 4)

def load_flights(filename = "flights.json"):
    try:
        with open (filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return{}
    except json.JSONDecodeError:
        print("Saved file is corrupted. Starting fresh.")
        return{}


def display_flight(name,flight_info):
    print (f"\nThe flight is {name}")
    print (f"The type of the aircraft is ", flight_info["Aircraft"])
    print (f"The speed of the aircraft is ", flight_info["Speed"],"m/s.")
    print (f"The altitude of the aircraft is ", flight_info["Altitude"],"m.")
    print(f"The fuel needed by the aircraft is ", flight_info["Fuel"],"kg")

def view_flights(flights):
    for name, flight_info in flights.items():
        display_flight(name,flight_info)
    

def search_flight(flights):
    name = input("Enter the name of the flight you want to view :").strip().title()
    flight_info = flights.get(name)
    if flight_info :
        display_flight(name,flight_info) 
    else:
        print(f"The specified flight {name} does not exist in the system.")


def update_flight(flights):
    name = input("Enter the name of the flight to update: ").strip().title()

    if name not in flights:
        print(f"Flight {name} does not exist in the system.")
        return
    print(f"\nCurrent details for {name}: ")
    for key, value in flights[name].items():
        print(f" {key}: {value}")

    field = input("\nWhich field do you want to update? (Aircraft/Speed/Altitude/Fuel): ").strip().title()
    if field not in flights[name]:
        print(f"'{field}' is not a valid field.")
        return
    new_value = input (f"Enter the new value for {field}: ").strip()
#conversion of numeric fields
    if field in ("Speed", "Altitude", "Fuel"):
        try:
            new_value = float(new_value)
        except ValueError:
            print(f"'{new_value}' is not a valid number.")
            return
    flights[name][field] = new_value
    print (f"{field} for {name} updated successfully.")

def max_altitude (flights):
    if not flights:
        print("There are no flights in the system.")
        return
    highest_flight = max(flights, key= lambda flight: flights [flight]["Altitude"])
    altitude = flights[highest_flight]["Altitude"]
    print(f"The flight : {highest_flight}, has the highest altitude of {altitude}m.") 

def max_speed (flights):
    if not flights:
        print("There are no flights in the system.")
        return
    fastest_flight = max(flights, key = lambda flight: flights[flight]["Speed"])
    speed = flights[fastest_flight]["Speed"]
    print(f"The fastest flight is {fastest_flight} with velocity of {speed} m/s.")

def delete_flight (flights):
    name = input ("Enter the name of the flight to delete: ").strip().title()

    if name not in flights:
        print (f"Flight {name} does not exist in the system.")
        return
    print(f"\nYou are about to delete:")
    display_flight(name, flights[name])

    confirm = input(f"Are you sure you want to delete {name}? (yes/no) .").strip().lower()
    if confirm == "yes":
        del flights[name]
        save_flights(flights)
        print(f"Flight {name} has been deleted successfully.")
    else:
        print("Deletion cancelled.")

def delete_all_flights (flights):
    if not flights:
        print("Tere are no flights to delete.")
        return
    confirm = input(f"Delete all {len(flights)} flights? This cannot be undone.(yes/no): ").strip().lower()
    if confirm == "yes":
        flights.clear()
        save_flights(flights)
        print("All flights have been deleted successffully.")
    else:
        print("Deletion cancelled.")
        
def main ():
    flights = load_flights()
    
    while True:
        print()
        print("-"*5,"FLIGHT DATA MANAGER MAIN MENU","-"*5)
        print("1. Add Flight.")
        print("2. View Flight.")
        print("3. Search Flight.")
        print("4. Update data.")
        print("5. Delete flight.")
        print("6. Delete all flights.")
        print("7. Find flight with highest altitude.")
        print("8. Find flight with the highest speed.")
        print("9. Exit.")
        choice = input("\n Choose from above menu what you want to do.(from 1 to 9)").strip()

        if choice == "1":
            add_flight(flights)
            save_flights(flights)
        elif choice == "2":
            view_flights(flights)
        elif choice == "3":
            search_flight(flights)
        elif choice == "4":
            update_flight(flights)
            save_flights(flights)
        elif choice == "5":
            delete_flight(flights)
        elif choice == "6":
            delete_all_flights(flights)
        elif choice == "7":
            max_altitude(flights)
        elif choice == "8":
            max_speed(flights)
        elif choice == "9":
            save_flights(flights)
            print ("Thankyou for your time. Exiting the calculator now.")
            break
        else:
            print("Invalid input !! Please choose from option 1 to 9.")
            

if __name__ == "__main__":
    main()
        
    

    

    
    



    
    
