from datetime import datetime
import pytz

LON = pytz.timezone('Europe/London')
NYC = pytz.timezone('America/New_York')
PTL = pytz.timezone('America/Los_Angeles')
datetime_lon = datetime.now(LON)
datetime_nyc = datetime.now(NYC)
datetime_ptl = datetime.now(PTL)
curTimeLon = (datetime_lon.strftime('%H'))
curTimeNYC = (datetime_nyc.strftime('%H'))
curTimePTL = (datetime_ptl.strftime('%H'))

if  int(curTimeLon)<9 or int(curTimeLon)>=17:
    print("London: ", datetime_lon.strftime('%H:%M:%S %m-%d-%Y'), "- Closed")
else:
    print("London: ", datetime_lon.strftime('%H:%M:%S %m-%d-%Y'), "- Open")

if  int(curTimeNYC)<9 or int(curTimeNYC)>=17:
    print("New York City: ", datetime_nyc.strftime('%H:%M:%S %m-%d-%Y'), "- Closed")
else:
    print("New York City: ", datetime_nyc.strftime('%H:%M:%S %m-%d-%Y'), "- Open")

if  int(curTimePTL)<9 or int(curTimePTL)>=17:
    print("Portland, OR: ", datetime_ptl.strftime('%H:%M:%S %m-%d-%Y'), "- Closed")
else:
    print("Portland, OR: ", datetime_ptl.strftime('%H:%M:%S %m-%d-%Y'), "- Open")          
