from slackclient import SlackClient
import os

f = open("oauth","r")
token=f.readline().splitlines()[0]
sc = SlackClient(token)


#connects with token
print("hey")
if sc.rtm_connect(with_team_state=False):
    print("also hey")
