import json
import random
import twitter
import time

class MeanTweeter:
    def __init__(self, peopleLoc, phrasesLoc, secretsLoc):
        self.peopleLoc = peopleLoc
        self.phrasesLoc = phrasesLoc

        self.secrets = json.load(open('secrets.json'))
        
        self.replied = list()
        self.api = None

    def getApi(self):
        if self.api == None:
            self.api = twitter.Api(consumer_key=self.secrets['consumer_key'],
                consumer_secret=self.secrets['consumer_secret'],
                access_token_key=self.secrets['access_token_key'],
                access_token_secret=self.secrets['access_token_secret'])
        
        return self.api

    def reply(self, statusID):
        phrasefile = json.load(open(self.phrasesLoc))
        phrases = phrasefile['phrases']

        phraseid = random.randint(0,len(phrases) - 1)
        phrase = phrases[phraseid]

        self.getApi().PostUpdate(status=phrase,
            in_reply_to_status_id=statusID,
            auto_populate_reply_metadata=True)

    def go(self):
        peoplefile = json.load(open(self.peopleLoc))
        people = peoplefile['people']

        for person in people:
            query = "q=from%3A" + person
            results = self.getApi().GetSearch(
                raw_query=query)

            if len(results) > 0:
                latest = results[0]

                if latest.id not in self.replied:
                    self.reply(latest.id)
                    self.replied.append(latest.id)

    def run(self):
        while True:
            self.go()
            time.sleep(30)

MeanTweeter("people.json", "phrases.json", "secrets.json").run()