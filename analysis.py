# -*- coding: utf-8 -*-
# Third-party app imports
import pandas as pd


def get_top_twitter_posts(tweets):
    twitterIdToTweet = {}

    data = {
        'id': [],
        'retweets': [],
        'likes': [],
        'username': []
    }

    for tweet in tweets:
        twitterIdToTweet[tweet['TweetIdStr']] = tweet
        data['id'].append(tweet['TweetIdStr'])
        data['retweets'].append(tweet['TwitterRetweets'])
        data['likes'].append(tweet['TwitterLikes'])
        data['username'].append(tweet['Username'])

    twitter_data = pd.DataFrame(
        data, columns=['id', 'retweets', 'likes', 'username'])
    best_tweets = twitter_data.sort_values(
        ['retweets', 'likes'], ascending=[0, 0])

    diverse_tweets = best_tweets.drop_duplicates('username')

    # Don't run into bugs
    max_tweets = 6
    if len(diverse_tweets) < 6:
        max_tweets = len(diverse_tweets)

    top_tweets = []
    for index, row in diverse_tweets[:max_tweets].iterrows():
        top_tweets.append(twitterIdToTweet[row['id']])

    return top_tweets


def get_top_instagram_posts(instagram_posts):
    instagramIdToInstagramPosts = {}

    data = {
        'id': [],
        'comments': [],
        'likes': [],
        'username': []
    }

    for instagram_post in instagram_posts:
        instagramIdToInstagramPosts[
            instagram_post['InstagramId']] = instagram_post
        data['id'].append(instagram_post['InstagramId'])
        data['comments'].append(instagram_post['InstagramComments'])
        data['likes'].append(instagram_post['InstagramLikes'])
        data['username'].append(instagram_post['InstagramUsername'])

    instagram_data = pd.DataFrame(
        data, columns=['id', 'comments', 'likes', 'username'])
    best_instagram_posts = instagram_data.sort_values(
        ['comments', 'likes'], ascending=[0, 0])

    diverse_instagram_posts = best_instagram_posts.drop_duplicates('username')

    '''
    Cases:
        1. The diverse produces 1/2 results. Then we should fill it in with
        instagram posts from the same person.
    '''

    # Don't run into bugs
    max_instagram_posts = 6
    if len(diverse_instagram_posts) < 6:
        max_instagram_posts = len(diverse_instagram_posts)

    top_instagram_posts = []
    for index, row in diverse_instagram_posts[:max_instagram_posts].iterrows():
        top_instagram_posts.append(instagramIdToInstagramPosts[row['id']])

    return top_instagram_posts


def get_top_headlines(headlines):
    max_headlines = 6
    if len(headlines) < 6:
        max_headlines = len(headlines)

    return headlines[:max_headlines]


def find_best_posts(social_posts):
    # We want a mixture of Twitter, Instagram, and RSS feed.
    # We want the posts with the highest likes, comments, etc.
    tweets = []
    headlines = []
    instagram_posts = []
    for social_post in social_posts:
        if social_post['_source']['data']['Type'] == 'Tweet':
            tweets.append(social_post['_source']['data'])
        elif social_post['_source']['data']['Type'] == 'Headline':
            headlines.append(social_post['_source']['data'])
        elif social_post['_source']['data']['Type'] == 'Instagram':
            instagram_posts.append(social_post['_source']['data'])

    top_tweets = []
    top_instagram_posts = []
    top_headlines = []

    if len(tweets) > 0:
        top_tweets = get_top_twitter_posts(tweets)

    if len(instagram_posts) > 0:
        top_instagram_posts = get_top_instagram_posts(instagram_posts)

    if len(headlines) > 0:
        top_headlines = get_top_headlines(headlines)

    return (top_tweets, top_instagram_posts, top_headlines, (len(instagram_posts), len(tweets), len(headlines)))


def find_best_email(emails):
    if 'hits' in emails and 'hits' in emails['hits']:
        number_of_emails = emails['hits']['total']
        emailIdToEmail = {}

        data = {
            'id': [],
            'opens': [],
            'clicks': [],
            'email': []
        }

        for email in emails['hits']['hits']:
            single_email = email['_source']['data']

            emailIdToEmail[single_email['Id']] = single_email
            data['id'].append(single_email['Id'])
            data['opens'].append(single_email['Opened'])
            data['clicks'].append(single_email['Clicked'])
            data['email'].append(single_email['To'])

        email_data = pd.DataFrame(
            data, columns=['id', 'opens', 'clicks', 'email'])
        best_emails = email_data.sort_values(['clicks', 'opens'], ascending=[0, 0])
        diverse_emails = best_emails.drop_duplicates('email')

        max_emails = 6
        if len(diverse_emails) < 6:
            max_emails = len(diverse_emails)

        top_emails = []
        scheduled_emails = []

        print diverse_emails

        for index, row in diverse_emails[:max_emails].iterrows():
            top_emails.append(emailIdToEmail[row['id']])

        return top_emails
