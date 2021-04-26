from flask import Blueprint, Flask, redirect, render_template, request

from models.manufacturer import Manufacturer
import repositories.module_repository as module_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all() # NEW
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)

# NEW
# GET '/manufacturers/new'
@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    return render_template("manufacturers/new.html", all_manufacturers = manufacturers)

# CREATE
# POST '/manufacturers'
@manufacturers_blueprint.route("/manufacturers",  methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    address = request.form['address']
    phone = request.form['phone']
    website = request.form['website']

    manufacturer = Manufacturer(name, address, phone, website)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

# SHOW
# GET '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template('/manufacturers/show.html', manufacturer = manufacturer)

# EDIT
# GET '/manufacturers/<id>/edit'
@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('manufacturers/edit.html', manufacturer = manufacturer)

# UPDATE
# PUT '/manufacturers/<id>'
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturer(id):

    name = request.form['name']
    description = request.form['description']
    stock = request.form['stock']
    buying_cost = request.form['buying-cost']
    selling_price = request.form['selling-price']
    function = request.form['function']
    width = request.form['width']
    depth = request.form['depth']
    minus_12v = request.form['minus-12v']
    plus_12v = request.form['plus-12v']
    manufacturer_id = request.form["manufacturer-id"]
    manufacturer  = manufacturer_repository.select(manufacturer_id)
    image_url = request.form['image-url']
    manufacturer = Manufacturer(name, description, stock, buying_cost, selling_price,
                    function, width, depth, minus_12v, plus_12v, manufacturer, 
                    image_url, id)
    manufacturer_repository.update(manufacturer)

    return redirect('/manufacturers')