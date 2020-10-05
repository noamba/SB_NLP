"""
To run flask application in dev, either:
    1) "cd app && export FLASK_APP=main" then "flask run" OR "python main.py"
        This is as required for the dockerized version which will only copy app/
    2) debug via pycharm with working dir set as app/
"""
from flask import Flask

from views.routes import configure_routes
from views.helpers import setup_match_objects


print(__name__)
app = Flask(__name__)

match_dict, phrase_matcher = setup_match_objects()
configure_routes(app, match_dict, phrase_matcher)
print("\n\n*** Match application is ready***")

if __name__ == "__main__":
    # debug=False to avoid "Restarting with stat" msg and following crash
    app.run(debug=False)
