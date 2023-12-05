class Package:
    """ Represents the item(s) being delivered by the Truck. """

    def __init__(self, package_id, address, city, state, zip_code, deadline_time, weight, status):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline_time = deadline_time
        self.weight = weight
        self.status = status
        self.delivery_time = None
        self.departure_time = None

    def __str__(self):
        return ("Package ID: %s\nAddress: %s, %s, %s %s | Weight: %s | Deadline time: %s\nStatus: %s | Delivery time: %s" %
                (self.package_id, self.address, self.city, self.state,
                 self.zip_code,self.weight, self.deadline_time, self.status, self.delivery_time))

    # Method to get status of the package based on time factors.
    def get_status(self, time_difference):
        if self.delivery_time < time_difference:
            self.status = "DELIVERED"
        elif self.departure_time > time_difference:
            self.status = "EN ROUTE"
        else:
            self.status = "AT HUB"
