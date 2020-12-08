import time 
from twitter import Api
import json 
def read_dict(file):
    return json.load(open(file))
def save_dict(file,dic):
    json.dump(dic, open(file,'w'))

def countdown(seconds):
    print("")
    for i in range(seconds+1):
        print("%i s left"%(seconds-i), end="\r")
        time.sleep(1)
    print("")
        
class API(Api):
    def __init__(self, file):
        self.file=file
        self.dic = read_dict(file)
        self.CONSUMER_KEY = self.dic['CONSUMER_KEY']
        self.CONSUMER_SECRET = self.dic['CONSUMER_SECRET']
        self.ACCESS_TOKEN_KEY = self.dic['ACCESS_TOKEN_KEY']
        self.ACCESS_TOKEN_SECRET = self.dic['ACCESS_TOKEN_SECRET']
        
        super(API,self).__init__(consumer_key=self.CONSUMER_KEY, 
                  consumer_secret=self.CONSUMER_SECRET,
                  access_token_key=self.ACCESS_TOKEN_KEY,
                  access_token_secret=self.ACCESS_TOKEN_SECRET)
        self.url = '%s/statuses/user_timeline.json' % (self.base_url)
    def getRateLimit(self):
        res = self.CheckRateLimit(self.url)
        if res.reset-time.time()<0:
            #print("Input new tokens for app Key:",self.dic['CONSUMER_KEY'])
            #self.dic['ACCESS_TOKEN_KEY'] = input("ACCESS_TOKEN_KEY") or self.ACCESS_TOKEN_KEY
            #self.dic['ACCESS_TOKEN_SECRET']= input("ACCESS_TOKEN_SECRET") or self.ACCESS_TOKEN_SECRET
            #save_dict(self.file, self.dic)
            self.__init__(self.file)
        else:
            return res.remaining, res.reset
def drop_fields(tweet,fields=['user','user_mentions','entities','retweeted_status','id']):
    for f in fields:
        tweet.pop(f,None)
    return tweet
class TwitterCrawler():

    def __init__(self, apis):
        self.apis = apis

    def api(self):
        idx = 0
        rm = -float('inf')
        reset=[]
        for i,a in enumerate(self.apis):
            remain, res = a.getRateLimit()
            reset.append(res)
            if rm<remain:
                idx=i
                rm=remain
        if rm ==0:
            reset = max(reset)
            print("\nRate Limit reachead, wait %d s"%(reset-time.time()))
            countdown(int(reset-time.time()+1))
            return self.api()
        print("Remaining reqs:",rm)
        return self.apis[idx]
    
    def getTweets(self,user_id, counts=400):
        res = None
        try:
            res = self.api().GetUserTimeline(user_id=user_id,count=counts)
            res = [drop_fields(r._json) for r in res]
        except Exception as err:
            print(res)
            print(err)
        return res
            
    
