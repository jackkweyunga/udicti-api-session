from flask import Flask

app = Flask(__name__)


@app.route("/api/")
def home():
    return {"name":"jackson"}


if __name__ == "__main__":
    app.run(debug=True)