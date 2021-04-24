import pdb
from models.module import Module
from models.manufacturer import Manufacturer

import repositories.module_repository as module_repository
import repositories.manufacturer_repository as manufacturer_repository

# book_repository.delete_all()
# author_repository.delete_all()
mutant_url = "https://www.modulargrid.net/img/imagecache/212x413_3535.jpg"
mutant_description = """====Primary Features====
It's really two modules in one: a totally unique analogue bassdrum and a voltage controlled distortion module! (with the same topology as batteryACID!)

- analogue bassdrum circuitry capable of vanilla TR-808 sounds \n
- built in voltage controlled distortion (batteryACID distortion) \n
- distortion accepts external inputs when not being used with kick drum (great for acid synth leads) \n
- voltage control of distortion amount \n
- voltage control of decay from short kicks to long "ooooooooomphs" \n
- voltage control of pitch (approximates v/oct response, but not musically tuned) \n
- non-invasive analogue optocouplers used for voltage control, thus, completely vintage sounds can still be had if that's what you're after! \n
- completely redesigned, hi-fi signal chain spares no expense by replacing cheap transistor amplifiers with low noise opamp equivalents \n
- you can dial in super hot, modular level output levels (up to 20Vp-p!)"""
hex_address = "HEXINVERTER ÉLECTRONIQUE, Somewhere in Canada, Maybe Montreal?"

hexinverter = Manufacturer("Hexinverter", hex_address, "1-555-2345")
manufacturer_repository.save(hexinverter)

module_1 = Module(name="Mutant Bassdrum", description=mutant_description, stock="5",
                  buying_cost=150, selling_price=212, function="drums", width=13, depth=35,
                  image_url=mutant_url, minus_12v=55, plus_12v=45, manufacturer=hexinverter)

module_repository.save(module_1)
# author2 = Author("David", "Ascher")
# author_repository.save(author2)


# book_1 = Book("Colour of Magic", "Fantasy", "Colin Smythe", author1)
# book_repository.save(book_1)

# book_2 = Book("The Light Fantastic", "Fantasy", "Colin Smythe", author1)
# book_repository.save(book_2)

# book_3 = Book("Learning Python", "Education", "O' Reilly", author2)
# book_repository.save(book_3)

pdb.set_trace()