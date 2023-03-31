from flask import Flask,request,render_template
import tensorflow as tf
import re
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer 
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
tokenizer = Tokenizer()
model = tf.keras.models.load_model("/Users/softweredevloper/PycharmProjects/api/model/solutionChalange.h5")
arr = ['suicide', 'loneliness', 'Emotional distress', 'General sadness', 'depressed',
       'Overwhelm', 'sleep', 'Work stress', 'scared', 'worthless', 'anxious', 'General stress',
       'Academic stress', 'death']
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST': 
        print(request)  
        query = request
        text = []
        txt = re.sub('[^a-zA-Z\']', ' ', query)
        txt = txt.lower()
        txt = txt.split()
        txt = " ".join(txt)
        text.append(txt)
        print(text)
        # text = ["this is a good day"]
        tokenizer.fit_on_texts(text)
        x_test = tokenizer.texts_to_sequences(text)
        print(x_test)
        x_test = np.array(x_test).squeeze()
        print(x_test)
        x_test = pad_sequences([x_test], padding='post', maxlen=42)
        print(x_test)
        y_pred = model.predict(x_test)
        y_pred = y_pred.argmax()
        print(y_pred)
        print(arr[y_pred])
        return ("Hi"+arr[y_pred])
    return None


@app.route('/ex')
def func():
    name = request.args.get('name')
    return f'Hello, {name}!'
if __name__ == '__main__':
    app.run(debug=True)