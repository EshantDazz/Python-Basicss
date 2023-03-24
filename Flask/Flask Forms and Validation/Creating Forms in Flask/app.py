from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)\

d={}

@app.route('/',methods=['POST','GET'])
def home():
     if request.method=='POST':
          lastname=request.form['lname']
          firstname=request.form['fname']
          d['lastname']=lastname
          d['firstname']=firstname
          return redirect(url_for('update'))
     else:
          return render_template('form.html')

@app.route('/update')
def update():
     return render_template('update.html',name=d['firstname']) 

if __name__=='__main__':
    app.run(debug=True)