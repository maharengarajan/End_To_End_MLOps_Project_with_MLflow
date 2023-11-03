from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from mlproject.pipeline import PredictionPipeline


#initialize flask app
app = Flask(__name__)


# route to display the home page
@app.route('/',methods=['GET'])  
def homePage():
    return render_template("index.html")


# route to train the pipeline
@app.route('/train',methods=['GET'])  
def training():
    os.system("python main.py")
    return "Training Successful!"


if __name__ == "__main__":
	app.run(host="0.0.0.0", port = 8080, debug=True)