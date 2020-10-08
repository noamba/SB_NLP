"""
Note for developer:
To run flask application in dev:
Activated, "cd app && export FLASK_APP=main" then "flask run" OR
"python main.py". This setup is as required for the dockerized
version which will only copy app/
"""
from flask import Flask

from views.routes import configure_routes
from views.helpers import setup_match_objects

print("\n\n>>> Match application is starting... <<<\n\n")

app = Flask(__name__)

match_dict, phrase_matcher = setup_match_objects()
configure_routes(app, match_dict, phrase_matcher)

print("\n\n>>> Match application is ready <<<\n\n")

if __name__ == "__main__":
    # Note: debug=False to avoid "Restarting with stat" msg and following crash
    app.run(debug=False)
