import flask
from flask import Flask,redirect,url_for,render_template
 
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")
@app.route('/i-am-new')
def i_am_new():
    return render_template("iamnew.html")

if __name__ == '__main__':
 
    app.run()