from flask import Flask, jsonify
import time

app = Flask(__name__)

start_time = time.time()
request_count = 0


@app.route("/")
def home():
    return "Delivery Metrics Exporter is running!"


@app.route("/metrics")
def metrics():
    global request_count
    request_count += 1

    uptime = time.time() - start_time

    return jsonify({
        "application": "delivery-metrics-exporter",
        "requests_total": request_count,
        "uptime_seconds": round(uptime, 2)
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)