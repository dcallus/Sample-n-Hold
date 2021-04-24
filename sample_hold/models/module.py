class Module:
    def __init__(self, name, description, stock, buying_cost, 
    selling_price, function, width, depth, minus_12v, plus_12v,
    manufacturer, image_url=None, id=None):
        
        self.name = name
        self.description = description
        self.stock = stock
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.function = function
        self.width = width
        self.depth = depth
        self.minus_12v = minus_12v
        self.plus_12v = plus_12v
        self.manufacturer = manufacturer
        self.image_url = image_url

        self.id = id