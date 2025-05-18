import time
import os
import pandas as pd

while True: 
    if os.path.exists("files/temps_today.csv"):
        try:
            df = pd.read_csv("files/temps_today.csv")
            print(df)
        except Exception as e:
            print(f"Error reading CSV file: {e}")