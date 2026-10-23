import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    """Render the Heritage Treasures homepage."""
    return render_template("index.html")


@app.route("/health")
def health():
    """Health-check endpoint for deployment monitoring."""
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1212))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    )