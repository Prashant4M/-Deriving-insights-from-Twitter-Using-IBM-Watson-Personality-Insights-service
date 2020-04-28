# Deriving insights from Twitter Using IBM Watson Personality Insightsservice
I was inspired to do this kind of project because writing(the mind thoughts) tells you the different personality traits about a person. To build a such type of system I suppose to use twitter(www.twitter.com) to get the tweets data of any person.
# Approach
* Getting the twitter account details
* Geting tweets of any particular user
* Preprocessing and cleaning the tweets
* Using Personality Insights instance
* Save the respose as a csv or json file

# Getting the twitter account details
The list of Twitter-active
Indian celebrities and their Twitter handles was gathered
using statistics available in social media analytics website
[Socialbakers](www.socialbakers.com).
# Geting tweets of any particular user
For retrieving the tweets I used:
- [GetOldTweets](https://pypi.org/project/GetOldTweets3/) : A Python 3 library and a corresponding command line utility for accessing old tweets.
# Preprocessing and cleaning the tweets
The collected tweets cannot directly be used for personality
determination for several reasons.
- Some of the tweets may be retweets. The retweets are
not written originally by the user but are written by
some other user and are being shared by the target user.
As retweet texts are not original texts of the target user,
retweets are not usable for personality determination.
- The tweets may contain non-language texts such as
hashtags, hyperlinks, smiley, and other emojis. These
non-language texts should be omitted before a tweet
can be used by the personality tools.
- The Twitter posts may be written in a language other
than English, even though they are written in English
script. Currently, the personality tool (Watson) works
only on English-language texts. So we identify non-
English posts and omit such posts from further analysis.
- The raw tweets include some information (such
as retweets, retweet count, location, and contributors) that
cannot be used as user text for personality trait generation.
Moreover, we retained only posts and replies made by the
celebrities in the last 7 months for further processing.
* The output of the above
may contain hashtags, Twitter handles,
hyperlinks, and emoticons. To identify the relevant information
(i.e., meaningful English words), only texts consisting
of English language were kept for further
processing. Hyperlinks in tweets were also identified and
deleted.
- For detailed approach you can refer to [Analyzing Big-Five Personality Traits of Indian Celebrities Using
Online Social Media](https://link.springer.com/article/10.1007/s12646-017-0408-8?shared-article-renderer)
# Using Personality Insights instance
for the use of PI service you can refer to the [Official API Docs Page](https://cloud.ibm.com/apidocs/personality-insights?code=python)
# Save the respose as a csv or json file
Refer to [this page](https://cloud.ibm.com/docs/services/personality-insights?topic=personality-insights-output)
