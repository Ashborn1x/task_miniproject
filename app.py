from flask import Flask
from flask_cors import CORS
from extensions import db, bcrypt, jwt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# init extensions
db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)
CORS(app)

# import routes AFTER app & db are ready
from routes.auth import auth_bp
from routes.tasks import tasks_bp

app.register_blueprint(auth_bp, url_prefix="/api")
app.register_blueprint(tasks_bp, url_prefix="/api")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
