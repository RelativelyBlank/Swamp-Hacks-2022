from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import os,sys
import pathlib
import requests

# make a blueprint
auth_bp = Blueprint('auth_bp', __name__, template_folder='templates')
GOOGLE_CLIENT_ID = '184728120634-720pj9v5aoisi02v87085vqe8to2fjgc.apps.googleusercontent.com'
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, 'client_secrets.json')
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=['https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'openid'],
    redirect_uri="http://127.0.0.1:5000/callback"
)
# re
def login_is_required(func):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            abort(401)
        else:
            return func()
    return wrapper
# make a login, callback, and logout route

@auth_bp.route('/login')
def login():
    authorizaton_url, state = flow.authorization_url()
    session['state'] = state
    return redirect(authorizaton_url)

@auth_bp.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session['state'] == request.args['state']:
        abort(500)

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )

    return id_info



@auth_bp.route('/logout')
def logout():
    pass

@auth_bp.route('/protected_area')
@login_is_required
def protected_area():
    return "Protected!"

@auth_bp.route('/')
def index():
    # return a login button
    return "<a href='/login'><button>Login</button></a>"