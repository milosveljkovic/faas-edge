
from array import array
from pydantic import BaseModel
from datetime import datetime
from util import removeNaNs, formatAll

class Sensor(BaseModel):
    time: str
    use: float
    gen: float
    dw: float         # dishwasher
    fu: float         # furance
    fu2: float
    ho: float         # home office
    fridge: float
    wc: float         # wine cellar

def main(dict):
    if 'data' in dict:
        sd = dict['data']
    else:
        sd = ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,"
    # only for testing locally
    # f = open("HomeC_short.csv", "r")
    a=format(3.33E-05,'.8f')
    print(a)
    # sd: str = f.readline().split(",")
    sd: str = sd.split(",")
    sd = formatAll(sd)
    sd = removeNaNs(sd)
    sensor = Sensor (
      time=datetime.utcfromtimestamp(int(sd[0])).strftime('%Y-%m-%d %H:%M:%S'),
      use= sd[1],
      gen= sd[2],
      dw= sd[4],
      fu= sd[5],
      fu2= sd[6],
      ho= sd[7],
      fridge= sd[8],
      wc= sd[9]
    )
    # return {"dw":6.0,"fridge":1.0,"fu":2.0,"fu2":4.0,"gen":5.0,"ho":4.0,"time":"1970-01-01 00:00:01","use":4.0,"wc":6.0}
    print(sensor.dict())
    return sensor.dict()

# main({"data": "1451624416,0.932833333,0.003483333,0.932833333,3.33E-05,0.0207,0.061916667,0.442633333,0.12415,0.006983333,0.013083333,0.000416667,0.00015,0,0.03135,0.001016667,0.004066667,0.001516667,0.003483333,36.14,clear-night,0.62,10,Clear,29.26,1016.91,9.18,cloudCover,282,0,24.4,0"})
# main()