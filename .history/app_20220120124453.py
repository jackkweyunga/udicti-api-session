from flask import Flask, request
import json

app = Flask(__name__)


@app.route("/api/v1.0.0/")
@app.route("/")
def home():
    
    return {
        "message":"Welcome to our api",
        ""}



@app.route("/api/v1.0.0/students/", methods=["POST","GET"])
def students():
        
    if request.method == "POST":
        
        new_student = request.json
        
        if "name" not in new_student.keys() or new_student == {}:
            return {"error":"field 'name' is required"}
        
        # logic for inputting data
        data = []
    
        # open the json file
        with open("./data.json", "r") as f:
            data = json.load(f)
            new_id = data[-1]["id"] + 1
            new_student["id"] = new_id
            data.append(new_student)
            
        # with open("./data.json", "w") as f:
        #     json.dump(data, f)  
        
        return new_student
    
    
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