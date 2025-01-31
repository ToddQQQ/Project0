import os
import pandas as pd
import re
import chardet
import nltk
from nltk.corpus import stopwords

# download NLTK resources
nltk.download("stopwords")

# Define the data directory (make sure your CSV files are stored in this directory)
DATA_DIR = "data"

def detect_encoding(file_path):
    """
    Detect the encoding of a file using chardet.
    """
    with open(file_path, "rb") as f:
        result = chardet.detect(f.read(100000))  # 读取前 100000 字节
    return result["encoding"]

def clean_text(text):
    """
    Clean tweet text by removing URLs, special characters, and stopwords.
    """
    if not isinstance(text, str):
        return ""

    text = re.sub(r"http\S+|www\S+", "", text)  # remove URL
    text = re.sub(r"@\w+", "", text)  # remove @account
    text = re.sub(r"[^A-Za-z\s]", "", text)  # remove special characters
    text = text.lower().strip()  # convert to lowercase
    stop_words = set(stopwords.words("english"))
    words = text.split()
    cleaned_words = [word for word in words if word not in stop_words]  # remove stopwords
    return " ".join(cleaned_words)

def load_and_clean_data(data_dir):
    """
    Load multiple CSV files from the data directory and clean their text.
    """
    all_data = []
    
    for file in os.listdir(data_dir):
        if file.endswith(".csv"):
            file_path = os.path.join(data_dir, file)
            encoding = detect_encoding(file_path)  # detect encoding
            try:
                df = pd.read_csv(file_path, encoding=encoding)
                if "text" in df.columns:
                    df["cleaned_text"] = df["text"].apply(clean_text)
                    all_data.append(df[["cleaned_text"]])
            except Exception as e:
                print(f"⚠️ Error reading {file_path}: {e}")

    # combine all data
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        return combined_df
    else:
        print("⚠️ No valid data found.")
        return pd.DataFrame()

# Run the data loading and cleaning process
if __name__ == "__main__":
    print("🚀 Loading and cleaning data...")
    cleaned_df = load_and_clean_data(DATA_DIR)

    if not cleaned_df.empty:
        print("✅ Data cleaning complete! Sample output:")
        print(cleaned_df.head())  # pritn the first few rows
        cleaned_df.to_csv("data/cleaned_data.csv", index=False)  # save the cleaned data
        print("📂 Cleaned data saved to 'data/cleaned_data.csv'.")
    else:
        print("⚠️ No data processed.")