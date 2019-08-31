#!/usr/bin/python

import sys
import datetime
import Adafruit_DHT 
import time
import calendar
import smtplib

#Configuration du type de sonde et du PIN
sensor = 22
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

#Récupération du temps
ts = str(calendar.timegm(time.gmtime())) + "000"

if str(sys.argv[1]) == 'temperature':
    if temperature is not None:
        print(ts + ',' '{0:0.1f}'.format(temperature))
    else:
        print('Err.')
        sys.exit(1)

elif str(sys.argv[1]) == 'humidity':
    if humidity is not None:
        print(ts + ',' + '{0:0.1f}'.format(humidity))
    else:
        print('Err.')
        sys.exit(1)

elif str(sys.argv[1]) == 'alert':
        if temperature > 20 :
            from email.MIMEMultipart import MIMEMultipart
            from email.MIMEText import MIMEText
            fromaddr = "exemple@gmail.com"
            toaddr = "exemple@exemple.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = "Temperature is high !"
            body = "Temperature is high ! Temp : " + str(temperature)
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, "xxxx")
            text = msg.as_string()
            server.sendmail(fromaddr, toaddr, text)
            server.quit() 

                                                                                                                                                                                                 1,10         Haut

