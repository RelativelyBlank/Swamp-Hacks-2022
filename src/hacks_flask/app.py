from flask import Flask

import core_gmaps
import core_sentimenta
import core_twilio
import blueprint_get
app = Flask(__name__)

# register get blueprint
app.register_blueprint(blueprint_get.get_flask_blueprint)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
#
if __name__ == "__main__":
    app.run(debug=True)