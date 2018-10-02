from twython import Twython

f = open('datalocal.txt', 'w+')
# help(Twython)
data = open('key.txt', mode='r').read()
print(data)
rows = data.split("\n")
print(rows)
APP_KEY = rows[0]
APP_SECRET = rows[1]
Access_Token = rows[2]
Access_Token_Secret = rows[3]


twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)


results = twitter.cursor(twitter.search, q='台風',result_type='Popular')
for result in results:
    if result['retweeted'] == False:
    #print(result['id'])
        f.write(str(result['id']))
        f.write(' ')
        f.write(str(result['id_str']))
        f.write(' ')
        f.write(str(result['truncated']))
        f.write(' ')
        f.write(str(result['retweet_count']))
        f.write(' ')
        f.write(str(result['text']))
        f.write('\n')
        #f.write(result['usr'])

f.close()