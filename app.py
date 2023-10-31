from flask import Flask, jsonify, render_template, request
from predict import makePredictionTF

# Creates Flask
app = Flask(__name__)

# home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_url', methods=['POST'])
def process_url():
    # get url from form
    targetURL = request.form['targetURL']
    # get model version from form
    modelType = request.form.get('modelType')

    # check if the url is valid
    if targetURL[:23] == "https://www.indeed.com/":
        # make a prediction
        scamResult = makePredictionTF(targetURL)

        # check the result of the prediction
        if scamResult["predict"] == 0:
            # not a scam
            verdeict = "\"" + scamResult["title"] + "\" is not likely to be a scam"
        else:
            # a scam
            verdeict = "\"" + scamResult["title"] + "\" has a risk of being a scam"

        # return the verdict and posting title
        return render_template('process_url.html', targetURL=targetURL, scamResult=verdeict)
    
    # if the url is bad, tell the user
    else:
        return render_template('process_url.html', targetURL=targetURL, scamResult="Invalid url: Must be a https://www.indeed.com/ link")


if __name__ == '__main__':
    app.run()