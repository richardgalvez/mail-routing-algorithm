class Package:
    """ Represents the item(s) being delivered by the Truck. """

    def __init__(self, package_id, address, city, zip_code, weight, status,
                 deadline_time, delivery_time, departure_time):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status
        self.deadline_time = deadline_time
        self.delivery_time = delivery_time
        self.departure_time = departure_time

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.package_id, self.address, self.deadline, self.city,
                                         self.zip_code, self.weight, self.status)

    def get_status(self, time_difference):
        if self.delivery_time < time_difference:
            self.status = "Package Delivered!"
        elif self.departure_time > time_difference:
            self.status = "Package is on the way!"
        else:
            self.status = "Package is currently at Hub."
