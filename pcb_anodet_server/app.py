from flask import Flask, session
from api import api_blueprint
import threading


thread_lock = threading.Lock()

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(api_blueprint)
app.secret_key = "AOI"
app.config["SESSION_TYPE"] = "filesystem"


@app.before_request
def before_request():
    if thread_lock.locked():
        return "Server busy", 1112
    thread_lock.acquire()


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    try:
        thread_lock.release()
    except:
        pass
    return response


def main():
    app.run(debug=False, host="0.0.0.0")


if __name__ == "__main__":
    main()
