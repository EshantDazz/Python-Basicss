from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import joblib

# Load the 20 newsgroups dataset
dataset = fetch_20newsgroups(subset='all', shuffle=True, random_state=42)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=42)

# Create a TF-IDF vectorizer to convert text to numeric features
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the training data and transform the training and testing data
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train a LinearSVC model on the training data
model = LinearSVC()
model.fit(X_train, y_train)

# Evaluate the model on the testing data
score = model.score(X_test, y_test)
print(f'Model accuracy: {score:.3f}')

# Save the model as a joblib file
joblib.dump(model, 'model.pkl')