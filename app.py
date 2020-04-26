from flask import Flask, render_template, request, make_response
import predictor
from predictor import predict, FlairActual
import json
import os
from werkzeug.utils import secure_filename
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


@app.route("/automated_testing")
def index():                                                                                         
    return (render_template("testing.html"))

@app.route("/automated_testing", methods = ['POST', 'GET'])
def automated_testing():
	if request.method == 'POST':
		myfile = request.files['upload_file']
		myfile.save(secure_filename(myfile.filename))
		lst = []
		with open(myfile.filename, 'rb') as filein:
			for url in filein:
				lst.append(url)
		result = {}
		for i in lst:
			i = i[:-1]
			pred = predict(i)
			print(pred)
			key = i
			value = pred
			result.update({key : value})
	d = json.dumps(result)
	return json.dumps(d)

@app.errorhandler(404)
@app.errorhandler(500)
def errors(error):
	return (render_template('notfound.html'))

if __name__ == '__main__':
    app.run()