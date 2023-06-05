from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from functions import check_malicious


app = Flask(__name__)
CORS(app)

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
