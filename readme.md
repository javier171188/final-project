# Final Project
## Overvew

Nowadays there are plenty information media, so keeping track of every one of the news has become in an impossible task. An even harder and related problem is that media sometimes present a bias, which make hard to trust the articles we find online.

This project presents the firs step to solve the previously mentioned problems. This repository only contains the recollection and analysis of the news. For the development of the graphic interface please check [here](http://romantic-lamport-229bd1.netlify.com).

## Steps

* We scrap the rss of the following media: CNN, The Wall Street Journal, BBC, USA Today and the New York Times. 

* We make a sentiment analysis for all of the scraped articles. For this step we use the SentimentIntensityAnalyzer from nltk.

* We clusterize the news. To vectorize the text we use TfidfVectorizer, then we cluster by the HDNSCAN algorithm and the cosine similarity to get a distance.

* The next step is to summarize the clusters. For this task we used the algorithm presented [here](https://stackabuse.com/text-summarization-with-nltk-in-python/).

* Finally we upload the data to a mongo database to feed the app.

## Future Improvements

Since this project only represents a first step, we are planning to make several improvements, for example:

* Refine the clustering system.
* Change the summary algorithm.
* Add a recommendation system.
* Track the most important news through time.

