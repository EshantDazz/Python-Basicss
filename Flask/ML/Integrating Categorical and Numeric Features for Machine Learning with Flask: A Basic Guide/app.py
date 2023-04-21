from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the dataset
df = pd.read_csv('sample.csv')

# Extract the categorical variables
categorical_variables = {}
for col in df.columns:
    if df[col].dtype == 'object':
        categorical_variables[col] = df[col].unique()

# Define the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the form data
        color = request.form['color']
        size = request.form['size']
        weight = float(request.form['weight'])

        # Filter the dataset based on the form data
        X = df[(df['color'] == color) & (df['size'] == size)]['weight'].values.reshape(-1, 1)
        y = df[(df['color'] == color) & (df['size'] == size)]['price'].values

        # Train a linear regression model on the filtered dataset
        model = LinearRegression()
        model.fit(X, y)

        # Predict the price for the given weight
        price = model.predict([[weight]])

        # Render the result page with the input values and prediction
        return render_template('result.html', input_values=[color, size, weight], prediction=price[0])

    else:
        # Render the home page
        return render_template('index.html', categorical_variables=categorical_variables)

if __name__ == '__main__':
    app.run(debug=True)