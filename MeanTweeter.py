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

        self.updateNo = 1

    def getApi(self):
        if self.api == None:
            self.api = twitter.Api(consumer_key=self.secrets['consumer_key'],
                consumer_secret=self.secrets['consumer_secret'],
                access_token_key=self.secrets['access_token_key'],
                access_token_secret=self.secrets['access_token_secret'])
        
        return self.api

    def post(self):
        phrasefile = json.load(open(self.phrasesLoc))
        phrases = phrasefile['phrases']

        phraseid = random.randint(0,len(phrases) - 1)
        phrase = phrases[phraseid]
        
        phrase = "Update No. " + self.updateNo + ".\n" + phrase
        self.updateNo++

        try:
            self.getApi().PostUpdate(status=phrase)
        except:
            pass

    def run(self):
        while True:
            self.post()
            time.sleep(300)

MeanTweeter("people.json", "phrases.json", "secrets.json").run()