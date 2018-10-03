import pymongo
import pprint
from pymongo import MongoClient
data = open('key.txt', mode='r').read()
print(data)
rows = data.split("\n")
print(rows)
APP_KEY = rows[0]
APP_SECRET = rows[1]
Access_Token = rows[2]
Access_Token_Secret = rows[3]
password = rows[4]
client = pymongo.MongoClient("mongodb+srv://Hong:%s@utecho-hbnie.mongodb.net/test?retryWrites=true" % password)

db = client.video
collection_movie = db.movieDetails

testpost = {'actors': 'Xie Hong',
            'countries': 'China',
            'director':'Xie Hong',
            'genres':['Drama','Romance'],
            'title':'Cute ESP',
            'metacritic':'100',
            'type':'movie',
            'year':'2018'
            }

collection_movie.insert_one(testpost)


pprint.pprint(collection_movie.find_one({'title': 'Cute ESP'}))

#{"year":"1961"}



