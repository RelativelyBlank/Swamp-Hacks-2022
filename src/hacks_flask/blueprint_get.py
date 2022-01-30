# import flask and blueprints
from flask import Blueprint, render_template, request, redirect, url_for, send_file, jsonify, abort
import core_gmaps
import core_sentimenta
import core_firestore
from flask_cors import cross_origin
# make a flask blueprint
get_flask_blueprint = Blueprint('get_blueprint', __name__, template_folder='templates')

# make a get request at /location/{}
@get_flask_blueprint.route('/location/<location>/image', methods=['GET'])
@cross_origin()
def getImageLocation(location):
    image_name = '{}.jpg'.format(location)
    # get the image from the core_gmaps module
    image = core_gmaps.getLocationImage(location)
    print(jsonify(image))
    print(image)
    # send the image to the client
    return jsonify(image)

# make a get request at /location/{}/reviews
@get_flask_blueprint.route('/location/<location>/reviews', methods=['GET'])
@cross_origin()
def getReviewsLocation(location):
    # get the reviews from the core_gmaps module
    reviews = core_gmaps.getLocationReviews(location)
    # send the reviews to the client
    return jsonify(reviews)

# make a get request at /location/{}/best_review
@get_flask_blueprint.route('/location/<location>/best_review', methods=['GET'])
@cross_origin()
def getBestReviewLocation(location):
    # get the best review from the core_gmaps modul
    reviews = core_gmaps.getLocationReviews(location)
    best_review = core_sentimenta.find_best_review(reviews)
    # send the best review to the client as json
    return jsonify(best_review)

@get_flask_blueprint.route('/get/<email>/get_file/<image_name>', methods=['GET', 'POST'])
@cross_origin()
def recover_image_from_firebase(email, image_name):
    if request.method == 'GET':
        image_file = core_firestore.get_image_from_firebase("postcard_{}_data".format(image_name), email)
    #   return the image
        return send_file(image_file, mimetype='image/gif')
    return abort(500)

# define a route to get all the image names from firebase with given email
@get_flask_blueprint.route('/get/<email>/get_images', methods=['GET', 'POST'])
@cross_origin()
def recover_images_from_firebase(email):
    if request.method == 'GET':
        images = core_firestore.get_image_names_from_firebase(email)
    #   return the images
        return jsonify(images)
    return abort(500)