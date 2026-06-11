import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------
# PAGE CONFIG
# ------------------------

st.set_page_config(
    page_title="Customer Review Sentiment Analysis",
    layout="wide"
)

# ------------------------
# LOAD DATA
# ------------------------

df = pd.read_excel("reviews.xlsx", engine="openpyxl")

# ------------------------
# SIDEBAR FILTERS
# ------------------------

st.sidebar.header("Filters")

selected_product = st.sidebar.selectbox(
    "Product",
    ["All"] + sorted(df["Product_Name"].unique().tolist())
)

selected_sentiment = st.sidebar.selectbox(
    "Sentiment",
    ["All"] + sorted(df["Predicted_Sentiment"].unique().tolist())
)

selected_rating = st.sidebar.selectbox(
    "Rating",
    ["All"] + sorted(df["Rating"].unique().tolist())
)

confidence_filter = st.sidebar.slider(
    "Minimum Confidence %",
    min_value=0,
    max_value=100,
    value=0
)

filtered_df = df.copy()

if selected_product != "All":
    filtered_df = filtered_df[
        filtered_df["Product_Name"] == selected_product
    ]

if selected_sentiment != "All":
    filtered_df = filtered_df[
        filtered_df["Predicted_Sentiment"] == selected_sentiment
    ]

if selected_rating != "All":
    filtered_df = filtered_df[
        filtered_df["Rating"] == selected_rating
    ]

filtered_df = filtered_df[
    filtered_df["Confidence"] >= confidence_filter
]

# ------------------------
# TITLE
# ------------------------

st.title("📊 Customer Review Sentiment Analysis Dashboard")

st.markdown("---")

# ------------------------
# KPI SECTION
# ------------------------

total_reviews = len(filtered_df)

positive_reviews = len(
    filtered_df[
        filtered_df["Predicted_Sentiment"] == "positive"
    ]
)

negative_reviews = len(
    filtered_df[
        filtered_df["Predicted_Sentiment"] == "negative"
    ]
)

neutral_reviews = len(
    filtered_df[
        filtered_df["Predicted_Sentiment"] == "neutral"
    ]
)

avg_confidence = round(
    filtered_df["Confidence"].mean(),
    2
)

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Total Reviews",
    total_reviews
)

col2.metric(
    "Positive",
    positive_reviews
)

col3.metric(
    "Negative",
    negative_reviews
)

col4.metric(
    "Neutral",
    neutral_reviews
)

col5.metric(
    "Avg Confidence %",
    avg_confidence
)

st.markdown("---")

# ------------------------
# PIE CHART
# ------------------------

col1, col2 = st.columns(2)

with col1:

    sentiment_pie = px.pie(
        filtered_df,
        names="Predicted_Sentiment",
        title="Sentiment Distribution"
    )

    st.plotly_chart(
        sentiment_pie,
        use_container_width=True
    )

# ------------------------
# PRODUCT CHART
# ------------------------

with col2:

    product_chart = px.histogram(
        filtered_df,
        x="Product_Name",
        color="Predicted_Sentiment",
        title="Product-wise Sentiment",
        barmode="group"
    )

    st.plotly_chart(
        product_chart,
        use_container_width=True
    )

st.markdown("---")

# ------------------------
# TOP PRODUCTS
# ------------------------

st.subheader("Top Products by Review Count")

product_summary = (
    filtered_df
    .groupby("Product_Name")
    .size()
    .reset_index(name="Review_Count")
    .sort_values(
        by="Review_Count",
        ascending=False
    )
)

st.dataframe(product_summary)

st.markdown("---")

# ------------------------
# DOWNLOAD BUTTON
# ------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="Download Filtered data",
    data=csv,
    file_name="filtered_sentiment_results.csv",
    mime="text/csv"
)

st.markdown("---")

# ------------------------
# REVIEW DATA
# ------------------------

st.subheader("Review data")

st.dataframe(filtered_df)
