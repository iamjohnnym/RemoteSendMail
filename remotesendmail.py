#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from sys import exit
from smtplib import SMTP_SSL
from email.MIMEText import MIMEText


class RemoteSendMail():
    def __init__(self, sender, user_name, passwd, sending_port):
        self.smtp_server = 'smtp.gmail.com'
        self.sending_port = sending_port
        self.user_name = user_name
        self.passwd = passwd
        self.sender = sender
        self.recipient = []
        self.text_subtype = 'plain'
        self.subject = ''
        self.content = ''

    def isValidPort(self, sending_port):
        local_ip = '127.0.0.1'
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     
        try:
            sock.connect((local_ip, int(sending_port)))
            sock.shutdown(1)
            return True
        except:
            return False

    def setSender(self, sender):
        self.sender = sender

    def setUsername(self, user_name):
        self.user_name = user_name

    def setPasswd(self, passwd):
        self.passwd = passwd

    def setSubject(self, subject):
        self.subject = subject

    def setContent(self, content):
        self.content = content

    def setRecipient(self, recipient):
        if type(recipient) is 'list':
            self.recipient = recipient
        else:
            print 'Unable to add recipient, input must be in the form of a list'

    def setTextSubtype(self, text_subtype):
        self.text_subtype = text_subtype

    def getUsername(self):
        return self.user_name

    def getSender(self):
        return self.sender

    def getSubject(self):
        return self.subject
        
    def getContent(self):
        return self.content

    def getRecipient(self):
        return self.recipient

    def getTextSubtype(self):
        return self.text_subtype

    def run(self):
        if self.isValidPort(self.sending_port):


if __name__ == '__main__':
    gms = RemoteSendMail('',
                         '',
                         '',
                         '')
