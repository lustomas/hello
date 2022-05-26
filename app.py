from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('parent.html')

@app.route("/mypage/me")
def me():
    return render_template('me.html')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       return render_template('contact.html')
   elif request.method == 'POST':
       print(request.contact)
       return redirect("/mypage/me")

