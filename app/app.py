from flask import Flask, jsonify, render_template


app = Flask(__name__)

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


@app.route("/todo")
def todo():
    return render_template("todo.html")



if __name__ == "__main__":
    app.run(debug=True)
