from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/index')  # Homepage
def home():
    return render_template('index.html')


@app.route('/hobby')  # Hobby
def hobby():
    return render_template('hobby.html')


@app.route('/portfolio')  # Portfolio
def portfolio():
    return render_template('portfolio.html')


@app.route('/contact')  # Contact
def contact():
    return render_template('contact.html')

@app.route('/resumeNuar') #to Anuar resume
def resumenuar():
    return render_template('resumeAnuar.html')

@app.route('/hobbyNuar') #to Anuar resume
def hobbynuar():
    return render_template('hobbyAnuar.html')

@app.route('/resumeSoleh') #to Anuar resume
def resumesoleh():
    return render_template('resumeSoleh.html')

@app.route('/hobbySoleh') #to Anuar resume
def hobbysoleh():
    return render_template('hobbySoleh.html')

@app.route('/') #to Anuar resume
def landing():
    return render_template('landing.html')

if __name__ == "__main__":
    app.run(debug=True)
