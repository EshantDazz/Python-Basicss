from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('iriss.pkl','rb'))

app=Flask(__name__)


@app.route('/')
def start():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def home():
    d1=float(request.form['a'])
    d2=float(request.form['b'])
    d3=float(request.form['c'])
    d4=float(request.form['d'])
    output=np.array([[d1,d2,d3,d4]])

    pred=model.predict(output)
    return render_template('display.html',data=pred)

if __name__=='__main__':
    app.run(debug=True)
