import praw
import pandas as pd
import datetime as dt
from IPython import display
from pprint import pprint
import numpy as np
import nltk
nltk.downloader.download('vader_lexicon')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='darkgrid', context='talk', palette='Dark2')
import string
from string import digits
import re


reddit = praw.Reddit(client_id='73IApaJarJRRVA',client_secret='QIET4TRTvxlLWDNFfobmDD7oAfM',user_agent='PD sentiment',username='hll4ce',password='Snsh11nE')


headlines = set()

for submission in reddit.subreddit('Parkinsons').new(limit=None):
    headlines.add(submission.selftext)
    display.clear_output()
    print(len(headlines))



#can just import the dataset here instead of creating it


x = list(headlines)

#remove punctuation
for index,item in enumerate(x):
	x[index] = re.sub(r'[^\w\s]',' ',item)

#remove newline
for index,item in enumerate(x):
	x[index] = re.sub(r'\n',' ',item)

#remove any too short
x.append("b")
for n, i in enumerate(x):
	if len(i) < 10:
		x[n] = ""

#remove numbers  
def remove(list): 
    
    list = [re.sub(pattern, '', i) for i in list] 
    return list

pattern = '[0-9]'
for index,item in enumerate(x):
	x[index] = re.sub(pattern,'',item)


#remove stop words
#stop word list:



#remove any empty




#Hutto and Gilbert (2015) VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []


for line in headlines:
    pol_score = sia.polarity_scores(line)
    pol_score['headline'] = line
    results.append(pol_score)

pprint(results[:3], width=100)

df = pd.DataFrame.from_records(results)
df.head()
#`compound` ranges from -1 (Extremely Negative) to 1 (Extremely Positive).

#positive label if compound greater than 0.2, negative if under -0.2
df['label'] = 0
df.loc[df['compound'] > 0.2, 'label'] = 1
df.loc[df['compound'] < -0.2, 'label'] = -1
df.head()


