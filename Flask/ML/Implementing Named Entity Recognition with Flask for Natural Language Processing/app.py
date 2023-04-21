from flask import Flask, render_template, request
import spacy

app = Flask(__name__)
nlp = spacy.load('en_core_web_sm')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return render_template('index.html', entities=entities)

if __name__ == '__main__':
    app.run(debug=True)


