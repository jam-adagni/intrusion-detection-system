import os
import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import joblib

# Usage: python train_model.py [path/to/KDDTrain+.csv]
data_path = sys.argv[1] if len(sys.argv)>1 else '../datasets/processed/KDDTrain+.csv'
print("Loading training data from", data_path)
df = pd.read_csv(data_path)

# Separate features & label
y = df['label']
X = df.drop(['label'], axis=1)

# Encode categorical columns
for col in X.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])

# Train
clf = RandomForestClassifier(n_estimators=100, random_state=42)
print("Training RandomForest...")
clf.fit(X, y)

# Save
os.makedirs('model', exist_ok=True)
joblib.dump(clf, 'model/ids_model.pkl')
print("Model saved to model/ids_model.pkl")