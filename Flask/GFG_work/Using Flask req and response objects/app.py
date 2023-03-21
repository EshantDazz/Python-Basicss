from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        response = make_response(f'Hello, {name}!')
    else:
        response = make_response('Hello, World!')

    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__=='__main__':
    app.run(debug=True)