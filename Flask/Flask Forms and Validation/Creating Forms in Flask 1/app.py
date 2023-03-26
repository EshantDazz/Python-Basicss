from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        fname=request.form.get('fname')
        lname=request.form.get('lname')
        email=request.form.get('email')
        print("First Name = ",fname)
        print("Last Name = ",lname)
        print("Email ",email)

    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True)

