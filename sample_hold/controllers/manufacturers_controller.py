from flask import Blueprint, Flask, redirect, render_template, request

from models.module import Module
import repositories.module_repository as module_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all() # NEW
    return render_template("manufacturers/index.html", all_manufacturers = manufacturers)