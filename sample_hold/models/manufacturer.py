class Manufacturer:
    def __init__(self, name, address, phone, website=None, disabled=False, id=None):
        
        self.name = name
        self.address = address
        self.phone = phone
        self.website = website

        self.id = id

        self.disabled = disabled