from irc import *
import os
import random

channel = "##bot-testing"
server = "irc.snoonet.org"
nickname = "glambot"

irc = IRC()
irc.connect(server, channel, nickname)

while 1:
    text = irc.get_text()
    print(text)

    if bytes("PRIVMSG", "UTF-8") in text and channel in text and bytes("hello", "UTF-8") in text:
        irc.send(channel, "Hello!")
