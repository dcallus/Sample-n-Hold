from db.run_sql import run_sql

from models.module import Module
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository


def save(module):
    sql = "INSERT INTO modules (name, description, stock, buying_cost, selling_price, function, width, depth, image_url, minus_12v, plus_12v, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [module.name, module.description, module.stock, module.buying_cost, module.selling_price, 
    module.function, module.width, module.depth, module.image_url, module.minus_12v, module.plus_12v, module.manufacturer.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    module.id = id
    return module


# def select_all():
#     books = []

#     sql = "SELECT * FROM books"
#     results = run_sql(sql)

#     for row in results:
#         author = author_repository.select(row['author_id'])
#         book = Book(row['title'], row['genre'], row['publisher'], author, row['id'] )
#         books.append(book)
#     return books



# def select(id):
#     book = None
#     sql = "SELECT * FROM books WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         author = author_repository.select(result['author_id'])
#         book = Book(result['title'], result['genre'], result['publisher'], author, result['id'] )
#     return book


# def delete_all():
#     sql = "DELETE  FROM books"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE  FROM books WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(book):
#     sql = "UPDATE books SET (title, genre, publisher, author_id) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [book.title, book.genre, book.publisher, book.author.id, book.id]
#     print(values)
#     run_sql(sql, values)
