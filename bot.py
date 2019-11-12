#!/usr/bin/env python3

import twitter
import settings


def rt_tweet(api, tweet):
    try:
        api.PostRetweet(tweet.id)
        print(f'[SUCCESS]: Retweeted - {tweet.text}')
    except twitter.error.TwitterError:
        print(f'[ERROR]: Could not retweet tweet - {tweet.id_str}')


def like_tweet(api, tweet):
    try:
        api.CreateFavorite(tweet)
        print(f'[SUCCESS]: Favorited - {tweet.text}')
    except twitter.error.TwitterError:
        print(f'[ERROR]: Could not favorite tweet - {tweet.id_str}')


if __name__ == '__main__':

    api = twitter.Api(consumer_key=settings.consumer_key,
                      consumer_secret=settings.consumer_secret,
                      access_token_key=settings.access_token_key,
                      access_token_secret=settings.access_token_secret)

    api.VerifyCredentials()

    results = api.GetSearch(raw_query='q=%23billard&src=typeahead_click')

    for tweet in results:
        like_tweet(api, tweet)
        rt_tweet(api, tweet)
