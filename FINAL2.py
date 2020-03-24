#aum namma ganeshaya namaha
import schedule
import time
#import config1
#import config2
import smtplib #Simple mail transfer protocol
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # New line
from email.mime.base import MIMEBase  # New line
from email import encoders  # New line
import QR
import empty_detect
import base


class Static_variable: #creating a static variable
    count_hour = 0
class scheduling_remainders:# to remind the user everyhour abt his parking
    def __init__(self):
        self.data = "Your car been parked for %d hours! just a reminder\n"%(Static_variable.count_hour)
    def job(self):
        #send this in mail
        temp = Mailing(self.data)
        temp.send_mail()
    def schedule(self,job):#job is the function to be scheduled again and again
        if Static_variable.count_hour==0: #so that first time it doesnt take one hour to print out the hourly counter
            job()
        Static_variable.count_hour+=1
        schedule.every(1).hour.do(job)
        while True:  #becomes false once the user takes out the car
            schedule.run_pending()
            time.sleep(1)
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
            server.sendmail("danceboyyaya@gmail.com",price[-1][-2],self.message_body) 
            print("Mail sent successfully")
            #terminating the server now
            server.quit()
        except smtplib.SMTPConnectError as s:
            print(s) #managing any error, i wish it doesnt happen during our event
class image_mail:
    def __init__(self):
        pass
    def send_image(self):
        email = 'danceboyyaya@gmail.com'
        password = 'chandra69chandra'
        send_to_email = price[-1][-2]
        subject = 'Parking details'
        message = 'From visionX'
        file_location = 'out.jpg'
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = send_to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        # Setup the attachment
        filename = os.path.basename(file_location)
        attachment = open(file_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        # Attach the attachment to the MIMEMultipart object
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        text = msg.as_string()
        server.sendmail(email, send_to_email, text)
        print("Mail sent successfully")
        server.quit()
#Input from sensor
inp =  1
if inp:
        #print("Scan QR")
        output = QR.scan().strip("b'")
        price =  base.check(output)  #A tuple (price amount, out) where second element = [regno, name, email, hours]
        #print("This is price : ", price[0])
        if price [0] == 1:
                empty_detect.empty()
                try:
                    user_image = image_mail()
                    user_image.send_image()
                    #user_schedule = scheduling_remainders()
                    #
                    user_schedule.schedule(user_scheduling.job())
                except : pass

        elif price[0] >= 1:
            user_money= Mailing(str(int(price[0])))
            user_money.send_mail()
            print("Thanks for using our service")
        else:
            print("You haven't subscribed\n")
        
