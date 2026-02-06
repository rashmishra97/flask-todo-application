from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient, render_template


app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.todo_db
collection = db.todo_items


@app.route("/")
def home():
    return jsonify({"message": "Flask app running successfully!"})


@app.route("/api")
def api():
    return jsonify({
        "project": "Flask To-Do Application",
        "author": "Rashmi Mishra",
        "version": "1.0",
        "status": "API updated in rashmi_new branch"
    })


@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.json

    item = {
        "itemName": data.get("itemName"),
        "itemDescription": data.get("itemDescription")
    }

    collection.insert_one(item)

    return jsonify({
        "message": "To-Do item stored successfully",
        "data": item
    }), 201



@app.route("/todo")
def todo():
    return render_template("todo.html")



if __name__ == "__main__":
    app.run(debug=True)
