from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydatabase_1.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SECRET_KEY"]=os.urandom(32)
app.config["DEBUG"]=True
db=SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

# Create all tables in the database (if they don't exist yet)
with app.app_context():
    db.create_all()

@app.route('/index')  # Homepage
def home():
    return render_template('index.html')

@app.route('/hobby')  # Hobby
def hobby():
    return render_template('hobby.html')

@app.route('/portfolio')  # Portfolio
def portfolio():
    return render_template('portfolio.html')

@app.route('/contact', methods = ['GET','POST'])  # Contact
def contact():
    if request.method =="POST":
      name = request.form.get("name")
      email = request.form.get("email")
      subject = request.form.get("subject")
      message = request.form.get("message")

      # Create a new Contact
      contact = Contact(name=name, email=email, subject=subject, message=message)

      # Add the new Contact to the session and commit it
      db.session.add(contact)
      db.session.commit()

      if contact.id is not None:
        message = "Message sent!"
        return render_template("contact.html", message=message)
      else:
        message = "Incomplete information. Please try again!"
        return render_template("contact.html", message=message)
    else:
      return render_template("contact.html")

@app.route('/resumeNuar') #to Anuar resume
def resumenuar():
    return render_template('resumeAnuar.html')

@app.route('/hobbyNuar') #to Anuar hobby page
def hobbynuar():
    return render_template('hobbyAnuar.html')

@app.route('/resumeSoleh') #to Soleh resume
def resumesoleh():
    return render_template('resumeSoleh.html')

@app.route('/hobbySoleh') #to Soleh hobby page
def hobbysoleh():
    return render_template('hobbySoleh.html')

@app.route('/') #to landng page
def landing():
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(debug=True)
