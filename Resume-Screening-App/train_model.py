import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
import pickle

# Load your dataset
# Make sure 'UpdatedResumeDataSet.csv' is in the same directory

df = pd.read_csv('UpdatedResumeDataSet.csv')

# Encode target labels
le = LabelEncoder()
y = le.fit_transform(df['Category'])

# TF-IDF vectorization
# You can use the cleanResume function from your app.py for better results
# For simplicity, we'll use raw text here

tfidf = TfidfVectorizer(stop_words='english')
X = tfidf.fit_transform(df['Resume'])

# Train a classifier
clf = SVC(kernel='linear', probability=True)
clf.fit(X, y)

# Save the model, vectorizer, and label encoder
pickle.dump(clf, open('clf.pkl', 'wb'))
pickle.dump(tfidf, open('tfidf.pkl', 'wb'))
pickle.dump(le, open('encoder.pkl', 'wb'))

print('Training complete. Model and encoders saved.')
