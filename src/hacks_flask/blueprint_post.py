# import flask and blueprints
from flask import Blueprint, render_template, request, redirect, url_for, send_file, jsonify, abort
import core_gmaps
import core_sentimenta
import core_firestore
from flask_cors import cross_origin
import pdfcrowd
# make a flask blueprint
post_flask_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')
# define a route to /post/upload_file
@post_flask_blueprint.route('/post/upload_file', methods=['GET', 'POST'])
@cross_origin()
def upload_file():
    if request.method == 'POST':
    #     get the json data from the request
        html = '''<div style="display: inline-block; align-items: center; text-align: center; justify-content: center;">
        <div style="background-image: url("./imgs/{}"); background-size: cover; background-repeat: no-repeat; width: 900px; margin-top: 50px; border-radius: 10px;">
            <div style="padding: 10px 50px 100px;">
                <div style="display: flex;">
                    <p style="float: left; text-align: justify; width: 100%; margin-left: 50px; font-size: 20px; font-weight: bold;">user</p>
                    <p style="float: left; text-align: justify; width: 100%; margin-left: 50px; font-size: 20px; font-weight: bold;">user</p>
                    <p style="float: left; text-align: justify; width: 100%; margin-left: 50px; font-size: 20px; font-weight: bold;">effil tower</p>
                    <img src="./imgs/{}" style="max-height: 130px;">
                </div>
                <div>
                    <div style="display: flex;">
                    <img src="./imgs/{}.jpg" style="height: 350px; width: 600px; border-radius: 10px;">
                    <p style="float: right; text-align: justify; width: 100%; margin-left: 50px;">"{}" -{}</p>
                    </div>
                </div>
                <div style="justify-content: right; text-align: right;">Signed: [User Name]</div>
            </div>
        </div>
        </div>
        '''.format('postcard_back.jpg','seal.png',request.get_json()['jpgLocation'],request.get_json()['text'],request.get_json()['author_name'])
        # get the image location from the json data
        #image_location = json_data['image_location']
        core_firestore.upload_image_to_firebase(image_location, json_data['email'])
        #upload string to cloud firestore
        #core_firestore.upload_string_to_firestore(html, request.get_json()['email'])
        return jsonify("fdnawldnawdl")


'''
curl --header "Content-Type: application/json" --request POST --data '{ "image_location": "imgs/test1.jpg", "email" : "salvadoraleguas@gmail.com" }' http://127.0.0.1:5000/post/upload_file
'''