import pandas as pd
import random
from datetime import datetime, timedelta

print("Script Started")

products = [
    "iPhone 16",
    "Samsung Galaxy S25",
    "OnePlus 14",
    "Sony Headphones",
    "Dell Laptop",
    "HP Laptop",
    "LG Monitor",
    "Boat Earbuds",
    "Apple Watch",
    "Canon Camera"
]

positive_reviews = [
    "Excellent product and highly recommended",
    "Amazing quality and worth the money",
    "Battery life is fantastic",
    "Very satisfied with the purchase",
    "Product exceeded my expectations",
    "Fast delivery and great packaging",
    "Camera quality is outstanding",
    "Excellent performance and build quality",
    "Very user friendly and reliable",
    "Five stars from my side"
]

negative_reviews = [
    "Very disappointed with the product",
    "Battery drains too quickly",
    "Poor quality and not worth the price",
    "Stopped working after a few days",
    "Packaging was damaged",
    "Customer support was not helpful",
    "Product heats up frequently",
    "Performance is very slow",
    "Received a defective item",
    "Would not recommend this product"
]

neutral_reviews = [
    "Average product",
    "Product is okay for the price",
    "Nothing special about it",
    "Works as expected",
    "Decent quality",
    "Neither good nor bad",
    "Can be improved",
    "Standard product",
    "Acceptable performance",
    "Met basic expectations"
]

data = []

for i in range(1, 10001):

    sentiment_type = random.choices(
        ["Positive", "Negative", "Neutral"],
        weights=[60, 25, 15],
        k=1
    )[0]

    if sentiment_type == "Positive":
        review = random.choice(positive_reviews)
        rating = random.choice([4, 5])

    elif sentiment_type == "Negative":
        review = random.choice(negative_reviews)
        rating = random.choice([1, 2])

    else:
        review = random.choice(neutral_reviews)
        rating = 3

    review_date = (
        datetime(2025, 1, 1)
        + timedelta(days=random.randint(0, 500))
    ).date()

    data.append([
        i,
        random.choice(products),
        rating,
        review,
        review_date
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Review_ID",
        "Product_Name",
        "Rating",
        "Review_Text",
        "Review_Date"
    ]
)

print("Rows generated:", len(df))
print("\nSample Data:")
print(df.head())

df.to_excel(
    "Data/reviews.xlsx",
    index=False
)

print("\nreviews.xlsx created successfully")
print("File saved to: Data/reviews.xlsx")