import pdb
from models.module import Module
from models.manufacturer import Manufacturer
from descriptions import *

import repositories.module_repository as module_repository
import repositories.manufacturer_repository as manufacturer_repository


module_repository.delete_all()
manufacturer_repository.delete_all()

# MANUFACTURERS

doepfer = Manufacturer("Doepfer", "somewhere in Germany", "555-555-555", "http://www.doepfer.de/")
hexinverter = Manufacturer("Hexinverter", "HEXINVERTER ÉLECTRONIQUE, Somewhere in Canada, Maybe Montreal?", "1-555-2345")
klangbau = Manufacturer("Klangbau Köln", "Berlin, Germany, E511 202", "555-555-505","https://xn--klangbaukln-zfb.de/")
make_noise = Manufacturer("Make Noise", "North-Carolina, USA", "555-555-511","https://makenoisemusic.com")
pittsburgh_modular = Manufacturer("Pittsburgh Modular", "Pittsburgh, USA", "1-555-2345")

manufacturer_repository.save(doepfer)
manufacturer_repository.save(hexinverter)
manufacturer_repository.save(klangbau)
manufacturer_repository.save(make_noise)
manufacturer_repository.save(pittsburgh_modular)


# MODULES

mutant_bassdrum_url = "https://www.modulargrid.net/img/imagecache/212x413_3535.jpg"
mutant_clap_url = "https://www.modulargrid.net/img/imagecache/212x413_4062.jpg"
mutant_machine_url = "https://www.modulargrid.net/img/imagecache/300x262_24839.jpg"
mutant_hotglue_url = "https://www.modulargrid.net/img/imagecache/300x317_5288.jpg"

twin_peak_res_url = "https://www.modulargrid.net/img/imagecache/235x413_12514.jpg"

makenoise_math_url = "https://www.modulargrid.net/img/imagecache/300x381_20545.jpg"

a_160_url = "https://www.modulargrid.net/img/imagecache/65x413_91.jpg"
a_160_2_url = "https://www.modulargrid.net/img/imagecache/66x413_4946.jpg"
a_160_5_url = "https://www.modulargrid.net/img/imagecache/64x413_5278.jpg"

pittsburgh_lpg_url = "https://www.modulargrid.net/img/imagecache/131x413_6225.jpg"


module_1 = Module(name="Mutant Bassdrum", description=mutant_bassdrum_description, stock="5",
                  buying_cost=150, selling_price=212, function="Drum", width=13, depth=35,
                  image_url=mutant_bassdrum_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_2 = Module(name="Mutant Clap", description=mutant_clap_description, stock="6",
                  buying_cost=100, selling_price=180, function="Drum", width=13, depth=35,
                  image_url=mutant_clap_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_3 = Module(name="Mutant Machine", description=mutant_machine_description, stock="22",
                  buying_cost=100, selling_price=180, function="Drum", width=13, depth=35,
                  image_url=mutant_machine_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_4 = Module(name="Mutant Hot Glue", description=mutant_hotglue_description, stock="6",
                  buying_cost=100, selling_price=180, function="Dynamics", width=21, depth=38,
                  image_url=mutant_hotglue_url, minus_12v=70, plus_12v=55, manufacturer=hexinverter)

module_5 = Module(name="Twin Peaks Resonator", description=twin_peak_description, stock="10",
                  buying_cost=100, selling_price=180, function="Filter", width=16, depth=38,
                  image_url=twin_peak_res_url, minus_12v=65, plus_12v=75, manufacturer=klangbau)

module_6 = Module(name="Maths", description=math_description, stock="20",
                  buying_cost=70, selling_price=120, function="Function Generator", width=20, depth=35,
                  image_url=makenoise_math_url, minus_12v=55, plus_12v=45, manufacturer=make_noise)

module_7 = Module(name="A-160", description=a_160_description, stock="5",
                  buying_cost=70, selling_price=120, function="Clock Modulator", width=8, depth=35,
                  image_url=a_160_url, minus_12v=60, plus_12v=45, manufacturer=doepfer)

module_8 = Module(name="A-160-2", description=a_160_2_description, stock="4",
                  buying_cost=70, selling_price=120, function="Clock Modulator", width=8, depth=35,
                  image_url=a_160_2_url, minus_12v=65, plus_12v=45, manufacturer=doepfer)

module_9 = Module(name="A-160-5", description=a_160_5_description, stock="8",
                  buying_cost=70, selling_price=120, function="Clock Modulator", width=8, depth=35,
                  image_url=a_160_5_url, minus_12v=20, plus_12v=25, manufacturer=doepfer)

module_10 = Module(name="LPG2", description=pittsburgh_lpg_description, stock="1",
                  buying_cost=70, selling_price=120, function="Low Pass Gate", width=8, depth=35,
                  image_url=pittsburgh_lpg_url, minus_12v=25, plus_12v=25, manufacturer=pittsburgh_modular)




module_repository.save(module_1)
module_repository.save(module_2)
module_repository.save(module_3)
module_repository.save(module_4)
module_repository.save(module_5)
module_repository.save(module_6)
module_repository.save(module_7)
module_repository.save(module_8)
module_repository.save(module_9)
module_repository.save(module_10)


pdb.set_trace()