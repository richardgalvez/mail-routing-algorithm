class Package:
    """ Represents the item(s) being delivered by the Truck. """

    def __init__(self, package_id, address, city, state, zip_code, deadline_time, weight, status, truck_id=None):
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
        self.truck_id = truck_id

    def __str__(self):
        return ("Package ID: %s | Truck #: %s\nAddress: %s, %s, %s %s | Weight: %s | Deadline time: %s\nStatus: %s | Delivery time: %s" %
                (self.package_id, self.truck_id, self.address, self.city, self.state,
                 self.zip_code,self.weight, self.deadline_time, self.status, self.delivery_time))

    # Method to get status of the package based on time factors.
    def get_status(self, time_difference):
        if self.delivery_time < time_difference:
            self.status = "DELIVERED"
        elif self.departure_time > time_difference:
            self.status = "AT HUB"
        else:
            self.status = "EN ROUTE"
