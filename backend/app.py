from flask import Flask
from routes.resume_routes import resume_bp

app = Flask(__name__)
app.register_blueprint(resume_bp)

if __name__ == "__main__":
    app.run(debug=True)
