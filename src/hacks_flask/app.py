from flask import Flask, session, abort, redirect
import sys, os
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
import core_gmaps
import core_sentimenta
import core_twilio
import blueprint_auth
import core_firestore

import blueprint_get
import blueprint_auth

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


# register get blueprint
app.register_blueprint(blueprint_get.get_flask_blueprint)
app.register_blueprint(blueprint_auth.auth_bp)


if __name__ == "__main__":
    app.run(debug=True)