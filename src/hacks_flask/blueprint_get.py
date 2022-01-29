# import flask and blueprints
from flask import Blueprint, render_template, request, redirect, url_for, send_file
import core_gmaps
# make a flask blueprint
get_flask_blueprint = Blueprint('get_blueprint', __name__, template_folder='templates')

# make a get request at /location/{}
@get_flask_blueprint.route('/location/<location>')
def getImageLocation(location):
    image_name = '{}.jpg'.format(location)
    # get the image from the core_gmaps module
    image = core_gmaps.getImage(location)
    # send the image to the client
    return send_file(image, mimetype='image/jpeg')