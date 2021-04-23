class Module:
    def __init__(self, name, description, stock, buying_cost, 
    selling_price, function, width, depth, manufacturer,  
    plus_12v=None, minus_12v=None, image_url=None, id=None):
        
        self.id = id
        self.name = name
        self.stock = stock
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.function = function
        self.width = width
        self.depth = depth
        self.image_url = image_url

        # volts = None means no info available, volts = 0 means draws no current.
        self.minus_12v = minus_12v
        self.plus_12v = plus_12v
        self.manufacturer = manufacturer