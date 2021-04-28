import pdb
from models.module import Module
from models.manufacturer import Manufacturer
from descriptions import *

import repositories.module_repository as module_repository
import repositories.manufacturer_repository as manufacturer_repository


module_repository.delete_all()
manufacturer_repository.delete_all()

# MANUFACTURERS
hex_address = "HEXINVERTER ÉLECTRONIQUE, Somewhere in Canada, Maybe Montreal?"


doepfer = Manufacturer("Doepfer", "somewhere in Germany", "555-555-555", "http://www.doepfer.de/")
hexinverter = Manufacturer("Hexinverter", hex_address, "1-555-2345")
manufacturer_repository.save(doepfer)


manufacturer_repository.save(hexinverter)


# MODULES

mutant_bassdrum_url = "https://www.modulargrid.net/img/imagecache/212x413_3535.jpg"









module_1 = Module(name="Mutant Bassdrum", description=mutant_bassdrum_description, stock="5",
                  buying_cost=150, selling_price=212, function="Drum", width=13, depth=35,
                  image_url=mutant_bassdrum_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_2 = Module(name="Mutant Clap", description="a short description", stock="3",
                  buying_cost=100, selling_price=180, function="Drum", width=13, depth=35,
                  image_url=None, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_repository.save(module_1)
module_repository.save(module_2)


pdb.set_trace()