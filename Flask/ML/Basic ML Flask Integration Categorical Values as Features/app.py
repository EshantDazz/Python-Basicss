from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

app = Flask(__name__)

# Load the data
data = pd.read_csv("sample_csv.csv")

# Extract the categorical variables
categorical_variables = {
    "color": data["color"].unique().tolist(),
    "size": data["size"].unique().tolist()
}

# Preprocess the data
onehot_encoder = OneHotEncoder(sparse=False)
X = onehot_encoder.fit_transform(data[categorical_variables.keys()])
y = data["price"]

# Train the model
model = LinearRegression()
model.fit(X, y)

# Define the home page
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html", categorical_variables=categorical_variables)

# Define the result page
@app.route("/", methods=["POST"])
def result():
    # Get the user's input
    color = request.form["color"]
    size = request.form["size"]

    # Convert the input to a one-hot encoded array
    input_data = pd.DataFrame({
        "color": [color],
        "size": [size]
    })
    input_array = onehot_encoder.transform(input_data[categorical_variables.keys()])

    # Make a prediction
    prediction = model.predict(input_array)

    # Display the result
    return render_template("result.html", color=color, size=size, prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)