# Tweets_Emotion_Classifer

![P3_Hashnode](https://user-images.githubusercontent.com/70808619/235376794-c947ebd6-795b-4b0c-af3a-8aa08ca76a71.png)



This is  Streamlit app powered by MindsDB that allows you to enter a Twitter username and predicts the emotions (positive, negative, or neutral) for the last 10 tweets from that user.

## How to use

To use the app, you'll need to have a Twitter API key and access token, which you can get by [creating a Twitter Developer account](https://developer.twitter.com/en/docs/getting-started/getting-access-to-the-twitter-api). Once you have your keys and tokens, you can add them by creating a new file `config.py`  in this repository.

Then, you can run the app locally by installing the required packages (listed in `requirements.txt`) and running `streamlit run file_name.py` from the command line.

When the app loads, enter a Twitter username and click the "Predict emotions" button. The app will fetch the last 10 tweets from that user and predict whether each tweet has a positive, negative, or neutral emotion. The results will be displayed in a table that shows the full text of each tweet and its predicted emotion.

## Acknowledgements

This app was created using the [Tweepy](https://www.tweepy.org/) library for accessing the Twitter API and [MindsDB_SDK](https://docs.mindsdb.com/what-is-mindsdb) for predicting emotions in the tweets. The app was built using [Streamlit](https://www.streamlit.io/), a Python library for building data apps.
