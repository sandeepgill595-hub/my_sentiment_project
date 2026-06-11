import pandas as pd
from transformers import pipeline

print("Loading model...")

classifier = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

print("Model loaded successfully")

df = pd.read_excel(
    "Data/reviews.xlsx",
    engine="openpyxl"
)

print("Rows loaded:", len(df))

sentiments = []
scores = []

for i, review in enumerate(df["Review_Text"]):

    result = classifier(str(review))[0]

    sentiments.append(result["label"])
    scores.append(round(result["score"] * 100, 2))

    if (i + 1) % 500 == 0:
        print(f"Processed {i+1} reviews")

df["Predicted_Sentiment"] = sentiments
df["Confidence"] = scores

df.to_excel(
    "Data/results.xlsx",
    index=False
)

print("Analysis completed")
print("Results saved to Data/results.xlsx")