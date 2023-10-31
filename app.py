from flask import Flask, jsonify, render_template, request
from predict import makePredictionTF, makePredictionSK

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
        # call the correct model for the choice made
        if modelType == 0:
            # tensor flow model
            scamResult = makePredictionTF(targetURL)
        else:
            # sklearn model
            scamResult = makePredictionSK(targetURL)

        # check the result of the prediction
        if scamResult["predict"] == 0:
            # not a scam
            verdeict = "\"" + scamResult["title"] + "\" is not a scam"
        else:
            # a scam
            verdeict = "\"" + scamResult["title"] + "\" is a scam"

        # return the verdict and posting title
        return render_template('process_url.html', targetURL=targetURL, scamResult=verdeict)
    
    # if the url is bad, tell the user
    else:
        return render_template('process_url.html', targetURL=targetURL, scamResult="Invalid url: Must be a https://www.indeed.com/ link")


if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0", port=5000, debug=True) # start the flask web app