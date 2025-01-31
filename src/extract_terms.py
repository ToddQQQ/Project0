import pandas as pd
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_terms(text):
    """ extract terms"""
    doc = nlp(text.lower())
    terms = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop]
    return list(set(terms)) 

def process_dataset(file_path):
    """ deal with dataset """
    df = pd.read_csv(file_path)
    df["ai_terms"] = df["cleaned_text"].apply(extract_terms)
    return df

if __name__ == "__main__":
    dataset_path = "data/cleaned_data.csv"
    print("🚀 Extracting AI-related terms...")
    processed_df = process_dataset(dataset_path)
    
    terms_df = processed_df[["ai_terms"]]
    terms_df.to_csv("data/ai_terms.csv", index=False)
    print("AI terms extracted and saved to 'data/ai_terms.csv'.")