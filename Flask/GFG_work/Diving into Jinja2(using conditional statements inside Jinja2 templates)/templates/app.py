from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello this is the home webpage"

@app.route('/valid/<int:no>')
def valid(no):
    return render_template('valid.html',age=no)


if __name__=='__main__':
    app.run(debug=True)