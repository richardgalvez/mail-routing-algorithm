'''
 Each truck can carry a maximum of 16 packages, and the ID number of each package is unique.
 The trucks travel at an average speed of 18 miles per hour and have an infinite amount of gas with no need to stop.
 There are no collisions.
 Three trucks and two drivers are available for deliveries. Each driver stays with the same truck as long as that
 truck is in service.
 Drivers leave the hub no earlier than 8:00 a.m., with the truck loaded, and can return to the hub for packages if
 needed.
 The delivery and loading times are instantaneous (i.e., no time passes while at a delivery or when moving packages
 to a truck at the hub). This time is factored into the calculation of the average speed of the trucks.
 There is up to one special note associated with a package
 The delivery address for package #9, Third District Juvenile Court, is wrong and will be corrected at 10:20 a.m.
 WGUPS is aware that the address is incorrect and will be updated at 10:20 a.m.
 However, WGUPS does not know the correct address (410 S. State St., Salt Lake City, UT 84111) until 10:20 a.m.
 The distances provided in the “WGUPS Distance Table” are equal regardless of the direction traveled.
 The day ends when all 40 packages have been delivered.

 B.  Develop a look-up function that takes the package ID as input and returns
 each of the following corresponding data components:
'''
# Student Name: Richard Galvez
# Student ID: 010611634

import Truck
import csv

def package_lookup(package_id):

'''
C.  Write an original program that will deliver all packages and meet all requirements using the attached supporting
documents “Salt Lake City Downtown Map,” “WGUPS Distance Table,” and “WGUPS Package File.”

2. Include comments in your code to explain both the process and the flow of the program.

D. Provide an intuitive interface for the user to view the delivery status (including the delivery time) of any
package at any time and the total mileage traveled by all trucks.
(The delivery status should report the package as at the hub, en route, or delivered.
Delivery status must include the time.)
'''
