# run_all.ps1
Param()

# 1) Ensure venv active (skip if global)
.\venv\Scripts\Activate.ps1

# 2) Download & preprocess
Write-Host "🔽 Downloading & preprocessing data…"
python .\datasets\raw\download_data.py

# 3) (Optional) Rename to match model script
Write-Host "🔄 Renaming processed files…"
ren .\datasets\processed\KDDTrain.csv  KDDTrain+.csv
ren .\datasets\processed\KDDTest.csv   KDDTest+.csv

# 4) Train model
Write-Host "🛠️  Training model…"
python .\model\train_model.py

# 5) Quick inference test
Write-Host "✅ Quick test on KDDTest+…"
python .\model\inference.py ..\datasets\processed\KDDTest+.csv

# 6) Launch Streamlit
Write-Host "🚀 Launching Streamlit UI…"
python -m streamlit run .\app\streamlit_app.py