from flask import Flask

from app.views.routes import configure_routes
from app.views.helpers import setup_match_objects

app = Flask(__name__)

match_dict, phrase_matcher = setup_match_objects()
configure_routes(app, match_dict, phrase_matcher)

if __name__ == '__main__':
    app.run(debug=True)
