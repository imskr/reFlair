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


@app.route("/automated_testing", methods = ['POST'])
def index():                                                                                         
    return (render_template("testing.html"))

def automated_testing():
	myfile = request.files['upload_file']
	myfile.save(myfile.filename)
	lst = []
	with open(myfile.filename, 'r') as filein:
		for url in filein:
			lst.append(url)
	dic = {}
	for i in lst:
		i = i[:-1]
		pred = predict(i)
		key = i
		value = pred[0]
		dic.update({key : value})
	d = json.dumps(dic)
	return json.dumps(d)

@app.errorhandler(404)
@app.errorhandler(500)
def errors(error):
	return (render_template('notfound.html'))

if __name__ == '__main__':
    app.run()