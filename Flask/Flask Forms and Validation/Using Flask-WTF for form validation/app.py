from flask import Flask,render_template,request,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import data_required,length


app=Flask(__name__)
app.config['SECRET_KEY']='GeeksforGeeks'
DataForm={}

#class which inherits froom the FlaskForm
class Validation(FlaskForm):
    username=StringField('First Name',validators=[data_required(),length(min=3)])
    password=PasswordField('Password',validators=[length(min=5,message='You need to enter minimum 5 hcaracters')])
    submit=SubmitField('Submit')

@app.route('/',methods=['POST','GET'])
def home():
    form=Validation()
    if form.validate_on_submit():
        username=form.username.data
        password=form.password.data
        return render_template('output.html',username=username,password=password)
    else:
        return render_template('form.html',form=form)
    

if __name__=="__main__":
    app.run(debug=True)
