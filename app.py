from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:0350@localhost/bmi'
db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)

    def __init__(self, email_, height_, weight_):
        self.email_ = email_
        self.height = height_
        self.weight = weight_


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/thankyou", methods=['POST'])
def thankyou():
    if request.method == 'POST':
        email = request.form["email_name"]
        height = request.form["height_name"]
        weight = request.form["weight_name"]
        print(request.form)
        data = Data(email, height, weight)
        db.session.add(data)
        db.session.commit()
        return render_template("thankyou.html")


if __name__ == '__main__':
    app.debug = True
    app.run()