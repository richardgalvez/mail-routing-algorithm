class Truck:
    """ Represents the vehicle(s) traveling the routes to deliver packages. """

    def __init__(self, truck_id, packages, max_cap, speed_mph, load, address, mileage, departure_time):
        self.truck_id = truck_id
        self.packages = packages
        self.max_cap = max_cap
        self.speed_mph = speed_mph
        self.load = load
        self.address = address
        self.mileage = mileage
        self.departure_time = departure_time
        self.time = departure_time

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" % (self.truck_id, self.packages, self.max_cap, self.speed_mph, self.load,
                                            self.address, self.mileage, self.departure_time)
