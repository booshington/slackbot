from slackclient import SlackClient
import os, time

'''
    @author:    boosh
    @desc:      Basic Slack Bot, reads local file oauth readonly to retrieve bot access API token, 
                runs loop waiting for key statements, then generates responses.
'''

#retrieves token, creates slack client
f = open("oauth","r")
token=f.readline().splitlines()[0]
sc = SlackClient(token)

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
                botResponse(event["text"])
        time.sleep(1)

#bot responses and logic is stored here.
def botResponse(text):
    if "magic4321" in text:
        return sendBotResponse(1)

def sendBotResponse(resp):
    if resp == 1:
        sc.api_call("chat.postMessage",channel="chatbots", text="You said the magic word!")

main()
