from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.module import Module


def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, address, phone, website) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [manufacturer.name, manufacturer.address, manufacturer.phone, manufacturer.website]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer


def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['address'], row['phone'], row['website'], row['id'] )
        manufacturers.append(manufacturer)
    return manufacturers


def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['address'], result['phone'], result['website'], result['id'])
    return manufacturer


def delete_all():
    sql = "DELETE  FROM manufacturers"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, address, phone, website) = (%s, %s, %s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.address, manufacturer.phone,
              manufacturer.website, manufacturer.id]
    run_sql(sql, values)

def modules(manufacturer):
    modules = []

    sql = "SELECT * FROM modules WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        module = Module(row['name'], row['description'], row['stock'], row['buying_cost'], row['selling_price'],
        row['function'], row['width'], row['depth'], row['minus_12v'], row['plus_12v'], row['manufacturer_id'], row['image_url'], row['id'])
        module.append(module)
    return module