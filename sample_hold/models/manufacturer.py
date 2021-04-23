class Manufacturer:
    def __init__(self, name, address, phone, website=None, id=None):
        self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website