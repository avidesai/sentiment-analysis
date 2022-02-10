"""
Sentiment Analysis:
Computationally identifying and categorizing opinions expressed in a piece of text.
This is done to determine whether the author's attitude towards a particular subject is positive, negative, or neutral.

Text is inputted from a website to determine the author's sentiment.

Disclaimer: the accuracy of model's sentiment predictions are not guaranteed by any means.
"""
from typing import Text
from textblob import TextBlob
import nltk
from newspaper import Article

url = "https://investor.fb.com/investor-news/press-release-details/2021/Facebook-Reports-Third-Quarter-2021-Results/default.aspx"
url2 = "https://investors.twilio.com/news/news-details/2022/Twilio-Announces-Fourth-Quarter-and-Full-Year-2021-Results/"
url3 = "https://news.yahoo.com/killer-whales-coming-seafood-supply-220000310.html"

# Input your own articles to determine their sentiment
article = Article(url3)
article.download()
article.parse()
nltk.download('punkt')
article.nlp()

# Get summary of the article
summary = article.summary
print(summary)
print('\n')

# Get sentiment of data
obj = TextBlob(summary)
# negative sentiment = bad, positive sentiment = good, zero sentiment = neutral
sentiment = obj.sentiment.polarity

if (sentiment > 0):
    print('Sentiment is Good.')
elif (sentiment < 0):
    print('Sentiment is Bad.')
else:
    print('Sentiment is Neutral.')