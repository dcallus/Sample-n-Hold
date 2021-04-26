from db.run_sql import run_sql

from models.module import Module
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository


def save(module):
    sql = """INSERT INTO modules (name, description, stock, buying_cost, 
    selling_price, function, width, depth, image_url, minus_12v, plus_12v, manufacturer_id) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"""
    
    values = [module.name, module.description, module.stock, module.buying_cost, module.selling_price, 
    module.function, module.width, module.depth, module.image_url, module.minus_12v, module.plus_12v, module.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    module.id = id
    return module

def select_all():
    modules = []

    sql = "SELECT * FROM modules"
    results = run_sql(sql)

    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        module = Module(row['name'], row['description'], row['stock'], row['buying_cost'], row['selling_price'],
        row['function'], row['width'], row['depth'], row['minus_12v'], row['plus_12v'], manufacturer, row['image_url'], row['id'])
        modules.append(module)
    return modules


def select(id):
    module = None
    sql = "SELECT * FROM modules WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        module = Module(result['name'], result['description'], result['stock'], result['buying_cost'], result['selling_price'], 
        result['function'], result['width'], result['depth'], result['minus_12v'], result['plus_12v'], manufacturer, result['image_url'], result['id'])
    return module


def delete_all():
    sql = "DELETE  FROM modules"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM modules WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(module):
    sql = """UPDATE modules SET (name, description, stock, buying_cost, 
    selling_price, function, width, depth, minus_12v, plus_12v, manufacturer_id, image_url)  = 
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"""
    values = [module.name, module.description, module.stock, module.buying_cost, module.selling_price, 
    module.function, module.width, module.depth, module.minus_12v, module.plus_12v, module.manufacturer.id, module.image_url, module.id]
    print(values)
    run_sql(sql, values)
