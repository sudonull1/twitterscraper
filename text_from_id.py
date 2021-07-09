#!/usr/bin/env python
# coding: utf-8

# In[1]:


f=open("id.csv","r")
lines=f.readlines()
result=[]
for x in lines:
    result.append(x[2:-1])
f.close()    


# In[2]:


from twython import Twython
import tweepy
CONSUMER_KEY = "1oBFQXOl09dFFA4Ud90E051MD"
CONSUMER_SECRET = "JarXdx9wU2aoUHP4vSjhmvRf6bT8h3Bya4AYv2C2xDQV3RbOTp"
OAUTH_TOKEN = "1397760755446042625-E5tVJYN0s4TGMnbJoVDi7hnewUEyO3"
OAUTH_TOKEN_SECRET = "osnqlmt8lCT6ymuZCq0307TW5ZxwXgoUcdnNCi9JzpVpg"
tweettext=[]
resultnew=[]
auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
twitter = Twython(
    CONSUMER_KEY, CONSUMER_SECRET,
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)
 


# In[ ]:



for i in result:
    try:
        status = api.get_status(i)
        text = status.text
        tweettext.append(text)
        resultnew.append(tweetid)
    except:
        pass
    
tweettext=pd.DataFrame(tweettext,columns={'text'});
resultnew=pd.DataFrame(resultnew,columns={'id'});
res=pd.concat([tweettext,resultnew],axis=1)
res.to_csv('harvardmod')
   
    


# In[ ]:




