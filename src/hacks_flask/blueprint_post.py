# import flask and blueprints
from flask import Blueprint, render_template, request, redirect, url_for, send_file, jsonify
import core_gmaps
import core_sentimenta
import core_firestore
# make a flask blueprint
post_flask_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')

# define a route to /post/upload_file
@post_flask_blueprint.route('/post/upload_file', methods=['GET', 'POST'])
def upload_file():
    core_firestore.upload_image_to_firebase('Tiananmen.jpg')
