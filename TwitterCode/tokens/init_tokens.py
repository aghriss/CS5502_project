

import json 
def read_dict(file):
    return json.load(open(file))
def save_dict(file,dic):
    json.dump(dic, open(file,'w'))

dic = {}

dic['CONSUMER_KEY'] = "MNKxK17xCmM6p6VSNwAzJeIOC"
dic['CONSUMER_SECRET'] ="9EaV8HC5FKTjY2ddYA6MgFrjntj8f2A1Rmu3WXizJnJsVBXUoc"
dic['ACCESS_TOKEN_KEY']="1035857143771979776-uO1aNuLdcitUjp1uDodiLH1sG4WvzB"
dic['ACCESS_TOKEN_SECRET']="SXAFxpk3I7qbMTJ5aAVmbLgF6V0YbbL8zqjKohgBtXrGc"

save_dict("App1.key",dic)



dic['CONSUMER_KEY'] = "rdGXFKWHggTgHHRhuYG4zkRcO"
dic['CONSUMER_SECRET'] = "d0jzgBjsaUzFgJYuGmzCNAJ5gwspZ2ubftgdODjkBFz5CpUXCD"
dic['ACCESS_TOKEN_KEY'] = "1035857143771979776-rqsUcJP7HKPGKHcz6tjmex0uoZKLyD"
dic['ACCESS_TOKEN_SECRET'] = "B9SKyM5EoDROGaHZHfamFp2tFUqCs4LlP2TQ48jw6E1jU"

save_dict("App2.key",dic)