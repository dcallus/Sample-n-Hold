from flask import Blueprint, Flask, redirect, render_template, request

from models.module import Module
import repositories.module_repository as module_repository
import repositories.manufacturer_repository as manufacturer_repository

modules_blueprint = Blueprint("modules", __name__)

@modules_blueprint.route("/modules")
def modules():
    modules = module_repository.select_all() # NEW
    return render_template("modules/index.html", all_modules = modules)

# NEW
# GET '/modules/new'
@modules_blueprint.route("/modules/new", methods=['GET'])
def new_module():
    manufacturers = manufacturer_repository.select_all()
    return render_template("modules/new.html", all_manufacturers = manufacturers)

# CREATE
# POST '/modules'
@modules_blueprint.route("/modules",  methods=['POST'])
def create_module():
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
    module = Module(name, description, stock, buying_cost, selling_price,
                    function, width, depth, minus_12v, plus_12v, manufacturer, 
                    image_url)
    module_repository.save(module)
    return redirect('/modules')


# SHOW
# GET '/modules/<id>'
@modules_blueprint.route("/modules/<id>", methods=['GET'])
def show_module(id):
    module = module_repository.select(id)
    return render_template('modules/show.html', module = module)

# EDIT
# GET '/modules/<id>/edit'
@modules_blueprint.route("/modules/<id>/edit", methods=['GET'])
def edit_module(id):
    module = module_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template('modules/edit.html', module = module, all_manufacturers = manufacturers)

# UPDATE
# PUT '/modules/<id>'
@modules_blueprint.route("/modules/<id>", methods=['POST'])
def update_module(id):

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
    module = Module(name, description, stock, buying_cost, selling_price,
                    function, width, depth, minus_12v, plus_12v, manufacturer, 
                    image_url, id)
    module_repository.update(module)

    return redirect('/modules')

# # DELETE
# DELETE '/modules/<id>'
@modules_blueprint.route("/modules/<id>/delete", methods=['POST'])
def delete_module(id):
    module_repository.delete(id)
    return redirect('/modules')
