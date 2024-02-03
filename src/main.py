from flask import Flask
from flask_jwt_extended import JWTManager
from src.config import SQLALCHEMY_DATABASE_URI, SECRET_AUTH, db
from src.route.command import route_com

# create app
app = Flask(__name__)

# add config
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['JWT_SECRET_KEY'] = SECRET_AUTH

# connect db
db.init_app(app)
# creat jwt
jwt = JWTManager(app)

# add route command
app.register_blueprint(route_com)


if __name__ == '__main__':
    from src.route.auth import route_auth
    # add route auth
    app.register_blueprint(route_auth)
    app.run(debug=True)
