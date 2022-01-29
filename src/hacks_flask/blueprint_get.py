# import flask and blueprints
from flask import Blueprint, render_template, request, redirect, url_for, send_file, jsonify
import core_gmaps
import core_sentimenta
# make a flask blueprint
get_flask_blueprint = Blueprint('get_blueprint', __name__, template_folder='templates')

# make a get request at /location/{}
@get_flask_blueprint.route('/location/<location>/image', methods=['GET'])
def getImageLocation(location):
    image_name = '{}.jpg'.format(location)
    # get the image from the core_gmaps module
    image = core_gmaps.getLocationImage(location)
    # send the image to the client
    return send_file(image, mimetype='image/jpeg')

# make a get request at /location/{}/reviews
@get_flask_blueprint.route('/location/<location>/reviews', methods=['GET'])
def getReviewsLocation(location):
    # get the reviews from the core_gmaps module
    reviews = core_gmaps.getLocationReviews(location)
    # send the reviews to the client
    return jsonify(reviews)

# make a get request at /location/{}/best_review
@get_flask_blueprint.route('/location/<location>/best_review', methods=['GET'])
def getBestReviewLocation(location):
    # get the best review from the core_gmaps modul
    reviews = core_gmaps.getLocationReviews(location)
    best_review = core_sentimenta.find_best_review(reviews)
    # send the best review to the client as json
    return jsonify(best_review)

