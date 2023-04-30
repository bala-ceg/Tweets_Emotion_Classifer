import streamlit as st
import tweepy
import re
import mindsdb_sdk as mdb
import pandas as pd
import os


consumer_key = os.environ['consumer_key']
consumer_secret = os.environ['consumer_secret']
access_token = os.environ['access_token']
access_secret = os.environ['access_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

MDB_EMAIL=os.environ['email']
MDB_PWD=os.environ['pwd']
MODEL_NAME=os.environ['model']

# Define function to predict emotions
def predict_from_mindsdb(df: pd.DataFrame):
    server=mdb.connect(login=MDB_EMAIL,password=MDB_PWD)
    model=server.get_project('mindsdb').get_model(MODEL_NAME)
    pred_df = pd.DataFrame(columns=['text'])
    pred_df['text'] = df['text']
    try: 
        ret_df = model.predict(pred_df)
    except Exception as e:
        print('Not able to generate predictions at the moment')
    return ret_df

# Define Streamlit app
st.title('Twitter Emotion Predictor - Powered by MindsDB')
st.write('Enter a Twitter username and click the button to predict the emotions of the user\'s the latest 10 tweets')

# Get input username from user
username = st.text_input('Enter a Twitter username')

# Fetch user's tweets and predict emotions
if st.button('Predict emotions'):
    try:
        tweets = api.user_timeline(screen_name=username, count=10, tweet_mode='extended')
        df = pd.DataFrame({
                'tweet_id': [tweet.id for tweet in tweets],
                'created_at': [tweet.created_at for tweet in tweets],
                'text': [tweet.full_text for tweet in tweets],
                'retweet_count': [tweet.retweet_count for tweet in tweets],
                'favorite_count': [tweet.favorite_count for tweet in tweets],
                'lang': [tweet.lang for tweet in tweets],
                'source': [tweet.source for tweet in tweets]
            })
        st.write(f'Predicting emotions for the latest {len(tweets)} tweets from @{username}...')
        df2 = predict_from_mindsdb(df)
        df = pd.concat([df, df2], axis=1)
        df = df.rename(columns={'text': 'tweet','sentiment': 'tweet_sentiment'}) 
        df = df[['tweet', 'tweet_sentiment']]
        st.dataframe(df) 
    except Exception as e:
        st.error(f'Error fetching tweets: {e}, perhaps a wrong user name')
    
