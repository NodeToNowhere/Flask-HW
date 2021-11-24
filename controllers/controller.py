from flask import render_template
from app import app
from models.customer_order import orders


@app.route("/orders")
def index():
    return render_template("index.html", title="Orders", orders=orders)
