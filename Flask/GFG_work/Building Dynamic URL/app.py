from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')
def hello():
    return "Hello this is the default home page"

@app.route('/valid/<int:age>')
def valid(age):
    return "You have entered "+str(age)+" and you are valid for voting"

@app.route('/not_valid/<int:age>')
def not_valid(age):
    return "You have entered "+str(age)+"  and you are not valid for voting"

@app.route('/result/<int:age>')
def result(age):
    r=''
    if age<18:
        r+='not_valid'
    else:
        r+='valid'
    return redirect(url_for(r,age=age))

if __name__=='__main__':
    app.run(debug=True)