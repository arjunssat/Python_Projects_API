from googleapiclient.discovery import build
import json
import time

YOUTUBE_API_SERVICE_NAME='youtube'
YOUTUBE_API_VERSION='v3'
key = 'Api'

youtube=build(developerKey=key,serviceName=YOUTUBE_API_SERVICE_NAME,version=YOUTUBE_API_VERSION)

search_keyword=youtube.search().list(q='data science',part='snippet',maxResults=100).execute()

data=[(i['snippet']['title'],i['snippet']['description'])for i in search_keyword['items']]
page_token=search_keyword['nextPageToken']

for i in range(10):
    time.sleep(2)
    search_keyword=youtube.search().list(q='india',part='snippet',maxResults=100,pageToken=page_token).execute()

    data.extend([(i['snippet']['title'],i['snippet']['description']) for i in search_keyword['items']])
    page_token=search_keyword['nextPageToken']

with open('data.json','w',encoding='utf8')as outfile:
    json.dump(data,outfile,ensure_ascii=False,indent=2)