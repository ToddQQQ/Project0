import pandas as pd
import os

DATA_DIR = "data"

chatgpt_path = os.path.join(DATA_DIR, "chatgpt.csv")
bard_path = os.path.join(DATA_DIR, "bard.csv")

chatgpt_df = pd.read_csv(chatgpt_path)
bard_df = pd.read_csv(bard_path)

print("ChatGPT :")
print(chatgpt_df.head())

print("\n Bard")
print(bard_df.head())