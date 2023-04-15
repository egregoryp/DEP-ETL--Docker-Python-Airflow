from api import app
from utils.db import db
from models.customer_models import Customer
from routes.customer_routes import *

if __name__ == '__main__':
    with app.app_context():            
            db.create_all()
    app.run(debug=True)