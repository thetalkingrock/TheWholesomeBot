#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy
import praw
import time
import datetime

#access tweepy
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#access praw
t = praw.Reddit(client_id='',
                     client_secret='',
                     password='',
                     user_agent='',
                     username='')

while True:
	#search for tweets from people having a bad day
	result_tweets = api.search(q="I'm really sad right now", count=20)
	#tweet out response to matching tweets
	for tweet in result_tweets:
		#check that each tweet was sent in the last 24 hours
		if (datetime.datetime.now() - tweet.created_at).days < 1:
            		print(tweet.text)
            		user_name = tweet.user.screen_name
			message = '@' + user_name + ' I hope things get better for you. '
            		message += 'Looking at these always makes me happy. :) '
