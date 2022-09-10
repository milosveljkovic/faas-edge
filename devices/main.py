import requests
from requests.auth import HTTPBasicAuth
import time
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
import uvicorn
import os
from requests_oauthlib import OAuth1

app = FastAPI()
FILE="HomeC_short.csv"    
homec_short = open(FILE, 'r')

global SAVING_MODE
SAVING_MODE=False
TURN_OFF=0

@app.post("/savemode")
def saveMode():
  global SAVING_MODE
  SAVING_MODE=True if SAVING_MODE==False else False
  return {'msg':'Ok'}

def saveMode(line):
  sd: str = line.split(",")
  if not sd[0]:
    return line
  sd[1]=float(sd[1])*0.5
  sd[4]=float(sd[4])*0.5
  sd[5]=float(sd[5])*0.5
  sd[6]=float(sd[6])*0.5
  sd[7]=float(sd[7])*0.5
  sd[8]=float(sd[8])*0.5
  sd[9]=float(sd[8])*0.5
  newLine=''
  for index,el in enumerate(sd):
    if (len(sd)-1) != index:
      newLine+=str(el)+","
    else:
      newLine+=str(el)
  return newLine

@app.on_event("startup")
@repeat_every(seconds=1)
def readDataFromSensor() -> None:
    try:
      line = homec_short.readline()
      if SAVING_MODE:
        print("SAVING MODE ON")
        line=saveMode(line)
        print(line)
      else:
        print("SAVING MODE OFF")
        print(line)
      url = "http://localhost:8081/api/v1/namespaces/_/actions/prst?blocking=false"
      data = {'data': line}
      headers = {'Content-Type': 'application/json',"Authorization":"Basic Nzg5YzQ2YjEtNzFmNi00ZWQ1LThjNTQtODE2YWE0ZjhjNTAyOmFiY3pPM3haQ0xyTU42djJCS0sxZFhZRnBYbFBrY2NPRnFtMTJDZEFzTWdSVTRWck5aOWx5R1ZDR3VNREdJd1A="}
      response = requests.post(url=url, json=data, headers=headers)
      print(response)
    except OSError:
      print("Could not open/read file:", FILE)

if __name__ == "__main__":
    uvicorn.run(app, debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8083)))