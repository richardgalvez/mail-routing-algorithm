# Student Name: Richard Galvez
# Student ID: 010611634

# Import modules and classes required for main program.
import datetime
import csv
from HashMap import HashMap
from Truck import Truck
from Package import Package

# Reference/Source citation: https://docs.python.org/3/library/csv.html
# Read Address information from provided file.
with open("csv/WGUPS-Address-Table.csv") as csvfile1:
    address_reader = csv.reader(csvfile1)
    address_reader = list(address_reader)

# Read Distance information from provided file.
with open("csv/WGUPS-Distance-Table.csv") as csvfile2:
    distance_reader = csv.reader(csvfile2)
    distance_reader = list(distance_reader)

# Read Package information from provided file.
with open("csv/WGUPS-Package-File.csv") as csvfile3:
    package_reader = csv.reader(csvfile3)
    package_reader = list(package_reader)


# Function to return difference between addresses.
def get_distance(x, y):
    distance = distance_reader[x][y]
    if distance == '':
        distance = distance_reader[y][x]
    return float(distance)


# Function to return address number from string.
def get_address(address):
    for row in address_reader:
        if address in row[2]:
            return int(row[0])


# Function to get sum for total mileage of trucks.
def get_mileage(t1, t2, t3):
    return t1.mileage + t2.mileage + t3.mileage


# Function to create package objects from Package-File csv file, then load them into hash map.
# Reference/Source citations: WGU C950 - Webinar-3 - How to Dijkstra – W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
def load_packages(file, hashmap):
    with open(file) as package_information:
        package_data = csv.reader(package_information)
        for package in package_data:
            pkg_id = int(package[0])
            pkg_address = package[1]
            pkg_city = package[2]
            pkg_state = package[3]
            pkg_zip = package[4]
            pkg_deadline = package[5]
            pkg_weight = package[6]
            pkg_status = "| AT HUB |"

            # Instantiate package object.
            pkg = Package(pkg_id, pkg_address, pkg_city, pkg_state, pkg_zip, pkg_deadline, pkg_weight, pkg_status)

            # Add data to hash map.
            hashmap.insert(pkg_id, pkg)


# Instantiate main hash map object.
package_hmap = HashMap()

# Load packages into hash map.
load_packages("csv/WGUPS-Package-File.csv", package_hmap)

# Instantiate 3 truck objects.
truck1 = Truck(1, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 16, 18, None,
               "4001 South 700 East", 0.0, datetime.timedelta(hours=8))

truck2 = Truck(2, [3, 9, 12, 17, 18, 21, 23, 24, 27, 35, 36, 38, 39], 16, 18, None,
               "4001 South 700 East", 0.0, datetime.timedelta(hours=10, minutes=20))

truck3 = Truck(3, [2, 4, 5, 6, 7, 8, 10, 11, 22, 25, 26, 28, 32, 33], 16, 18, None,
               "4001 South 700 East", 0.0, datetime.timedelta(hours=9, minutes=5))


# Function based on nearest neighbor algorithm to sort packages and set which truck they are on while calculating distance of a (t)ruck.
def deliver_packages(t, truck_id):
    undelivered = []
    for packageID in t.packages:
        package = package_hmap.lookup(packageID)
        undelivered.append(package)
    # Clear package list of (t)ruck to make way for new packages in the order set by nearest neighbor algorithm.
    t.packages.clear()

    # Go through the list of 'undelivered' list until none remaining, adding the closest package into t.packages list.
    while len(undelivered) > 0:
        next_addr = 2000
        next_pkg = None
        for package in undelivered:
            package.truck_id = truck_id
            if get_distance(get_address(t.address), get_address(package.address)) <= next_addr:
                next_addr = get_distance(get_address(t.address), get_address(package.address))
                next_pkg = package
        # Add next closest package to (t)ruck's package list.
        t.packages.append(next_pkg.package_id)
        # Remove the same package from 'undelivered' list.
        undelivered.remove(next_pkg)
        # Adds the mileage driven to the (t)ruck.mileage attribute.
        t.mileage += next_addr
        # Update (t)ruck's current address to the package driven to.
        t.address = next_pkg.address
        # Update the time it took for truck to drive to the closest package.
        t.time += datetime.timedelta(hours=next_addr / 18)
        next_pkg.delivery_time = t.time
        next_pkg.departure_time = t.departure_time


