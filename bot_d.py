from slackclient import SlackClient
import os, time

#for deferred-exit()
#from contextlib import ExitStack
#from functools import partial

'''
    @author:    boosh
    @desc:      Basic Slack Bot, reads local file oauth readonly to retrieve bot access API token, 
                runs loop waiting for key statements, then generates responses.
'''

DEBUG=False

#retrieves token, creates slack client
f = open("oauth","r")
try:
    f.readline()
    f.seek(0)
except FileNotFoundError as error:
    print("Exception thrown in token file:")
    print(error)
    exit()

token=f.readline().splitlines()[0]
sc=SlackClient(token)

def main():
    #connects with token
    if not sc.rtm_connect():
        print("error in authentication")
        return
    
    #sends a message to the channel tha the bot is active
    sc.api_call("chat.postMessage",channel="chatbots", text="G.O.L.I.A.T.H. ONLINE")

    #bot loop. for events, process the text and send a response, if any
    while True:
        events = sc.rtm_read()
        for event in events:
            if event["type"] == "message":
                if DEBUG:
                    print("got user message: "+event["text"])
                botResponse(event["text"])
        time.sleep(1)

#bot responses and logic is stored here.
def botResponse(text):
    if "magic4321" in text:
        return sendBotResponse(1)
    elif "shutdownbot99" in text:
        if DEBUG:
            print("shutting bot down")
        #defers shutdown to after the return
        #ExitStack().callback(partial(exit()))
        #return sendBotResponse(0)
        
        #kept this code because it's fun, this is faster:
        sendBotResponse(0)
        exit()

def sendBotResponse(resp):
    msg=""
    if resp == 0:
        msg="Bot Shutting Down...Whyy.yy..y......----"
    elif resp == 1:
        msg="You said the magic word!"
    else:
       return

    if ((DEBUG == True) and (msg != "")):
        print("Posting message: "+msg)

    sc.api_call("chat.postMessage",channel="chatbots", text=msg)

main()
