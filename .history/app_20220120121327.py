from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/api/v1.0.0/")
def home():
    
    return {"message":"Welcome to our api"}



@app.route("/api/v1.0.0/students/", methods=["POST","GET"])
def students():
        
    if request.method == "POST":
        
        print(request.json()
        
        # logic for inputting data
        
        
        return {"message":"you posted"}
    
    
    data = []
    
    # open the json file
    with open("./data.json", "r") as f:
        data = json.load(f)
        
    return {"students":data}


@app.route("/api/v1.0.0/students/<int:id>")
def student(id):
        
    students = []
    
    # open the json file
    with open("./data.json", "r") as f:
        data = json.load(f)
        
        students = [i for i in data if i["id"] == id]
        
        if students == []:
            return {"error":"Student not found"}
        
    return students[0]


if __name__ == "__main__":
    app.run(debug=True)