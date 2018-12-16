#ip address is machine1 = 10.20.4.25leaz
import tweepy
import schedule
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import datetime as date
import multiprocessing
import time


class MyListener(StreamListener):
 
    def on_data(self, data):
        today = str(date.date.today())  
        today = "Tweets" + today + ".json"
        try:
            with open(today, 'a') as f:
                #f.write(data.rstrip('\n') + ",")
                
                f.write(data.rstrip('\n'))
                #f.write(",".rstrip('\n'))
                
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True


    
def job():
    print("I'm working...")

def streamThings():
    
#Variables that contains the user credentials to access Twitter API 
    access_token = "1041739423564673024-VR0Tk2TV8HcmVE1WFPmo03dyD5bYex"
    access_secret = "BmGTwVEwZPfJtvDZ9vAVsKc5qUsmZY3kWuWKOxmYyxUEI"
    consumer_key = "MY84ronuaoXy8rjjiOCJ29zuG"
    consumer_secret = "n6eP50ATZV32rk1nAQo9wXzhCeWnUOgvjd8FUyHJN6kWRUrmsA"
    today = str(date.date.today())  
    today = "Tweets" + today + ".json"
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
 
    api = tweepy.API(auth)


    twitter_stream = Stream(auth, MyListener())
    keyword_list = ["#venom"]
    twitter_stream.filter(track=keyword_list, languages=['en'])

    
def doMoreStuff():
    while True:
        p = multiprocessing.Process(target=streamThings, name="Streaming")
        p.start()
        time.sleep(86400)
        p.terminate()
        p.join()
        print("Restarted Program")
    
if __name__ == '__main__':
    # Start foo as a process
    #schedule.every(1).minutes.do(doMoreStuff)
    #schedule.every().day.at("5:30").do(doMoreStuff)
    doMoreStuff()
    '''
    while 1:
        #print("Trying to do stuff")
        schedule.run_pending()
        time.sleep(300
    '''
    # Wait 10 seconds for foo
    #time.sleep(3600)

    # Terminate foo
    #p.terminate()

    # Cleanup
    #p.join()
    
    
 

#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
