import sys
import pandas as pd
import joblib

# Usage: python inference.py [path/to/input.csv]
model = joblib.load('model/ids_model.pkl')
in_csv = sys.argv[1] if len(sys.argv)>1 else '../datasets/processed/KDDTest+.csv'
df = pd.read_csv(in_csv)

# Encode categorical to match training preprocessing
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype('category').cat.codes

preds = model.predict(df)
print(preds)