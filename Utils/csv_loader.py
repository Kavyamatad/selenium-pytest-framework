# utils/csv_loader.py
import pandas as pd

def load_locators(file_path="data/test_path.csv"):
    df = pd.read_csv(file_path)
    return dict(zip(df["element_name"], df["xpath"]))