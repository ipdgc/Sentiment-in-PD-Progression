# Sentiment Analysis in Parkinson's Disease

## Motivation
Blogs, social media, news outlets, online patient forums, and other sources of online media have rapidly increased the sharing of disease experience. Parkinson's disease is no different; large communities of both patients and caregivers have found homes on the internet, sharing symptoms, drug responses, and general day to day life. Obtaining and processing this large amount of textual data can provide unique insights into the patient experience. 

## General Information 
- Contributors:
    - Hampton Leonard, NIA, NIH
    - Manuela Tan
    - Prabhjyot Saini
    - Van Truong, NCI, NIH & Johns Hopkins University
    - Irem Sarihan, Cleveland Clinic
    - Fanny Casse

### Goals
- Sentiment of PD on social media
  - Building off of what was done with reddit last year
- Drug review data
  - Sentiment of PD drugs, are there patterns or outliers
- Look at sentiment in headlines/articles relating to Parkinson’s, 
  - e.g. new treatments, and whether there is much continuity in these
  - dashboard to display current sentiments around new treatments/news of PD
  
  
 ### Roles
 
- Updating and building off of Reddit
  - Hampton
  - Manuela
- Drug review data
  - Fanny
  - Irem
- Sentiment in headlines/articles
  - Van
  - Prabhjyot
  
### Deliverables

- Pipeline for text processing
- Dashboard
 
 
## Text Processing Pipeline

- takes an input of a dataframe with a column of text to be processed
- outputs frequency counts of words, trigrams, td idf matrix
- option of sentiment analysis?
 
## Parkinson's Disease Sentiment in Social Media

### Reddit

- (make this part better)
- scraped pd subreddit for everything after 01-01-2012 to now
- 3033 posts
- 14817 comments

- filter raw dataframe based on a number of things, drugs, clinical trials, etc
- run through pipeline
- sentiment analysis and compare



#### What do people talk about on the Parkinson's Disease subreddit?

![](/images/reddit_wordcloud.png)




[Dashboard](https://datastudio.google.com/s/s6xxbbc4qOw) for viewing different metrics taken from analyzed media text data

![](/images/dashboard.png)



