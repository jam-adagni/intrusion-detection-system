import streamlit as st
import pandas as pd
import joblib
import os

# ✅ Resolve model path relative to this script
HERE = os.path.dirname(__file__)
MODEL_PATH = os.path.join(HERE, '..', 'model', 'ids_model.pkl')

# ✅ Load the trained model
clf = joblib.load(MODEL_PATH)

# ✅ UI setup
st.title('🔐 Real-Time Intrusion Detection')
uploaded = st.file_uploader("Upload a CSV of features", type='csv')

if uploaded:
    df = pd.read_csv(uploaded)

    st.write("### 📂 Uploaded Data Preview")
    st.dataframe(df)

    # ✅ Get expected features from the model
    expected = clf.feature_names_in_

    # 🧾 Display expected features for reference
    st.write("🧩 Expected columns:", list(expected))

    # ❗ Check for missing columns
    missing = set(expected) - set(df.columns)
    if missing:
        st.error(f"🚫 Missing expected columns: {missing}")
    else:
        # 🧠 Encode categorical features
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype('category').cat.codes

        # 🧩 Select expected features only
        df = df[expected]

        # 🤖 Predict
        preds = clf.predict(df)

        # 📊 Summary
        num_intrusions = sum(preds)
        num_normal = len(preds) - num_intrusions

        st.markdown(f"""
        ### 📈 Prediction Summary  
        - 🟢 Normal connections: **{num_normal}**  
        - 🔴 Intrusions detected: **{num_intrusions}**
        """)

        # 🖍️ Highlight predictions
        results = pd.DataFrame({'prediction': preds})
        styled = results.style.applymap(
            lambda val: 'background-color: red; color: white' if val == 1 else 'background-color: green; color: white'
        )

        st.write("### 📋 Detailed Predictions")
        st.dataframe(styled)

        # 💾 Download option
        csv = results.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Predictions as CSV", csv, "predictions.csv", "text/csv")