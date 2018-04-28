import twitter
import json
import random

phrasefile = json.load(open('phrases.json'))
phrases = phrasefile['phrases']

peoplefile = json.load(open('people.json'))
people = peoplefile['people']

secrets = json.load(open('secrets.json'))
api = twitter.Api(consumer_key=secrets['consumer_key'],
                  consumer_secret=secrets['consumer_secret'],
                  access_token_key=secrets['access_token_key'],
                  access_token_secret=secrets['access_token_secret'])

for person in people:
    query = "q=from%3A" + person
    results = api.GetSearch(
        raw_query=query)

    latest = results[0]

    phraseid = random.randint(0,len(phrases) - 1)
    phrase = phrases[phraseid]

    api.PostUpdate(status=phrase,
        in_reply_to_status_id=latest.id,
        auto_populate_reply_metadata=True)

    print("done!")