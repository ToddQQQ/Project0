import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(file_path, test_size=0.2):
    column_names = ["sentiment", "tweet_id", "date", "query", "user", "text"]
    df = pd.read_csv(file_path, encoding="latin-1", names=column_names)

    # map the sentiment to 0 and 4
    df["sentiment"] = df["sentiment"].map({0: "negative", 4: "positive"})

    return train_test_split(df["text"], df["sentiment"], test_size=test_size, random_state=42)