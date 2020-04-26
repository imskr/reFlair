from flask import Flask, render_template, request, make_response
import predictor
from predictor import predict, FlairActual
import json
import os
port = int(os.environ.get("PORT",5000))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def detect():
	redditURL = request.form['redditpost']
	print(redditURL)
	predicted_flair = str(predict(str(redditURL)))
	actualflair = str(FlairActual(str(redditURL)))
	print(predicted_flair, actualflair)
	return render_template('index.html', predicted_flair = predicted_flair, actualflair = actualflair)


@app.errorhandler(404)
@app.errorhandler(500)
def errors(error):
	return (render_template('notfound.html'))

if __name__ == '__main__':
    app.run()