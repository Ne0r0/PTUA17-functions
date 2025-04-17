import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, redirect
from forms import MessageForm

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

SECRET_KEY = "my_secret_key"
app.config['SECRET_KEY'] = SECRET_KEY

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(120), unique=True, nullable=False)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, name, surname, message):
        self.name = name
        self.surname = surname
        self.message = message

    def __repr__(self):
        return f'{self.name} - {self.created_at}'
    
@app.route("/", methods=['GET', 'POST'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        surname = form.surname.data
        message = form.message.data
        new_message = Message(name, surname, message)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("index.html", form=form)


@app.route("/about")
def about():
    return render_template("index.html")
    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 