from flask import Flask, session, abort, redirect
import sys, os
import datetime

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