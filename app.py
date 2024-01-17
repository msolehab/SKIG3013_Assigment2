from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os


app = Flask(__name__)
# Get the absolute path to the directory where your Flask application is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Use the absolute path to your database file
db_path = os.path.join(BASE_DIR, "mydatabase_1.db")

def create_table():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS contact(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      email TEXT NOT NULL,
      subject TEXT NOT NULL,
      message TEXT NOT NULL
    )
    '''
    cursor.execute(create_table_query)
    conn.commit()

create_table()  # Call this function when your application starts


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

      conn = sqlite3.connect('mydatabase_1.db')  # Connect to the database
      cursor = conn.cursor()
      #query
      insert_query = '''
        INSERT INTO contact (name, email, subject, message)
        VALUES (?, ?, ?, ?);
        '''
      cursor.execute(insert_query, (name, email, subject, message))
      conn.commit()

      if cursor.rowcount > 0:
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
