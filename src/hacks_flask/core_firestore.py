from google.cloud import firestore
import os
# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
db = firestore.Client()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("firestore_keys.json")

doc_ref = db.collection(u'users').document(u'aturing')
doc_ref.set({
    u'first': u'Alan',
    u'middle': u'Mathison',
    u'last': u'Turing',
    u'born': 1912
})