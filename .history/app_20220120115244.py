from flask import Flask
import json

app = Flask(__name__)


@app.route("/api/v1.0.0/")
def home():
    
    return {"message":"Welcome to our api"}


@app.route("/api/v1.0.0/")
def students():
        
    data = []
    
    # open the json file
    with open("./data.json", "r") as f:
        data = json.load(f)
        
    return {"students":data}


if __name__ == "__main__":
    app.run(debug=True)