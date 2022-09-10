# coding=UTF-8
#
# Use this script to quickly send a bunch of mails. Useful for testing.
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import psycopg2

DATE_FORMAT_1 = "%a, %d %b %Y %H:%M:%S -0700 (UTC)"
DATE_FORMAT_2 = "%d %b %Y %H:%M:%S -0800"
DATE_FORMAT_3 = "%-d %b %Y %H:%M:%S -0800"
DATE_FORMAT_4 = "%a, %d %b %Y %H:%M:%S -0700"
DATE_FORMAT_5 = "%a, %d %b %Y %H:%M:%S -0700 UTC"
DATE_FORMAT_6 = "%a, %-d %b %Y %H:%M:%S -0700 (UTC)"
DATE_FORMAT_7 = "%a, %-d %b %Y %H:%M:%S -0700"

useSSL = False
# address = "127.0.0.1"
address = "smtp-service.default"
smtpPort = 2500
price=12.41

def makeTextMessage(subject, date, dateFormat, body, multipart=False):
    if multipart:
        msg = MIMEMultipart()
        msg.attach(MIMEText(body))
    else:
        msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = getRandomFrom()
    msg["To"] = getRandomTo()
    msg["Date"] = date.strftime(dateFormat)

    return msg

def getRandomFrom():
    return 'smart.home.reporter@gmail.com'

def getRandomTo():
    return 'user@example.com'


def sendMail(msg):
    if not useSSL:
        server = smtplib.SMTP("{0}:{1}".format(address, smtpPort))
    else:
        server = smtplib.SMTP_SSL("{0}:{1}".format(address, smtpPort))

    fromAddress = msg["From"]
    to = [msg["To"]]

    server.sendmail(fromAddress, to, msg.as_string())
    server.quit()

def connectToDb():
    print("Connecting to db")
    # conn=psycopg2.connect("host=localhost port=5432 dbname=postgres user=postgres password=postgres")
    conn=psycopg2.connect("host=pg-minikube-postgresql.default port=5432 dbname=postgres user=postgres password=postgres")
    cur=conn.cursor()
    return cur, conn

def disconnect(cur):
    print("Disconnect from db")
    cur.close()

def main(dict):
    try:
        cur,conn = connectToDb()
        cur.execute('SELECT * FROM iot.smart_home ORDER BY "time" ASC ')
        x = cur.fetchall()
        startDate=x[0][0]
        endDate=x[len(x)-1][0]
        consumedEnegery=0
        generatedEnergy=0
        dw=0
        fu=0
        fu2=0
        ho=0
        fr=0
        wc=0
        totalCost=0
        for d in x:
          generatedEnergy+=d[2]
          consumedEnegery+=d[1]
          dw+=d[3]
          fu+=d[4]
          fu2+=d[5]
          ho+=d[6]
          fr+=d[7]
          wc+=d[8]
        difference=endDate-startDate
        totalEnegery=consumedEnegery - generatedEnergy
        if difference.days == 0:
          totalCost=totalEnegery*price
        else:
          totalCost=totalEnegery*difference.days*price

        html = """
        <html><body>
        <h2>Smart Home App Report</h2>
        <p>Description: Energy Consumption</p>
        <p>From: {}  | To: {}</p>
        <p>Total Energy Consumption [kW]: {} </p>
        <p>Dishwasher [kW]: {} </p>
        <p>Furance [kW]: {} </p>
        <p>Furance2 [kW]: {} </p>
        <p>Home office [kW]: {} </p>
        <p>Fridge [kW]: {} </p>
        <p>Wine cellar [kW]: {} </p>
        <p>Total Cost: {} $</p>
        </body>
        </html>
        """.format(startDate.strftime("%a, %d %b %Y %H:%M"), endDate.strftime("%a, %d %b %Y %H:%M"), totalEnegery,dw,fu,fu2,ho,fr,wc,totalCost)

        msg = makeTextMessage(
            "Smart Home Report From {} To {}".format(startDate, endDate),
            datetime.datetime.now(),
            DATE_FORMAT_1,
            html
        )

        sendMail(msg)
    except Exception as e:
      return {"Error":"An error occurred while trying to connect and send the email: {0}".format(e.message)}
    except:
        print("Something went wrong related to DB")
        return {"Error":"Something went wrong"}
    return {"msg":"Successfully sent report"}