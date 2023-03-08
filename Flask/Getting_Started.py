from flask import Flask

#WSGI application
app=Flask(__name__)

@app.route('/')
def Welcome():
    return "Jangkilt here.Hello "

@app.route('/holi')
def holi():
    return "Happy Holi "



if __name__=='__main__':
    app.run(debug=True)