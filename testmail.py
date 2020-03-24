import smtplib
class Mailing: # this sends final destinatio,path to travel and so on
    def __init__(self,data):
        self.data=data
        self.message_body = "  " #initially the body should have no messages
    def send_mail(self):
        #trying to establish server here
        try:
            server = smtplib.SMTP("smtp.gmail.com",587)  # we are trying to create a session with gmail server
            server.starttls()  #we are trying to set up a transport layer security system to encrypt the mails being sent   #security feature
            server.login("danceboyyaya@gmail.com","chandra69chandra") #email ans password of host server which ll send the mails and config1 contains it
            self.message_body = self.data
            server.sendmail("danceboyyaya@gmail.com","danceboyyaya@gmail.com",self.message_body) #config 2 python file has email of users
            print("if it came till here then message sent successfully\n")
            #terminating the server now
            server.quit()
        except smtplib.SMTPConnectError as s:
            print(s) #managing any error, i wish it doesnt happen during our event
x=Mailing("hi\n")
x.send_mail()
