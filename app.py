from flask import Flask, request, render_template
#from flask_cors import CORS
from functions import check_malicious


app = Flask(__name__)
#CORS(app)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        download_link = request.form.get('link')
        is_malicious = check_malicious(download_link)
        return render_template('result.html', is_malicious=is_malicious, link=download_link)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
