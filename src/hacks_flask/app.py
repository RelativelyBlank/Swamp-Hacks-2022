from flask import Flask, session, abort, redirect
import sys, os
import datetime
# ==== INSTRUCTIONS ====
# TO GET THE IMAGE OF THE LOCATION
#   -> SEND A REQUEST TO http://127.0.0.1:5000/location/<location>/image
#   -> THE IMAGE IS DOWNLOADED TO imgs/<location>.jpg
# TO GET THE BEST REVIEW OF THE LOCATION
#   -> SEND A REQUEST TO http://127.0.0.1:5000/location/<location>/best_review
#   -> RETURNS A JSON WITH THE BEST REVIEW
# TO UPLOAD A FILE:
#   -> SEND A REQUEST TO http://127.0.0.1:5000/post/upload_file
#   -> THE JSON MUST BE LIKE '{ "image_location": "imgs/test1.jpg", "email" : "salvadoraleguas@gmail.com" }'
#   -> THE FILE MUST BE SENT AS A POST REQUEST
# TO GET AN IMAGE FROM FIREBASE
#  -> SEND A REQUEST TO http://127.0.0.1:5000/get/<email>/get_file/<image_name>
#  -> THE IMAGE IS DOWNLOADED TO imgs/<image_name>
# TO GET ALL THE IMAGES FOR A USER ON FIREBASE
#  -> SEND A REQUEST TO http://127.0.0.1:5000/get/<email>/get_images
#  -> RETURNS A JSON OF THE IMAGE NAMES


os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
import core_gmaps
import core_sentimenta
import core_twilio
import blueprint_auth
import core_firestore

import blueprint_get
import blueprint_auth
import blueprint_post

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.permanent_session_lifetime = datetime.timedelta(days=365)


# register get blueprint
app.register_blueprint(blueprint_get.get_flask_blueprint)
app.register_blueprint(blueprint_auth.auth_bp)
app.register_blueprint(blueprint_post.post_flask_blueprint)

if __name__ == "__main__":
    app.run(debug=True)