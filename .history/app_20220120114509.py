from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hellow world"


if __name__ == "__main__"