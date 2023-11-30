class Truck:
    """ Represents the vehicle(s) traveling the routes to deliver packages. """

    def __init__(self, packages, load, address, speed, mileage, departure_time):
        self.packages = packages
        self.load = load
        self.address = address
        self.speed = speed
        self.mileage = mileage
        self.departure_time = departure_time

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.packages, self.load, self.address, self.speed,
                                      self.mileage, self.departure_time)
