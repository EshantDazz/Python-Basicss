import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Load the data
df = pd.read_csv("data.csv")

# Split the data into training and testing sets
train_data = df.sample(frac=0.8, random_state=42)
test_data = df.drop(train_data.index)

# Create a pipeline for text classification
pipeline = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

# Train the model
pipeline.fit(train_data["text"], train_data["label"])

# Test the model
predicted_labels = pipeline.predict(test_data["text"])
accuracy = accuracy_score(test_data["label"], predicted_labels)
print(f"Accuracy: {accuracy}")


from flask import Flask, render_template, request
app = Flask(__name__)

# Load the model
pipeline = Pipeline([
    ("vectorizer", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])
pipeline.fit(df["text"], df["label"])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form["text"]
        predicted_label = pipeline.predict([text])[0]
        return render_template("index.html", predicted_label=predicted_label)
    else:
        return render_template("index.html", predicted_label=None)
	
if __name__=='__main__':
	app.run(debug=True)