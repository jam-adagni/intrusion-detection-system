# Intrusion Detection System

This project uses the NSL-KDD dataset to train a RandomForest classifier for network intrusion detection,
and exposes a Streamlit front-end for real-time prediction.

## Project Structure

datasets/
├── raw/
│   └── download_data.py     # fetches & preprocesses NSL-KDD
└── processed/
    ├── KDDTrain+.csv        # processed train data
    └── KDDTest+.csv         # processed test data

model/
├── train_model.py          # trains & saves ids_model.pkl
└── inference.py            # loads model & predicts CSV inputs

app/
└── streamlit_app.py        # Streamlit UI

requirements.txt             # Python deps