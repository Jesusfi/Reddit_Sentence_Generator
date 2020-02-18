from sentencegenerator import SentenceGenerator 
import praw
import pandas as pd 
import random
import os
import config

reddit = praw.Reddit(client_id=config.client_id, \
                    client_secret=config.client_secret, \
                    user_agent=config.user_agent, \
                    username=config.username, \
                    password=config.password)

subreddit_name = input("Enter subreddit name: ")

#Get specific subreddit 
subreddit = reddit.subreddit(subreddit_name)

original_posts = []
post_limit = 100

print ("Gathering top",post_limit, subreddit_name, "Hot posts") 
for submission in subreddit.hot(limit = post_limit):
    original_posts.append(submission.title)
    original_posts.append(submission.selftext)

print ("Gathering top",post_limit,subreddit_name,"Top posts")
for submission in subreddit.top(limit = post_limit): 
    original_posts.append(submission.title)
    original_posts.append(submission.selftext)

print ("Filtering empty strings")
original_posts = list(filter(None, original_posts))

print ("Filtering duplicate strings")
original_posts = list(set(original_posts))

print ("Spliting to individual words") 
power = 1
generator = SentenceGenerator(original_posts, power)

print ("Generationg sentance\n")
for i in range(6):
    sentence = generator.generate_sentence(sentence_length = 30)
    print (sentence)

print("\nGenerating sentance power 2\n")
power = 2 
generator_two_words = SentenceGenerator(sentence_list = original_posts, power = power)
for i in range(6):
    sentence = generator_two_words.generate_sentence(sentence_length = 30)
    print (sentence)
