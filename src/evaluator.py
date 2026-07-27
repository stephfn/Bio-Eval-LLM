import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

def calculate_semantic_fidelity(df):
    vectorizer = TfidfVectorizer()
    scores = []
    
    for _, row in df.iterrows():
        tfidf_matrix = vectorizer.fit_transform([row['ground_truth_logic'], row['ai_response']])
        sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        scores.append(round(float(sim), 4))
        
    df['similarity_score'] = scores
    return df

def generate_summary(df):
    total = len(df)
    hallucinations = df['has_hallucination'].sum()
    print(f"--- EVALUATION SUMMARY ---")
    print(f"Total Prompts Evaluated: {total}")
    print(f"Hallucination / Error Rate: {(hallucinations/total)*100:.1f}%")
    print(f"Average Similarity Score: {df['similarity_score'].mean():.4f}")

if __name__ == "__main__":
    df = load_data("data/eval_dataset.json")
    df = calculate_semantic_fidelity(df)
    generate_summary(df)
