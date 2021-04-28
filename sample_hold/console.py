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

klangbau = Manufacturer("Klangbau Köln", "Berlin, Germany", "555-555-505","https://xn--klangbaukln-zfb.de/")
hexinverter = Manufacturer("Hexinverter", hex_address, "1-555-2345")

manufacturer_repository.save(doepfer)
manufacturer_repository.save(hexinverter)
manufacturer_repository.save(klangbau)
manufacturer_repository.save(hexinverter)


# MODULES

mutant_bassdrum_url = "https://www.modulargrid.net/img/imagecache/212x413_3535.jpg"
mutant_clap_url = "https://www.modulargrid.net/img/imagecache/212x413_4062.jpg"
mutant_machine_url = "https://www.modulargrid.net/img/imagecache/300x262_24839.jpg"
mutant_hotglue_url = "https://www.modulargrid.net/img/imagecache/300x317_5288.jpg"

twin_peak_res_url = "https://www.modulargrid.net/img/imagecache/235x413_12514.jpg"

makenoise_math_url = "https://www.modulargrid.net/img/imagecache/300x381_20545.jpg"

a_148_url = "https://www.modulargrid.net/img/imagecache/64x413_82.jpg"
a_160_url = "https://www.modulargrid.net/img/imagecache/65x413_91.jpg"
a_160_2_url = "https://www.modulargrid.net/img/imagecache/66x413_4946.jpg"
a_160_5_url = "https://www.modulargrid.net/img/imagecache/64x413_5278.jpg"

pittsburgh_url = "https://www.modulargrid.net/img/imagecache/131x413_6225.jpg"

mum_m8_url = "https://www.modulargrid.net/img/imagecache/133x413_13679.jpg"

spock_url = "https://www.modulargrid.net/img/imagecache/64x413_336.jpg"


module_1 = Module(name="Mutant Bassdrum", description=mutant_bassdrum_description, stock="5",
                  buying_cost=150, selling_price=212, function="Drum", width=13, depth=35,
                  image_url=mutant_bassdrum_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_2 = Module(name="Mutant Clap", description=mutant_clap_description, stock="6",
                  buying_cost=100, selling_price=180, function="Drum", width=13, depth=35,
                  image_url=mutant_clap_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_3 = Module(name="Mutant Machine", description=mutant_machine_description, stock="1",
                  buying_cost=100, selling_price=180, function="Drum", width=13, depth=35,
                  image_url=mutant_machine_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_4 = Module(name="Mutant Hot Glue", description=mutant_hotglue_description, stock="1",
                  buying_cost=100, selling_price=180, function="Drum", width=13, depth=35,
                  image_url=mutant_hotglue_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_5 = Module(name="Twin Peaks Resonator", description=twin_peak_description, stock="1",
                  buying_cost=100, selling_price=180, function="Drum", width=13, depth=35,
                  image_url=twin_peak_res_url, minus_12v=55, plus_12v=45, manufacturer=klangbau)



module_repository.save(module_1)
module_repository.save(module_2)
module_repository.save(module_3)
module_repository.save(module_4)
module_repository.save(module_5)


pdb.set_trace()