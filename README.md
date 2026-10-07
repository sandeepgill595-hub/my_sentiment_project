# Customer Review Sentiment Analysis

An end-to-end sentiment analysis project: Python scores customer reviews as Positive, Negative or Neutral, a Streamlit app lets you explore the results, and a Power BI dashboard summarizes them.

**Live demo:** [https://mysentimentproject-cqwimqdgu84xhgumzmp44e.streamlit.app/]


## Business problem
Support and product teams receive large volumes of free-text reviews and cannot read them all. This project turns raw reviews into sentiment counts, trends and common words so a team can see what customers are happy or unhappy about.

## Data
- `reviews.xlsx`: input reviews.
- `results.xlsx`: reviews with the sentiment label and score added by the analysis script.
- No real customer data is used.

## What it does
1. `generate_reviews.py` creates the sample review dataset.
2. `app.py` is a Streamlit app that shows sentiment distribution, word clouds and filters.
3. `Sentiment Analysis.pbix` is a Power BI report built on `results.xlsx`.

## Key findings
*Based on 10,000 synthetic reviews (Jan 2025 – May 2026) across 10 products, used to demonstrate the analysis pipeline.*

- **Sentiment split:** 62.2% positive (6,217), 21.8% negative (2,179) and 16.0% neutral (1,604).
- **Matches star ratings:** every review rated 4–5 stars was classified positive, and 80% of 1–2 star reviews were classified negative.
- **Main complaint themes:** defects or "stopped working" (492 reviews), poor quality and not worth the price (282), slow performance (262), battery drain (260), damaged packaging (256), unhelpful customer support (216).
- **Product comparison:** HP Laptop had the highest negative share (25.1%) and Sony Headphones the lowest (19.5%), a small gap given the synthetic data.
- **Over time:** monthly negative share ranged from 18.4% (May 2025) to 24.9% (Aug 2025) with no clear trend.
- **Model confidence:** average confidence was 90.8% for positive, 82.4% for negative and only 61.5% for neutral reviews, so neutral is the hardest class.
## Screenshots
| Streamlit app | Power BI dashboard |
|---|---|
| <img src="https://github.com/user-attachments/assets/53f9b663-028c-4a36-bae4-8da454c35e27" alt="Streamlit app" width="450"> | <img src="https://github.com/user-attachments/assets/0d63ee8a-339b-4aee-bdfc-36fca0c3db6c" alt="Power BI dashboard" width="450"> |
## Tech stack
Python, Pandas, NLTK, TextBlob, Matplotlib, Plotly, WordCloud, Streamlit, Power BI, Excel (openpyxl)

## How to run locally
```bash
git clone https://github.com/sandeepgill595-hub/my_sentiment_project.git
cd my_sentiment_project
pip install -r requirements.txt
python sentiment_analysis.py
streamlit run app.py
```
Open `Sentiment Analysis.pbix` in Power BI Desktop (free) to view the dashboard.

- The dataset is synthetic with 30 unique review sentences, so results show the pipeline, not real customer behavior.
- Sentiment closely tracks star rating in this data.
- Next step: rerun the pipeline on a real public review dataset (for example, Amazon product reviews on Kaggle).
  
## Author
Sandeep Singh Gill | [LinkedIn](https://linkedin.com/in/sandeep-gill-99b147278) | [GitHub](https://github.com/sandeepgill595-hub)
