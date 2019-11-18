#!/usr/bin/env python3

import twitter
import settings

import urllib


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


def remove_when_user_contains(filter, tweets):
    """
    Returns: a list of tweets not containing filter
    filter: The substring to look for
    tweets: The array of tweets to go over
    """
    remaining = []

    for tweet in tweets:
        if (tweet.user.screen_name.lower().count(filter) == 0):
            remaining.append(tweet)

    return remaining


def user_list_contain(filter, users) -> bool:
    """
    Returns: True if a user contains the specified filter, False otherwise
    filter: The substring to look for
    users: The array of users to go over
    """
    for user in users:
        if (user.screen_name.lower().count(filter) > 0):
            return True
    return False


def remove_when_user_mentions_contains(filter, tweets):
    """
    Returns: The list of tweets whose user mentions do not contain the specified filter
    filter: The substring to look for
    tweets: The tweets to go over
    """
    remaining = []

    for tweet in tweets:
        if (not user_list_contain(filter, tweet.user_mentions)):
            remaining.append(tweet)

    return remaining


def remove_when_tweet_contains(filter, tweets):
    """
    Returns: The list of tweets not containing the given filter
    filter: The substring to look for
    tweets: The list of tweets to go over
    """
    remaining = []

    for tweet in tweets:
        if (tweet.text.lower().count(filter) == 0):
            remaining.append(tweet)

    return remaining


if __name__ == '__main__':

    api = twitter.Api(consumer_key=settings.consumer_key,
                      consumer_secret=settings.consumer_secret,
                      access_token_key=settings.access_token_key,
                      access_token_secret=settings.access_token_secret)

    api.VerifyCredentials()

    parameters = {'q': 'billard'}

    parameters = urllib.parse.urlencode(parameters)

    results = api.GetSearch(raw_query=f'{parameters}&src=typeahead_click')

    results = remove_when_user_contains('billard', results)
    results = remove_when_user_mentions_contains('billard', results)

    results = remove_when_tweet_contains('sur le billard', results)

    for tweet in results:
        like_tweet(api, tweet)
        rt_tweet(api, tweet)
