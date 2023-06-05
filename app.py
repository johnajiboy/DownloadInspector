from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from functions import check_malicious


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST'])
def index():
   data = request.get_json()
   download_link = data.get('downloadLink')
   is_malicious = check_malicious(download_link)
   return jsonify({'is_malicious': is_malicious})

def run_app():
    app.run(debug=True)
if __name__ == '__main__':
    run_app()
