from pytrends.request import TrendReq

# API Connection
pytrends = TrendReq(hl='ja-JP', tz=360)
# Set the search keyword
kw_list = ["Python"]
pytrends.build_payload(kw_list, timeframe='2014-01-01 2018-09-30', geo='JP')
df = pytrends.interest_over_time()
df.plot(figsize=(15, 3), lw=.7)
print(pytrends)
