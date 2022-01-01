#!/usr/bin/python

from googleapiclient.discovery import build
import time

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
YOUTUBE_API_KEY = "AIzaSyD95ECCJL1f8SMkRzc32AmavdN2Rrl1-ek"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

search_response = youtube.search().list(
    part='snippet',
    # 検索したい文字列
    # 検索条件(今回は視聴回数が多い順に取得)
    # order='viewCount',
    # 検索対象(今回は動画に絞る)
    type='video',
    publishedAfter='2021-01-01T00:00:00+09:00',
    publishedBefore='2021-02-01T00:00:00+09:00',
    regionCode='JP',
    videoLicense='creativeCommon',
).execute()

videos = []
channels = []
playlists = []

# Add each result to the appropriate list, and then display the lists of
# matching videos, channels, and playlists.
for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
        videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
        channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                     search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
        playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                      search_result["id"]["playlistId"]))

print(search_response)
print("Videos:\n", "\n".join(videos), "\n")

pageToken = search_response.get("nextPageToken", [])

while len(pageToken) != 0:
    print(pageToken)
    # time.sleep(1)
    search_response = youtube.search().list(
        part='snippet',
        # 検索したい文字列
        # 検索条件(今回は視聴回数が多い順に取得)
        # 検索対象(今回は動画に絞る)
        type='video',
        # maxResults=50,
        pageToken=pageToken,
        publishedAfter='2021-01-01T00:00:00+09:00',
        publishedBefore='2021-02-01T00:00:00+09:00',
        regionCode='JP',
        videoLicense='creativeCommon',
    ).execute()
    pageToken = search_response.get("nextPageToken", [])
    print(search_response)

print('END')
