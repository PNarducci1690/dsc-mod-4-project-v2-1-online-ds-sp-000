import pandas as pd
import re
import string
import html

replacers = {'mt':'modified tweet', 
          'hrs':'hours',
          'fri': 'friday',
          'dm':'direct message',
          'prt':'partial tweet',
          'ht':'hat tip',
          'cc':'carbon copy',
          'imho':'in my humble opinion',
          'ayfkmwts': 'are you fucking kidding me with this shit',
          'gtfooh':'get the fuck out of here',
          'oh':'overheard',
          'rlrt':'real life retweet',
          'gmafb':'give me a fucking break',
          'nbd':'no big deal',
          'smh':'shaking my head',
          'idk': 'i do not know',
          'stfu': 'shut the fuck up',
          'nfw': 'no fucking way',
          'irl':'in real life',
          'nsfw':'not safe for work',
          'sfw':'safe for work',
          'fml':'fuck my life',
          'fwiw':'for what it is worth',
          'qotd':'quote of the day',
          'lmao':'laughing my ass off',
          'hotd':'headline of the day',
          'ftw':'for the win',
          'btw':'by the way',
          'bfn':'bye for now',
          'afaik':'as far as i know',
          'lol':'laugh out loud',
          'ty':'thank you',
          'yw':'youre welcome',
          "isn't" : 'is not',
          "aren't" : 'are not',
          "wasn't" : "was not", 
          "weren't" : "were not",
          "haven't" : "have not",
          "hasn't" : "has not",
          "hadn't" : "had not",
          "won't" : "will not",
          "wouldn't" : "would not", 
          "don't" : "do not", 
          "doesn't" : "does not",
          "didn't" : "did not",
          "can't" : "can not",
          "couldn't" : "could not",
          "shouldn't" : "should not",
          "mightn't" : "might not",
          "mustn't" : "must not",
          "they're" : "they are",
          '�' : '',
          'ϡ' : '',
          'ʋ' : '',
          'ҋ' : '',
          '⋁' : '',
          '΋' : '',
          '۝' : '',
          }


def tweet_text_cleaner(tweet):
    tweet = html.unescape(tweet) #unescapes html code
    tweet = tweet.replace(u'\ufffd', '?') #removes unicode
    tweet = tweet.lower() #make string values lowercase
    tweet = re.sub('\d[a-z0-9]+', '', tweet) #remove numeric values and accompanying text
    tweet = re.sub('\d+', '', tweet) #remove remaining numeric text
    tweet = re.sub('@[a-z0–9]+', '', tweet) # remove @ and accompying text
    tweet = re.sub('#[a-z0–9]+', '', tweet) # Remove # and accompying text
    tweet = re.sub('rt[\s]+', '', tweet) # Removes rt
    tweet = re.sub('https?://[A-Za-z0-9./]+', '', tweet) # removes hyperlinks
    tweet = re.sub('https?://[A-Za-z0-9./]+', '', tweet) # removes hyperlinks
    tweet = re.sub('\{[a-z0–9]+}', '', tweet) #will remove {} and ac
    for key in replacers.keys():
        tweet = tweet.replace(key, replacers[key])
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    tweet = re.sub('\s+', ' ', tweet)

    
    
    return tweet
    
    

    
    