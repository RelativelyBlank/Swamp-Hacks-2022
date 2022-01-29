from google.cloud import firestore
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort, current_app
# read https://cloud.google.com/firestore/docs/quickstart-servers#firestore_setup_dataset_pt1-python

import os
# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("firestore_keys.json")
db = firestore.Client(project='alien-segment-337020')

# upload an html file to firestore

def upload_image_to_firebase(image_file_path):
    # check if session exists
    print(session)
    if 'email' not in session:
        abort(403)

    with open(image_file_path, "rb") as image_file:
        doc_ref = db.collection(u'users').document(u'{}'.format(session["email"]))
        doc_ref.set({
            u'postcard_data': image_file.read()
        })

#     return an html response that indicates the upload was successful
    return "upload successful"

# upload_html_to_firestore("bucket.jpg")