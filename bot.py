#!/usr/bin/env python3

import twitter
import settings

if __name__ == '__main__':

    api = twitter.Api(consumer_key=settings.consumer_key,
                      consumer_secret=settings.consumer_secret,
                      access_token_key=settings.access_token_key,
                      access_token_secret=settings.access_token_secret)

    api.VerifyCredentials()

"""
results = api.GetSearch(raw_query='q=%23billard&src=typeahead_click')

for tweet in results:
    try:
        api.CreateFavorite(tweet)
    except twitter.error.TwitterError:
        print("Fav failed")
    # api.PostRetweet(tweet)
"""
