#Building URL Dynamically
'''
1. Variable Rules
2. URL building
'''

from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Hello how are you"


#variable rules technique 
@app.route('/success/<int:score>')
def marks(score):
    return "You have scored "+str(score)+" marks and success"

@app.route('/fail/<int:score>')
def fail(score):
    return "You have scored "+str(score)+" marks and failed"


#result checker
@app.route('/result/<int:marks>')
def results(marks):
    result=''
    if marks<50:
        result+='fail'
    else:
        result+='success'
    return redirect(url_for(result,score=marks))



if __name__=='__main__':
    app.run()