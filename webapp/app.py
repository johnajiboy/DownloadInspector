from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from functions import check_malicious, create_users_table, create_user, check_login_info


app = Flask(__name__)
CORS(app)

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        create_users_table()
        create_user(name, email, password)
        return redirect('/login')
    return render_template('signup.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        if check_login_info(name, password) == True:
            return redirect('/')
        else:
            return redirect('/login')
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
      data = request.form
      download_link = data.get('link')
      is_malicious = check_malicious(download_link)
      return render_template('result.html', is_malicious=is_malicious, link=download_link)
   else:
       return render_template('index.html')

def run_app():
    app.run(port=5001, debug=True)
if __name__ == '__main__':
    run_app()
