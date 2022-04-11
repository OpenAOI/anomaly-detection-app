from flask import Flask
from api import api_blueprint


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(api_blueprint)
app.secret_key = "AOI"
app.config["SESSION_TYPE"] = "filesystem"


def main():
    app.run(debug=False, host="0.0.0.0")


if __name__ == "__main__":
    main()
