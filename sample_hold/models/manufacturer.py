class Manufacturer:
    def __init__(self, name, address, phone, website=None, id=None, disabled=False):
        
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website

        self.id = id

        self.disabled = disabled