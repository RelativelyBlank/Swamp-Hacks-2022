# import flask and blueprints
import os.path

from flask import Blueprint, render_template, request, redirect, url_for, send_file, jsonify, abort
import core_gmaps
import core_sentimenta
import core_firestore
from flask_cors import cross_origin


# make a flask blueprint
post_flask_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')
# define a route to /post/upload_file
@post_flask_blueprint.route('/post/upload_file', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
    #     get the json data from the request
        json_data = request.get_json()
        print(json_data)
        # get the image location from the json data
        image_location = os.path.abspath('imgs/' + json_data['image_location'])
        # get the image caption from t
        core_firestore.upload_image_to_firebase(image_location, json_data['email'])
        return jsonify({"message": "Image uploaded successfully"})



'''
curl --header "Content-Type: application/json" --request POST --data '{ "image_location": "imgs/test1.jpg", "email" : "salvadoraleguas@gmail.com" }' http://127.0.0.1:5000/post/upload_file
'''