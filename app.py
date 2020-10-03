from flask import Flask

from routes.routes import configure_routes

app = Flask(__name__)
configure_routes(app)
app.run(debug=True)
