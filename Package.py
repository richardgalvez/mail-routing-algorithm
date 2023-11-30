class Package:
    """ Represents the item(s) being delivered by the Truck. """

    def __init__(self, package_id, address, deadline, city, zip_code, weight, status):
        self.package_id = package_id
        self.address = address
        self.deadline = deadline
        self.city = city
        self.zip_code = zip_code
        self.weight = weight
        self.status = status

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.package_id, self.address, self.deadline, self.city,
                                         self.zip_code, self.weight, self.status)

    def get_status(self):
