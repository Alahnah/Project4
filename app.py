from flask import Flask, jsonify, render_template, request
from predict import makePrediction

# Creates Flask
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    targetURL = request.form['targetURL']
    if targetURL[:23] == "https://www.indeed.com/":
        # Call your Python function with the input value
        scamResult = makePrediction(targetURL)
        return render_template('process_url.html', targetURL=targetURL, scamResult=scamResult)
    else:
        return render_template('process_url.html', targetURL=targetURL, scamResult="Invalid url: Must be a https://www.indeed.com/ link")


if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0", port=5000, debug=True) # start the flask web app