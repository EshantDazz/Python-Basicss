from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def hello():
    return "This is the default homepage"


@app.route('/valid/<int:age>')
def valid(age):
    v=''
    if age>=18:
        v+='Valid'
    else:
        v+="Not Valid"
    result={'Age':age,'Result':v}
    return render_template('result.html',res=result)


if __name__=='__main__':
    app.run(debug=True)