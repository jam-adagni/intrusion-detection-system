import os
import requests
import pandas as pd

# Raw URLs for NSL-KDD on GitHub
URLS = {
    'train': 'https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTrain+.txt',
    'test':  'https://raw.githubusercontent.com/defcom17/NSL_KDD/master/KDDTest+.txt'
}

# Column names for NSL-KDD (41 features + label)
col_names = [
    "duration","protocol_type","service","flag","src_bytes","dst_bytes","land",
    "wrong_fragment","urgent","hot","num_failed_logins","logged_in","num_compromised",
    "root_shell","su_attempted","num_root","num_file_creations","num_shells",
    "num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count",
    "srv_count","serror_rate","srv_serror_rate","rerror_rate","srv_rerror_rate",
    "same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count",
    "dst_host_srv_count","dst_host_same_srv_rate","dst_host_diff_srv_rate",
    "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate",
    "dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate",
    "label"
]

os.makedirs('datasets/raw', exist_ok=True)
os.makedirs('datasets/processed', exist_ok=True)

for split, url in URLS.items():
    print(f"Downloading NSL-KDD {split} set...")
    r = requests.get(url)
    raw_path = f"datasets/raw/KDD{split.title()}.txt"
    with open(raw_path, 'wb') as f:
        f.write(r.content)
    print(f"Saved raw to {raw_path}")

    # Read & save as CSV
    df = pd.read_csv(raw_path, names=col_names)
    out_csv = f"datasets/processed/KDD{split.title()}.csv"
    df.to_csv(out_csv, index=False)
    print(f"Processed CSV saved to {out_csv}")