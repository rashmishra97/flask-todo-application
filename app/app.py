from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask app running successfully"})

@app.route("/api")
def api():
    return jsonify({"status": "API working"})

if __name__ == "__main__":
    app.run(debug=True)
