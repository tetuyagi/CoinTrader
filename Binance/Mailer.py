# coding: utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import json

FROM_ADDRESS = 'mailerYG3@gmail.com'
MY_PASSWORD = 'tetuyagi'
TO_ADDRESS = 'tetuyagi0419@gmail.com'
BCC = 'tetuyagi0419@gmail.com'
SUBJECT = 'GmailのSMTPサーバ経由'
BODY = 'pythonでメール送信'


class Mailer:
    def __init__(self):
        self.fromAddress = ""
        self.myPassword = ""
        self.toAddressList = []

        self.load()

    def __create_message(self, subject, body):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = self.fromAddress

        toAddressList = self.__listToString(self.toAddressList)
        msg['To'] = toAddressList
        # msg['Bcc'] = bcc_addrs
        msg['Date'] = formatdate()
        return msg

    def load(self, filePath="Mailer.json"):
        with open(filePath, 'r') as f:
            jsonObj = json.load(f)
            self.fromAddress = jsonObj["from_address"]
            self.myPassword = jsonObj["my_password"]

            addressJson = jsonObj["to_address_list"]

            for i in range(len(addressJson)):
                self.toAddressList.append(addressJson[i])

    def send(self, subject, body):
        msg = self.__create_message(subject, body)

        smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpobj.ehlo()
        smtpobj.starttls()
        smtpobj.ehlo()
        smtpobj.login(self.fromAddress, self.myPassword)
        #
        smtpobj.sendmail(self.fromAddress, self.toAddressList, msg.as_string())
        smtpobj.close()

    def __listToString(self, list):
        str = ""
        length = len(list)
        for i in range(length):
            str += list[i]
            if(i != length-1):
                str += ","

        print(str)
        return str


if __name__ == '__main__':
    subject = "SUBJECT"
    body = "陳ぽこ太郎"

    mailer = Mailer()
    mailer.send(subject, body)
