from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/health")
def health():
    return render_template(
        "health.html",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


@app.route("/error")
def error():
    app.logger.error("Test application error generated!")

    return render_template(
        "error.html",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ), 500


@app.route("/load")
def load():
    start_time = time.time()

    # Generate CPU workload for approximately 10 seconds
    while time.time() - start_time < 10:
        pass

    return render_template(
        "load.html",
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)