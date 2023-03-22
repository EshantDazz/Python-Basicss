from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello():
    return 'This is the home page'

@app.route('/about')
def about():
    return "Here we will show you how to pass down values within the function parameter"

@app.route('/number/<int:no>')
def number(no):
    return "The number you have entered is "+str(no)

@app.route('/word/<string:w>')
def word(w):
    return f"The word you have chosen is {w}"

if __name__=='__main__':
    app.run(debug=True)