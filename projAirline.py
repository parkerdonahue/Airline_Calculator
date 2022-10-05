
# Name:         Parker Donahue
# Class:        CSC 110 - Fall 2021
# Assignment:   Programming project implementation
# Due Date:     December 14, 2021

# Program Title:  Airline Calculator
# -----------------------------------------

# Project Description:
# --------------------
# This program will read a data file given by the user.
# The program will sort each value type into a list, allowing the user access accurate information.
# The program will provide the user with 6 functional options, and an option to quit.
# Each option will display the information it is meant to
# The program will again display the options after the requested information is displayed,
# until the user quits with an input of 7

# General Solution:
# -----------------
# Create 5 lists containing the unique values
# Create a run boolean and a while loop checking if the user has quit yet
# The loop is used to: Display the options for functions, then the information based on the user input,
# then repeat until the user has quit

# run the exception handling to check if the file input is valid.
# return the valid file name.
def open_file():

    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            flightFile = open(fname,'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again ...")
    return flightFile

# takes in value
# prints it
def display(value_to_display):
    print(value_to_display)
    return
    # This function will print the parameter value.
    # it will return nothing, only execute and display

# verifies choice is valid, altering error message
def choice_check():
        # boolean to end function
        found = False
        # list containing possible values
        seven = ['1', '2', '3', '4', '5', '6', '7']
        # executing if found has yet to be set to True
        while found == False:
            # takes input from user for choice
            choice = input("Choice ==> ")
            try:
                # catches error of non number
                y = int(choice)
                try:
                    # catches error of outside of 1 - 7
                    x = seven.index(choice)
                    # confirms choice
                    goodChoice = choice
                    # ends process when found
                    found = True
                    # returns the confirmed choice
                    return goodChoice

                except ValueError:
                    print("Entry must be between 1 and 7")

            except ValueError:
                print("Entry must be a number")

#   uses the file confirmation function to take in file name
#   sorts the values into 5 unique lists for manipulation
def get_data():

    flightFile = open_file()
    airlineList = []
    flightNumList = []
    deppList = []
    arrList = []
    priceList = []

    # goes through every line of the input file
    for line in flightFile:
        # strips line of white space
        line = line.strip()
        # seperates strings at ,
        airline, flightNum, depp, arr, price = line.split(',')
        # adds all values to unique list
        airlineList.append(airline)
        flightNumList.append(flightNum)
        deppList.append(depp)
        arrList.append(arr)
        # edits price, removing $ and replacing it with blank
        # adds after alteration
        price = price.replace('$','')
        priceList.append(price)

    # closes input file
    flightFile.close()
    return airlineList, flightNumList, deppList, arrList, priceList

#   This function will print the parameter value.
#   it will return nothing, only execute and display
def display(value_to_display):
    print(value_to_display)
    return

#   displays the main menu
def display_choice():

    # concatenates and prints
    print("\n" + "Please choose one of the following options:" + "\n"+
          "1 -- Find flight information by airline and flight number" +"\n"+
          "2 -- Find flights shorter than a specified duration" +"\n"+
          "3 -- Find the cheapest flight by a given airline" +"\n"+
          "4 -- Find flight departing after a specified time" +"\n"+
          "5 -- Find the average price of all flights" +"\n"+
          "6 -- Write a file with flights sorted by departure time" +"\n"+
          "7 -- Quit", "")

#   checks if the airline and flight number entered line up
#   returns confirmed input
def both_check(airlines, flightNums):
    # run booleans
    goodAirline = False
    goodFlight = False

    # airline is unconfirmed
    while goodAirline == False:
        airline = input("Enter airline name: ")
        try:
            x = airlines.index(airline)
            # confirm and store airline
            goodAirline = True

            # flight is unconfirmed
            while goodFlight == False:
                flight = input("Enter flight number: ")
                try:
                    good_indexes = []
                    for i in range(len(airlines)):
                        if airlines[i] == airline:
                            good_indexes.append(i)
                    y = flightNums.index(flight)
                    if flightNums.index(flight) in good_indexes:
                        # confirm and store flight
                        goodFlight = True
                        return airline, flight
                    else:
                        # attemps to access outside of index, causing an error on purpose
                        y = flightNums[(len(flightNums) + 1)]

                except ValueError:
                    display("Invalid input -- try again")

                # catches the unique index value
                except IndexError:
                    display("Invalid input -- try again")

        except ValueError:
            display("Invalid input -- try again")

# takes in all lists and returns the index of the information at the given flight
def find_specific_flight(airlines, flightNums, depps, arrs, prices):
    # blank
    display('')
    goodAirline, goodFlight = both_check(airlines, flightNums)

    # goes through flightnums until at the confirmed flight
    for i in range(len(flightNums)):
        if flightNums[i] == goodFlight and airlines[i] == goodAirline:
            return int(i)

#   uses a flights index and all the lists to calculate duration of the flight at given index
def calculate_duration(index_flight,depps, arrs):

    # adressing value
    arrival_line = arrs[index_flight]

    # splitting into hours and minutes
    ahours, aminutes = arrival_line.split(':')
    # calculates total minutes
    atotal = (int(ahours) * 60) + (int(aminutes))
    depp_line = depps[index_flight]
    dhours, dminutes = depp_line.split(':')
    dtotal = (int(dhours) * 60) + (int(dminutes))

    # calculates duration between two totals
    duration = int(atotal) - int(dtotal)

    return duration


#   takes in all lists and returns a list of those with shorter durations than the specified minute count
def shorter_than_specified(depps, arrs):
    # run boolean
    found = False
    display("")
    # processes until done
    while found == False:
        user_minutes = input("Enter maximum duration (in minutes): ")
        shorter_list = []
        try:
            # tries to assign minute input to int, catching value error, or converting to int
            user_int = int(user_minutes)

            for i in (range(len(depps))):
                # calculates duration of each flight
                duration = int(calculate_duration(i, depps, arrs))
                # checks if it is less than input
                if duration <= user_int:
                    #add those indexes with lower duration to the shorter list
                    shorter_list.append(i)
            found = True

        except ValueError:
            display("Entry must be a number")
    return shorter_list


# This function plots the values for wach list at a specified index
def display_vals_at(chosen_index, airlines, flightNums, depps, arrs, prices):
    chosen_index = int(chosen_index)
    print(airlines[chosen_index].ljust(8), flightNums[chosen_index].ljust(6),
    depps[chosen_index].rjust(7), arrs[chosen_index].rjust(7),
    "$", str(prices[chosen_index]).rjust(3))

#   takes in all lists and returns the index value of the cheapest flight corresponding to specified airline
def cheapest_by_airline(airlines,prices):
    # run boolean
    found = False
    display("")
    # processes until done
    while found == False:
        airline = input("Enter airline name: ")
        try:
            # tries to assign values index in list, checking if it exists
            index_check = airlines.index(airline)

            airline_indexes = []
            for i in (range(len(airlines))):
                # calculate each price
                if airline == airlines[i]:
                    airline_indexes.append(int(i))

            lowest_price = prices[airline_indexes[0]]

            for j in range(len(airline_indexes)):
                if int(prices[airline_indexes[j]]) <= int(lowest_price):
                    lowest_price = prices[airline_indexes[j]]
                    index = airline_indexes[j]
            found = True
            # returns the index at which the cheapest flight is in
            return index
        except ValueError:
            display("Invalid input -- try again")


#   takes in all lists and produces a list of indexes for those departing after specified time
def after_specified_time(depps):
    # able to run until found
    found = False
    # checks if has ever failed
    bust = False
    while found == False:
        # if has every failed, change the message
        if bust == True:
            time = input("Invalid time - Try again ")
        else:
            time = input("Enter earliest departure time: ")
        try:
            # tries to split, aswell as make inputs integers, checking both errors
            user_hours, user_minutes = time.split(':')
            x = user_hours[1]
            user_hours = int(user_hours)

            user_minutes = int(user_minutes)
            # empty list of the proper indexes
            after_indexes = []
            # creates value for users time
            user_total = (user_hours * 60) + user_minutes

            for i in range(len((depps))):
                # creates value for each time in depps and compares to value for users
                hours, minutes = depps[i].split(':')
                hours = int(hours)
                minutes = int(minutes)
                total = (hours * 60) + minutes

                if total > user_total:
                    # adds the index of flights with higher total to list
                    after_indexes.append(i)
            found = True
            # returns the list of indices
            return after_indexes
        # sets bust to true indicating the fail
        except ValueError:
            bust = True
        # indicates fail
        except IndexError:
            bust = True


# makes list of the total minutes and corresponding indexes based on departure values
def create_total_list(depps):
    total_list = []
    indexes = []
    # each value in depps
    for i in range(len(depps)):
        # calculates minutes
        dHours, dMinutes = depps[i].split(':')
        dTotal = int(int(dHours) * 60) + int(dMinutes)
        total_list.append(int(dTotal))
        # adds index to list
        indexes.append(int(i))

    # returns the totals and their indexes
    return total_list, indexes


# sorts the total list, and the index list on the same rules
def sortedIndex(depps):
    # uses total list function to make the two lists to sort
    total_list, index_list = create_total_list(depps)
    # iterate to access each value
    for i in range(len(total_list)):
        # iterate to compare value to other
        for j in range(0, (len(total_list) - i - 1)):
            # compares and sorts in ascending
            if total_list[j] > total_list[j + 1]:
                # swaps if they are not in correct order
                temp_total = total_list[j]
                temp_index = index_list[j]
                total_list[j] = total_list[j + 1]
                index_list[j] = index_list[j + 1]
                total_list[j + 1] = temp_total
                index_list[j + 1] = temp_index
    return index_list, total_list

#   function takes in the sorted indexes and makes new file in order
def add_to_file(index_list, airlines, flightNums, depps, arrs, prices):
    # writes to file
    file = open("time-sorted-flights.csv", "w")
    for j in range(len(index_list)):

        # gets the write information to write
        index = int(index_list[j])
        file.write(str(airlines[index]) + ',' + str(flightNums[index]) + ',' + str(depps[index]) + ',' + str(arrs[index]) + ',' + ' $' + str(prices[index]) + "\n")

    file.close()
    return


#   calculates average of all prices
def calc_avg_price(prices):
    total = 0
    count = len(prices)

    for i in range(len(prices)):
        total = total + float(prices[i])
    #   rounds the average to have two decimal places
    avg = float(total / count)
    avg = round(avg, 2)

    return avg

def main():
    # run boolean
    run = True
    airlines, flightNums, depps, arrs, prices = get_data()

    while run == True:
        # displays choices and confirms entry
        display_choice()
        valid_choice = choice_check()

        # if statement checks the users input
        # 1 displays headers then needed flights
        if valid_choice == '1':
            chosen_index = find_specific_flight(airlines,flightNums, depps, arrs,prices)

            display("\nThe flight that meets your criteria is:")
            display('')
            display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
            print(airlines[chosen_index].ljust(8), flightNums[chosen_index].ljust(6),
                  depps[chosen_index].rjust(7), arrs[chosen_index].rjust(7),
                  "$", str(prices[chosen_index]).rjust(3))
        # 2 displays headers and needed flights, or NONE
        elif valid_choice == '2':

            shorter_list = shorter_than_specified(depps, arrs)
            if len(shorter_list) == 0:
                display("\nNo flights meet your criteria")
            elif len(shorter_list) == 1:
                display("\nThe flight that meets your criteria is:")
                display('')
                display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
                # loops through list of those meeting criteria
                for i in range(len(shorter_list)):
                    display_vals_at(shorter_list[i], airlines, flightNums, depps, arrs, prices)

            else:
                display("\nThe flights that meet your criteria are:")
                display('')
                display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
                # loops through the list of flights meeting criteria
                for i in range(len(shorter_list)):
                    display_vals_at(shorter_list[i], airlines, flightNums, depps, arrs, prices)
        # 3 displays headers and needed flights or NONE
        elif valid_choice == '3':

            index = (cheapest_by_airline(airlines,prices))
            display("\n" + "The flight that meets your criteria is:")
            display("")
            display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
            display_vals_at(index,airlines,flightNums,depps,arrs,prices )
        # 4 displays headers and needed flights
        elif valid_choice == '4':
            display("")
            after_indexes = after_specified_time(depps)
            # checks if list is empty, changing output
            if len(after_indexes) == 0:
                display("\nNo flights meet your criteria")
            else:
                display("\n" + "The flights that meet your criteria are:")
                display("")
                display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
                for i in range(len(after_indexes)):
                    display_vals_at(after_indexes[i], airlines, flightNums, depps, arrs, prices)
        # 5 displays the average price
        elif valid_choice == '5':
            # creates unique statement
            statement = "\n" + "The average price is $ " + str(calc_avg_price(prices))
            display(statement)
        # 6 uses functions to write to file
        elif valid_choice == '6':
            display("\n" + "Sorted data has been written to file: time-sorted-flights.csv")
            # sorts the two lists for written order
            sorted_index, sorted_total = (sortedIndex(depps))
            add_to_file(sorted_index, airlines,flightNums,depps,arrs,prices)
        # 7 terminates by changing run boolean
        elif valid_choice == '7':
            display("Thank you for flying with us")
            run = False
