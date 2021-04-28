from flask import Blueprint, Flask, redirect, render_template, request
from models.module import Module
import pdb
import repositories.module_repository as module_repository
import repositories.manufacturer_repository as manufacturer_repository

modules_blueprint = Blueprint("modules", __name__)

@modules_blueprint.route("/modules")
def modules():
    function_filter = request.args.get("filter-function")
    manufacturer_filter = request.args.get("filter-manufacturer")
    name_filter = request.args.get("filter-name")
    manufacturers = manufacturer_repository.select_all()
    modules = module_repository.select_all() # NEW
    filtered_functions = []
    filtered_manufacturers = []
    filtered_names = []
    filters_used = []

    if function_filter is not None:
        for module in modules:
            if module.function == function_filter:
                filtered_functions.append(module)
        filters_used.append(filtered_functions)


    if manufacturer_filter is not None:
        for module in modules:
            if str(module.manufacturer.id) == manufacturer_filter:
                filtered_manufacturers.append(module)
        filters_used.append(filtered_manufacturers)
    
    if name_filter is not None:
        for module in modules:
            if name_filter.lower() in module.name.lower():
                filtered_names.append(module)
        filters_used.append(filtered_names)
    

    # combines any amount of filters, just add a new filter above
    if filters_used != []:
        for filter in filters_used:
            filtered_results = set(filters_used[0]).intersection(set(filter))
        modules = list(filtered_results) 

    return render_template("modules/index.html", all_modules = modules, all_manufacturers = manufacturers)

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

# SHOW
# GET '/modules/<id>/description'
@modules_blueprint.route("/modules/<id>/description", methods=['GET'])
def show_single_module(id):
    module = module_repository.select(id)
    return render_template('modules/show_desc.html', module = module)

# SHOW
# GET '/modules/<id>/specification'
@modules_blueprint.route("/modules/<id>/specification", methods=['GET'])
def show_module_with_spec(id):
    module = module_repository.select(id)
    return render_template('modules/show_spec.html', module = module)

# SHOW
# GET '/modules/<id>/shop'
@modules_blueprint.route("/modules/<id>/shop", methods=['GET'])
def show_module_shop_info(id):
    module = module_repository.select(id)
    return render_template('modules/show_shop.html', module = module)

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
