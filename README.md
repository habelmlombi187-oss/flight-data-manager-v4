# Flight Data Manager

A beginner-friendly Python command-line application for managing flight data.

The program allows users to add, view, search, update, and delete flight records. Flight data is stored in a JSON file so that information can be saved and loaded between program sessions.

## Features

- Add a new flight
- View all flights
- Search for a specific flight
- Update flight information
- Delete a flight
- Delete all flights
- Find the flight with the highest altitude
- Find the flight with the highest speed
- Save flight data to a JSON file
- Load saved flight data when the program starts
- Basic input validation and error handling

## Flight Information

Each flight can contain:

- Flight name/number
- Aircraft type
- Speed (m/s)
- Altitude (m)
- Fuel capacity (kg)

## Technologies Used

- Python
- Dictionaries
- Functions
- JSON
- File handling
- Exception handling
- Lambda functions
- Command-line input/output

## Project Structure

```text
flight-data-manager/
│
├── flight_manager.py
├── flights.json
└── README.md
```

## How to Run

Make sure Python is installed on your computer.

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/flight-data-manager.git
```

Move into the project directory:

```bash
cd flight-data-manager
```

Run the program:

```bash
python flight_manager.py
```

## Main Menu

The application provides the following options:

```text
1. Add Flight
2. View Flight
3. Search Flight
4. Update data
5. Delete flight
6. Delete all flights
7. Find flight with highest altitude
8. Find flight with highest speed
9. Exit
```

## Example

A flight record can look like:

```text
Flight_1
Aircraft: Boeing 737
Speed: 230 m/s
Altitude: 1000 m
Fuel: 5000 kg
```

## What I Learned

This project was created as a Python practice project to strengthen my understanding of:

- Writing and organizing functions
- Working with dictionaries
- Reading and writing JSON files
- Handling user input
- Handling exceptions with `try` and `except`
- Searching and updating data
- Using `lambda` functions
- Building a complete command-line application
- Organizing a project for Git and GitHub

## Future Improvements

Possible future versions of this project may include:

- Object-oriented programming with `Flight` classes
- Encapsulation and `@property`
- Passenger and cargo flight subclasses
- Better input validation
- Flight sorting and filtering
- A graphical user interface
- Unit testing
- More aircraft performance calculations

## Author

I created this as a Python learning and portfolio project.
