from flask import Flask

from views.routes import configure_routes
from views.helpers import setup_match_objects

"""
    runs now with
        1) python app/main.py - as required for the dockerized version
        2) debug via pycharm
    It does not run with "export FLASK_APP=app.main  && flask run"
    
    Had to remove app. from all imports and
    change below to app.run(debug=False) to avoid "Restarting with stat" msg
    and following crash
"""

print(__name__)
app = Flask(__name__)

match_dict, phrase_matcher = setup_match_objects()
configure_routes(app, match_dict, phrase_matcher)

if __name__ == "__main__":
    app.run(debug=False)
