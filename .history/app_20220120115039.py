from flask import Flask
import json

app = Flask(__name__)


@app.route("/api/v1.0.0/")
def home():
    
    data = []
    
    # open the json file
    with open("./data.json", "r") as f:
        data = 
    return {"name":"jackson"}


if __name__ == "__main__":
    app.run(debug=True)