import pymongo
import pprint
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://Hong:wsadwsad@utecho-hbnie.mongodb.net/test?retryWrites=true")

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



