#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
RemoteSendMail - v1.0.0

Send mail from remote servers.  It's defaulted to Gmail.

"""

import socket
import re
from sys import exit
from smtplib import SMTP_SSL as SMTP
from email.MIMEText import MIMEText


class EmailError(Exception):
    pass


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

    def clearRecipient(self):
        """
        Sets self.recipient back to an empty list
        """
        self.recipient = []

    def isValidEmail(self, recipient):
        """
        Validate the outgoing + recipient email addresses
        """
        if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", \
                    recipient):
            return True
        else:
            raise EmailError('Invalid Email Address')

    def setSmtpServer(self, smtp_server):
        """
        Set te remote SMTP server that you want to connect to
        """
        self.smtp_server = smtp_server

    def setPort(self, sending_port):
        """
        Connect to a live port for the remote server
        """
        self.sending_port = sending_port

    def setSender(self, sender):
        """
        Set the email address of who the email is from
        """
        try:
            if self.isValidEmail(sender):
                self.sender = sender
        except EmailError as e:
            print e

    def setUsername(self, user_name):
        """
        Set username for the user you wish to use to connect remotely
        """
        self.user_name = user_name

    def setPasswd(self, passwd):
        """
        Set password for the designated username
        """
        self.passwd = passwd

    def setSubject(self, subject):
        """
        Set email subject
        """
        self.subject = subject

    def setContent(self, content):
        """
        Set email's content
        """
        self.content = content

    def setRecipient(self, recipient):
        """
        Set recipients of the email.  This is a list and it
        appends to self.recipient
        """
        try:
            if self.isValidEmail(recipient):
                self.recipient.append(recipient)
        except EmailError as e:
            print e

    def setTextSubtype(self, text_subtype):
        """
        Set the text subtype for the email
        """
        self.text_subtype = text_subtype

    def getSmtpServer(self):
        """
        Returns self.smtp_server
        """
        return self.smtp_server

    def getPort(self):
        """
        Returns self.port
        """
        return self.sending_port
        
    def getUsername(self):
        """
        Returns self.user_name
        """
        return self.user_name

    def getPasswd(self):
        """
        Returns self.passwd
        """
        return self.passwd

    def getSender(self):
        """
        Returns self.sender
        """
        return self.sender

    def getSubject(self):
        """
        Returns self.subject
        """
        return self.subject

    def getContent(self):
        """
        Returns self.content
        """
        return self.content

    def getRecipient(self):
        """
        Returns self.recipient
        """
        return self.recipient

    def getTextSubtype(self):
        """
        Returns self.text_subtype
        """
        return self.text_subtype
        
    def run(self):

        if self.getSender() and \
           self.getRecipient() and \
           self.getSubject() and \
           self.getContent():

            try:
                message = MIMEText(self.getContent(), self.getTextSubtype())
                message['Subject'] = self.getSubject()
                message['From'] = self.getSender()

                connection = SMTP(self.getSmtpServer(), self.getPort())
                connection.set_debuglevel(False)
                connection.login(self.getUsername(), self.getPasswd())

                try:
                    connection.sendmail(self.getSender(),
                                        self.getRecipient(),
                                        message.as_string())
                finally:
                    connection.close()
            except Exception, e:
                print "Message to {0} failed: {1}".format(
                                                self.getRecipient(), e)

        else:
            print 'fail'


if __name__ == '__main__':
    gms = RemoteSendMail('',
                         '',
                         '',
                         '')

    gms.setRecipient('foobar@bar.com')
    gms.setSubject('foo')
    gms.setContent('rawr')
    gms.run()
