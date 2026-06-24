from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import random
import time

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.0')


@app.route('/')
def home():
    return jsonify({"status": "healthy", "service": "flask-monitor-app"})


@app.route('/api/data')
def get_data():
    time.sleep(random.uniform(0, 0.5))
    return jsonify({"data": [1, 2, 3, 4, 5], "count": 5})


@app.route('/api/error')
def trigger_error():
    if random.random() < 0.5:
        return jsonify({"error": "Simulated error"}), 500
    return jsonify({"status": "ok"})


@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
