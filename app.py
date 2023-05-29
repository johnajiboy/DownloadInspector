from flask import Flask, request, jsonify
from flask_cors import CORS
from functions import check_malicious


app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download():
    download_link = request.form.get('link')
    is_malicious = check_malicious(download_link)

    if is_malicious:
        return jsonify({'result': 'malicious'})
    else:
        return jsonify({'result': 'safe'})


if __name__ == '__main__':
    app.run(debug=True)
