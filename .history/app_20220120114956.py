from flask import Flask

app = Flask(__name__)


@app.route("/api/v1.0.0/")
def home():
    
    data = []
    
    
    return {"name":"jackson"}


if __name__ == "__main__":
    app.run(debug=True)