# Customer Review Sentiment Analysis

An end-to-end sentiment analysis project: Python scores customer reviews as Positive, Negative or Neutral, a Streamlit app lets you explore the results, and a Power BI dashboard summarizes them.

**Live demo:** [https://mysentimentproject-cqwimqdgu84xhgumzmp44e.streamlit.app/]

![App overview](images/app_overview.png)

## Business problem
Support and product teams receive large volumes of free-text reviews and cannot read them all. This project turns raw reviews into sentiment counts, trends and common words so a team can see what customers are happy or unhappy about.

## Data
- `reviews.xlsx`: input reviews.
- `results.xlsx`: reviews with the sentiment label and score added by the analysis script.
- No real customer data is used.

## What it does
1. `generate_reviews.py` creates the sample review dataset. **[CONFIRM]**
2. `app.py` is a Streamlit app that shows sentiment distribution, word clouds and filters.
3. `Sentiment Analysis.pbix` is a Power BI report built on `results.xlsx`.

## Key findings
- **[ADD 2-3 real findings, e.g. "X% of reviews were positive; the most common words in negative reviews were ..."]**

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

## Limitations and next steps
- Rule-based sentiment can miss sarcasm and mixed opinions.
- Next: compare against a trained model such as scikit-learn logistic regression and report accuracy.

## Author
Sandeep Singh Gill | [LinkedIn](https://linkedin.com/in/sandeep-gill-99b147278) | [GitHub](https://github.com/sandeepgill595-hub)
