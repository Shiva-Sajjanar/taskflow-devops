from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "TaskFlow API is running"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "taskflow-api",
        "version": "1.0.0",
        "environment": "development"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

