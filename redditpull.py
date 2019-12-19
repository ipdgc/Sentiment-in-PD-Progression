from psaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()

start_epoch=int(dt.datetime(2017, 1, 1).timestamp())

print(list(api.search_submissions(after=start_epoch,
                            subreddit='politics',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=10)))