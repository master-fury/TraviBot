from flask import Flask, render_template, request
import requests
from datetime import datetime
import json


c_data = {}
trip_detail = []
fam_type = True
flag = False

with open('./convo.json') as f:
    c_data = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reply',methods=["POST"])
def suggestions():
    global flag
    global fam_type
    text = request.get_json()
    reply = text['data']
    if(reply == 'business trip'):
        fam_type = False
    if(text['type']=='robot'):
        import time
        time.sleep(1)
        if(c_data.get(text['data'])!=None):
            if(c_data[text['data']]['action'] == 'true' and c_data[text['data']]['position'] == 'end'):
                if(fam_type):
                    reply =  generte_receipt_family()
                else:
                    reply = generte_receipt_business()
            elif(c_data[text['data']]['action'] == 'true'):
                flag = True
                reply=c_data[text['data']]['result']
            else:
                reply=c_data[text['data']]['result']
        else:
            reply = "Sorry! I didn't get you."
    trip_detail.append(reply)   
    now = datetime.now()
    time = now.strftime("%H:%M")
    # print(trip_detail)
    return render_template('reply.html', reply=reply , time=time, type=text["type"])


def generte_receipt_family():
    receipt = "Your Reservations are as follows: Type of Trip:"+trip_detail[3]+" No of People:"+trip_detail[5]+" Current City:"+trip_detail[7]+" Destination City:"+trip_detail[9]+" Travelling Date:"+trip_detail[11]+" Returning Date"+trip_detail[13]+" Booked Stay:"+trip_detail[15]+"Your Email:"+trip_detail[17]+" .Payment Link has been sent successfully sent to your email. Thank you for using Travi!!"
    return receipt

def generte_receipt_business():
    receipt = "Payment Link has been sent successfully sent to your email. Thank you for using Travi!!"
    return receipt

if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(debug=False)