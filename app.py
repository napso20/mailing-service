from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from svc.utils.database_utils import create_db_connection_url


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = create_db_connection_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
