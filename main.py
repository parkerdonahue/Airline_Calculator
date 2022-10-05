
def open_file():
    # This function will run the exception handling to check if the file input is valid.
    # it will return the valid file name.
    goodFile = False
    while goodFile == False:
        fname = input("Please enter a file name: ")
        try:
            flightFile = open(fname,'r')
            goodFile = True
        except IOError:
            print("Invalid file name try again ...")
    return flightFile

def display(value_to_display):
    print(value_to_display)
    return
    # This function will print the parameter value.
    # it will return nothing, only execute and display


def choice_check():
        found = False
        seven = ['1', '2', '3', '4', '5', '6', '7']
        while found == False:
            choice = input("Choice ==> ")
            try:
                # catches the error
                y = int(choice)
                try:
                    x = seven.index(choice)
                    goodChoice = choice
                    found = True
                    return goodChoice
                except ValueError:
                    print("Entry must be between 1 and 7")

            except ValueError:
                print("Entry must be a number")

def get_data():
    flightFile = open_file()
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
        price = price.replace('$','')
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

    print("\n" + "Please choose one of the following options:" + "\n"+
          "1 -- Find flight information by airline and flight number" +"\n"+
          "2 -- Find flights shorter than a specified duration" +"\n"+
          "3 -- Find the cheapest flight by a given airline" +"\n"+
          "4 -- Find flight departing after a specified time" +"\n"+
          "5 -- Find the average price of all flights" +"\n"+
          "6 -- Write a file with flights sorted by departure time" +"\n"+
          "7 -- Quit", "")

    # This will repeat the option displaying, after every interaction, until the user has quit
    # it will return nothing, only execute and display
def both_check(airlines, flightNums):
    goodAirline = False
    goodFlight = False

    while goodAirline == False:
        airline = input("Enter airline name: ")
        try:
            x = airlines.index(airline)
            goodAirline = True

            while goodFlight == False:
                flight = input("Enter flight number: ")
                try:
                    good_indexes = []
                    for i in range(len(airlines)):
                        if airlines[i] == airline:
                            good_indexes.append(i)
                    y = flightNums.index(flight)
                    if flightNums.index(flight) in good_indexes:
                        goodFlight = True
                        return airline, flight
                    else:
                        y = flightNums[(len(flightNums) + 1)]
                except ValueError:
                    display("Invalid input -- try again")
                except IndexError:
                    display("Invalid input -- try again")

        except ValueError:
            display("Invalid input -- try again")

        '''while goodFlight == False:
            flight = input("Enter flight number: ")
            try:
                good_indexes = []
                for i in range(len(airlines)):
                    if airlines[i] == airline:
                        good_indexes.append(i)
                y = flightNums.index(flight)
                if flightNums.index(flight) in good_indexes:
                    goodFlight = True
                    return airline, flight
                else:
                    y = flightNums[(len(flightNums) + 1)]
            except ValueError:
                display("Invalid entry - try again ... ")
            except IndexError:
                display("Invalid entry - try again ... ")

            for i in range(len(flightNums)):
                if flightNums[i] == flight and airlines[i] == airline:
                    goodFlight = True
                    return airline, flight

                else:
                    y = flightNums[(len(flightNums) + 1)]                 
        except ValueError:
            display("Invalid entry - try again ... ")'''


    '''while goodFlight == False:
        flight = input("Enter flight number: ")
        try:
            y = flightNums.index(flight)

            for i in range(len(flightNums)):
                if flightNums[i] == flight and airlines[i] == airline:
                    goodflight = True
                    return airline, flight
                else:
                    y = flightNums[len(flightNums+1)]
        except TypeError:
            display("Invalid entry - try again ... ")
        except ValueError:
            display("Invalid entry - try again ... ")
            return airline, flight
    
            if flightNums.index(flight) in airline_indexes:
                goodFlight = True
                return airline, flight

            if flightNums.index(flight) in airline_indexes and airlines.index(airline) == flightNums.index(flight):
                goodFlight = True
                


                return airline, flightNums[airline_indexes[i]]
            else:
                print(airline, flight, airlines.index(airline), flightNums.index(flight), airline_indexes, flightNums[airline_indexes[i]])
                error = int(airline)'''




