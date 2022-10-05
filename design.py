
# Name:         Parker Donahue
# Class:        CSC 110 - Fall 2021
# Assignment:   Programming projest Design
# Due Date:     November 12, 2021


# Program Title:  Airline Flight Scheduling
# -----------------------------------------


# Project Description:
# --------------------
# This program will read a data file given by the user.
# The program will sort each value type into a list, allowing the user access accurate information.
# The program will provide the user with 6 functional options, and an option to quit.
# Each option will display the information it is meant to
# The program will again display the options after the requested information is displayed, until the user quits with an input of 7


# General Solution:
# -----------------
# Create 5 lists containing the unique values
# Create a run boolean and a while loop checking if the user has quit yet
# The loop is used to: Display the options for functions, then the information based on the user input,
# then repeat until the user has quit


# PsuedoCode:
# -----------
#   Prompt user to input file name, handling exceptions until file name is valid. open_file()
#   Sort the data file into 5 lists: Airlines, Flight Numbers, Dep Times, Arr Times, Prices. get_data()
#
#   While the user has not quit
#           Display the 7 options
#           Prompt the user for input with the display, 'Choice ->'. Handling exceptions
#           If input is 1
#               execute to find flight information by airline and flight number. find_specified_flight()
#               display information. display()
#           If input is 2
#               execute to fight flights shorter than specified duration. shorter_than_specified()
#               display information. display()
#           If input is 3
#               execute to find the cheapest flight of a given airline. cheapest_flight()
#               display information. display()
#           If input is 4
#               execute to find flights departing
#               display information. display()
#           If input is 5
#               execute to find the average price of flights in a given airline. average_price_all()
#               display information. display()
#           If input is 6
#               execute to sort flights by departure and write them in order in new file. new_file()
#               display information. display()
#           If input is 7
#               user has quit
#               exit the while loop


# Function Design:
# ----------------

def open_file():
    # This function will run the exception handling to check if the file input is valid.
    # it will return the valid file name.
    goodFile = False
    while goodFile == False:
        fname = input("Enter file name: ")
        try:
            gradeFile = open(fname,'r')
            goodFile = True
        except IOError:
            print("Invalid filename, try again")
    return gradeFile


def get_data():
    flightFile = openFile()
    airlineList = []
    flightNumList = []
    deppList = []
    arrList = []
    priceList = []

    for line in flightFile:
        line = line.strip()
        airline, flightNum, depp, arr, price = line.split(',')
        airlineList.append(airline)
        flightNumList.append(flightNum)
        deppList.append(depp)
        arrList.append(arr)
        priceList.append(price)

    flightFile.close()
    return airlineList, flightNumList, deppList, arrList, priceList
    # This function will parse the text file, splitting the data into 5 lists for each type of value.
    # it will return the 5 LISTS: Ariline, Flight Number, Departure Time, Arrival Time, Price.

def display(value_to_display):
    print(value_to_display)
    return
    # This function will print the parameter value.
    # it will return nothing, only execute and display

def display_choice():

    print("\nPlease choose one of the following options:" ,
          "\n1 -- Find flight information by airline and flight number" ,
          "\n2 -- Find flights shorter than a specified duration" ,
          "\n3 -- Find the cheapest flight by a given airline" ,
          "\n4 -- Find flight departing after a specified time" ,
          "\n5 -- Find the average price of all flights" ,
          "\n6 -- Write a file with flights sorted by departure time" ,
          "\n7 -- Quit")
    # This will repeat the option displaying, after every interaction, until the user has quit
    # it will return nothing, only execute and display
def input_check(input, listCheck):
    found = False

    try:
        x = listCheck.index(input)
        found = True
        goodInput = input

    except IOError:
        print("Invalid input -- try again")
    return goodInput


def find_specific_flight(airlines, flightNums, depps, arrs, prices):
    airline = input("Enter airline name:")
    goodAirline = input_check(airline, airlines)
    flight = input("Enter flight number:")
    goodFlight = input_check(flight, flight)
    for i in airlines:
        if i == goodAirline:
            airLineIndex = i
            for j in flightNum:
                if j == goodFlight:
                    goodFlightIndex = j
                    if j == i:
                        return airlines[j], flightNums[j], depps[j], arrs[j], prices[j]


    # This function will ask the user for an arline and a flight number, handling exceptions.
    # it will return the 5 VALUES belonging to the flight entered.

def shorter_than_specified():
    # This function will ask the user for a maximum flight duration, handling exceptions, calculate the duration, and compare the duration to all other flights.
    # it will return a LIST of flights whos duration is less than the specified maximum.

def cheapest_flight():
    # This function will prompt the user to input a specified arline, handling excptions, then find the cheapest flight provided by that airline.
    # it will return the 5 VALUES in order, belonging to the cheapest flight found.

def after_specified_time():
    # This function will prompt the user ot input a time, handling exceptions, then create a list of flights whos departure time is greater than the input.
    # it will return the LIST of later departures.

def average_price_all():
    # This function will prompt the user to enter an airline, then find the average of all the price values belonging to the specified airline.
    # it will return the average price VALUE.

def new_file():
    # This function will sort the flights by departure time, then create a new file and write all information about each flight in order of departure.
    # it will return nothing, only execute and create the file.
def choice_check(selection):
    found = False
    seven = {1, 2, 3, 4, 5, 6, 7}
    while found == False:
        try:
            # catches the error
            x = seven.index(selection)
            goodChoice = selection
            found = True
        except TypeError:
            print("Entry must be a number")
        except ValueError:
            print("Entry must be between 1 and 7")
        return goodChoice

def main():
    run = True
    while run == True:
        display_choice()

    filename = open_file()
    airlines, flightNums, depps, arrs, prices = get_data()
    print(airlines)

    selection = input(display_choice())
    goodSelection = choice_check(selection)


#    This function impliments the pseudocde, using the functions above and abiding by the logic of the pseudocode.


