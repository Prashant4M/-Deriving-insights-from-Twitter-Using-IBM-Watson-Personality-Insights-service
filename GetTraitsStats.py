#Import required libraries
import numpy as np
from ibm_watson import PersonalityInsightsV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pandas as pd
from ibm_watson import ApiException
import GetOldTweets3 as got
import json
import re

authenticator = IAMAuthenticator("your_api_key")
personality_insights = PersonalityInsightsV3(
    version='2020-01-30',
    authenticator=authenticator
)

personality_insights.set_service_url('url')

def convert_tweet_to_feedable_form(s):
    #Return the converted array
    return {
        'id': str(s.id),
        'contenttype': 'text/plain',
        'language': 'en',
        'content': " ".join(re.sub("([@#][A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",s.text).split()),
        'reply': (s.to is not None),
        'forward': False
    }


#Read the CSV file containing the Image_Link,Name,Twitter Handle of the Actor
twitter_handles = pd.read_csv('Final_Celebrities_Data.csv')
name = list(twitter_handles['Actor Name'])
twitter_handle = list(twitter_handles['Twitter Handle'])
image_Link = list(twitter_handles['Image_Link'])

#Getting the tweets of the user
for i in range(len(name)):
    tweetCriteria = got.manager.TweetCriteria().setUsername(twitter_handle[i]).setLang("en").setEmoji("unicode").setSince("2019-05-01").setUntil("2020-01-31")
    print("Getting Tweets....")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    pi_content_items_array = list(map(convert_tweet_to_feedable_form, tweets))
    pi_content_items = {'contentItems': pi_content_items_array}
    
    if pi_content_items['contentItems'] != []: 
        print("Predicting Traits.....")
        profile = personality_insights.profile(
            pi_content_items,
            'application/json',
            content_type='application/json',
            consumption_preferences=False,
            raw_scores=True
        ).get_result()
        print("Saving Results.....")
        profile['Actor Name'] = name[i]
        profile['Image Link'] = image_Link[i]
        out_file = open(r"Your_Path\Traits_Data\{}.json".format(name[i]+"_Personality_Traits"), "w") 
        json.dump(profile, out_file, indent = 6)
        print("Result Saved[{}+1]".format(i))
        out_file.close()
    else:
        print("No Tweets for the user!!!!")