# takes in all lists and returns the index of the information at the given flight
def find_specific_flight(airlines, flightNums, depps, arrs, prices):

    display('')
    goodAirline, goodFlight = both_check(airlines, flightNums)

    for i in range(len(flightNums)):
        if flightNums[i] == goodFlight and airlines[i] == goodAirline:
            return int(i)

    '''for i in range(len(airlines)):
        if airlines[i] == goodAirline:
            for j in range(len(flightNums)):
                if flightNums[j] == goodFlight and i == j:
                    print(j)
                    return j
                else:
                    pass
        else:
            return -1'''
    '''for i in range(len(airlines)):
        if airlines[i] == goodAirline:
            airline_indexes.append(i)'''


    '''found = False
    for i in range(len(airlines)):
        if found ='''

    '''i = 0
    found = False
    good_indexes = []
    while i < len(airlines) and found == False:
        if airlines[i] == goodAirline:
            good_indexes.append[i]
            airlineIndex = i
        found = True
        i = i + 1
    j = 0
    find = False
    while find == False:
        if flightNums[j] == goodFlight:
            goodFlightIndex = j
            find = True
        j = j + 1
    if goodFlightIndex == airlineIndex:
        return goodFlightIndex
    else: return -1'''

#   uses a flights index and all the lists to calculate duration of the flight at given index
def calculate_duration(index_flight,depps, arrs):

    arrival_line = arrs[index_flight]

    ahours, aminutes = arrival_line.split(':')
    atotal = (int(ahours) * 60) + (int(aminutes))
    depp_line = depps[index_flight]
    dhours, dminutes = depp_line.split(':')
    dtotal = (int(dhours) * 60) + (int(dminutes))
    duration = int(atotal) - int(dtotal)
    return duration



#   takes in all lists and returns a list of those with shorter durations than the specified minute count
def shorter_than_specified(airlines, flightNums, depps, arrs, prices):
    found = False
    display("")
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
def cheapest_by_airline(airlines, flightNums, depps, arrs, prices):
    found = False
    display("")
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
    #able to run until found
    found = False
    bust = False
    while found == False:
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
            #returns the list of indices
            return after_indexes
        except ValueError:
            bust = True
        except IndexError:
            bust = True



def create_total_list(depps):
    total_list = []
    indexes = []
    for i in range(len(depps)):
        dHours, dMinutes = depps[i].split(':')
        dTotal = int(int(dHours) * 60) + int(dMinutes)
        total_list.append(int(dTotal))
        indexes.append(int(i))
    return total_list, indexes




# sorts the total list, and the index list on the same rules
def sortedIndex(depps):
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

#function takes in the sorted indexes and makes new file in order
def add_to_file(index_list, airlines, flightNums, depps, arrs, prices):
    file = open("time-sorted-flights.csv", "w")
    for j in range(len(index_list)):

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

    run = True

    airlines, flightNums, depps, arrs, prices = get_data()

    while run == True:

        display_choice()
        valid_choice = choice_check()
        if valid_choice == '1':
            chosen_index = find_specific_flight(airlines,flightNums, depps, arrs,prices)

            display("\nThe flight that meets your criteria is:")
            display('')
            display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
            print(airlines[chosen_index].ljust(8), flightNums[chosen_index].ljust(6),
                  depps[chosen_index].rjust(7), arrs[chosen_index].rjust(7),
                  "$", str(prices[chosen_index]).rjust(3))

        elif valid_choice == '2':

            shorter_list = shorter_than_specified(airlines, flightNums, depps, arrs, prices)
            if len(shorter_list) == 0:
                display("\nNo flights meet your criteria")
            elif len(shorter_list) == 1:
                display("\nThe flight that meets your criteria is:")
                display('')
                display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
                for i in range(len(shorter_list)):
                    display_vals_at(shorter_list[i], airlines, flightNums, depps, arrs, prices)

            else:
                display("\nThe flights that meet your criteria are:")
                display('')
                display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
                for i in range(len(shorter_list)):
                    display_vals_at(shorter_list[i], airlines, flightNums, depps, arrs, prices)

        elif valid_choice == '3':

            index = (cheapest_by_airline(airlines,flightNums,depps,arrs,prices))
            display("\n" + "The flight that meets your criteria is:")
            display("")
            display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
            display_vals_at(index,airlines,flightNums,depps,arrs,prices )

        elif valid_choice == '4':
            display("")
            after_indexes = after_specified_time(depps)
            display("\n" + "The flights that meet your criteria are:")
            display("")
            display("AIRLINE  FLT#    DEPART  ARRIVE PRICE")
            for i in range(len(after_indexes)):
                display_vals_at(after_indexes[i],airlines,flightNums,depps,arrs,prices)
        elif valid_choice == '5':

            statement = "\n" + "The average price is $ " + str(calc_avg_price(prices))
            display(statement)

        elif valid_choice == '6':
            display("\n" + "Sorted data has been written to file: time-sorted-flights.csv")
            sorted_index, sorted_total = (sortedIndex(depps))
            add_to_file(sorted_index, airlines,flightNums,depps,arrs,prices)
        elif valid_choice == '7':
            display("Thank you for flying with us")
            run = False

main()