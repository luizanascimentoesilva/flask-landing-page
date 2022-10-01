import os, sqlite3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)

db_path = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
db_uri = 'sqlite:///{}'.format(db_path)

app.config.update(dict(
    SQLALCHEMY_DATABASE_URI=db_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
))

db = SQLAlchemy(app)

class UserComments(db.Model):
    _tablename_= 'userComments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    commentary = db.Column(db.String)
    created_at = db.Column(db.DateTime(timezone=True))


@app.route('/')
def index():
    return render_template('home.html')

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/add_comment', methods=['POST'])
def add_record():
    today = date.today()
    db.session.add(UserComments(name=request.form['Name'],  email=request.form['Email'], commentary=request.form['Comment'], created_at=today ))
    db.session.commit()
    return "Comentário salvo"

if __name__ == "__main__":
    app.run(debug=True)

