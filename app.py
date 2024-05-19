import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
## Load the model
classifier = pickle.load(open('classifier.pkl', 'rb'))

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    data = np.array(data).reshape(1,-1)
    output = classifier.predict(data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    data = np.array(data).reshape(1,-1)
    output = classifier.predict(data)[0]
    print(output)
    if output==1:
        return render_template("insomnia.html", prediction_text=f"")
    elif output==2:
        return render_template("apnea.html", prediction_text=f"")
    else:
        return render_template("normal.html", prediction_text=f"")

if __name__ == "__main__":
    app.run(debug=True)
