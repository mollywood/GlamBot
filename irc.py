import socket
import sys

class IRC:

    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send("PRIVMSG " + chan + " " + msg + "n")

    def connect(self, server, channel, botnick):
        #defines the socket
        print("connecting to:"+server)
        self.irc.connect((server, 6667))
        self.irc.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :This is a fun bot!n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "n", "UTF-8"))
        self.irc.send(bytes("JOIN " + channel + "n", "UTF-8")) #join the channel

    def get_text(self):
        text = self.irc.recv(2040) #receive the get_text

        if text.find(bytes('PING', 'UTF-8')) != -1:
            self.irc.send('PONG ' + text.split() [1] + 'rn')

        return text
