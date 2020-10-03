from flask import Flask

from routes.routes import configure_routes
from settings import REDUCE_CATEGORY_SET_SIZE

app = Flask(__name__)
configure_routes(app, reduce_category_set_size=REDUCE_CATEGORY_SET_SIZE)
app.run(debug=True)