# Trucks being loaded and determining the truck # the packages are on.
deliver_packages(truck1, truck1.truck_id)
deliver_packages(truck2, truck2.truck_id)

# Ensure that the 3rd truck does not leave until either the 1st or 2nd truck are done with their deliveries.
truck3.departure_time = min(truck1.time, truck2.time)
deliver_packages(truck3, truck3.truck_id)

# Get package #9 from the hash map for later use.
pkg9 = package_hmap.lookup(9)
# Store original address and zip code to keep for later use.
pkg9_original_address = pkg9.address
pkg9_original_zip = pkg9.zip_code


class Main:
    """ This is the main program for the user interface. """
    print("Welcome to the Western Governors University Parcel Service (WGUPS)!\n")
    print("Packages for each truck:")
    print("Truck #1: 1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40")
    print("Truck #2: 3, 9, 12, 17, 18, 21, 23, 24, 27, 35, 36, 38, 39")
    print("Truck #3: 2, 4, 5, 6, 7, 8, 10, 11, 22, 25, 26, 28, 32, 33")
    print("The total mileage for all trucks on the current route is: " + str(get_mileage(truck1, truck2, truck3)) + "\n")

    # User is prompted to begin by entering in "time".
    text = input("What would you like to do? Enter 'start' to begin or 'q' to quit the program.\n")
    program_end = False
    while not program_end:
        if text == "start":
            # User is prompted to enter a specific time with validation.
            convert_time = ""
            user_time = input("Please enter a time in the format HH:MM:SS to check status of related package(s). Enter 'q' to quit.\n")
            if user_time.lower() == 'q':
                print("Program exiting. Have a nice day!")
                exit()
            valid_time = False
            while not valid_time:
                try:
                    (hr, min, sec) = user_time.split(":")
                    convert_time = datetime.timedelta(hours=int(hr), minutes=int(min), seconds=int(sec))
                    valid_time = True
                except ValueError:
                    user_time = input("Invalid time format. Please enter a valid time in the format HH:MM:SS or 'q' to quit.\n")

            # Check if the entered time is before 10:20:00, as the new address will update after 10:20 am.
            if convert_time < datetime.timedelta(hours=10, minutes=20):
                # Update the address for package #9 if before 10:20 am.
                pkg9.address = "300 State St"
                pkg9.zip_code = "84103"
            elif convert_time >= datetime.timedelta(hours=10, minutes=20):
                # Reset to the address from CSV (correct address) if the time is after 10:20 am.
                pkg9.address = pkg9_original_address
                pkg9.zip_code = pkg9_original_zip

            # User is prompted if they would like to see the status of all packages or only one.
            next_input = input("To view individual package status, enter 'single'. To view all packages, enter 'all'. To quit, enter 'q'.\n")
            # Stay open until user inputs "single", "all", or "q" to quit.
            status_end = False
            while not status_end:
                if next_input.lower() == "single":
                    # User is prompted to input a package ID.
                    single_input = input("Enter the package ID: ")
                    package = package_hmap.lookup((int(single_input)))
                    package.get_status(convert_time)
                    print(str(package))
                    print("")
                    status_end = True
                elif next_input.lower() == "all":
                    for packageID in range(1, 41):
                        package = package_hmap.lookup(packageID)
                        package.get_status(convert_time)
                        print(str(package))
                        print("")
                    status_end = True
                elif next_input.lower() == "q":
                    print("Program exiting. Have a nice day!")
                    exit()
                else:
                    next_input = input("Command not recognized. Please enter 'single' to view one package, 'all' to view all packages, or 'q' to exit the program.\n")
        elif text.lower() == "q":
            print("Program exiting. Have a nice day!")
            program_end = True
        else:
            text = input("Command not recognized. Enter 'start' to begin or 'q' to quit the program.\n")
