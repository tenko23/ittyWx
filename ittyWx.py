import requests, threading, time, math, textwrap
from datetime import datetime, timedelta
import requests.auth  #See readme for info.
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from TT_port import print_data
from RelayOn import turn_on_relay  #If no relay, comment this line out.
from RelayOff import turn_off_relay  #If no relay, comment this line out.
import gc

now = datetime.now()
wrapper = textwrap.TextWrapper(width=65)

s = requests.Session()
retries = Retry(total=math.inf,
                backoff_factor=1.5,
                status_forcelist=[ 101, 204, 205, 401, 404, 410, 444, 425, 429, 408, 500, 501, 502, 503, 504, 511, 520, 522, 524 ])
s.mount('https://', HTTPAdapter(max_retries=retries))

def garbage():
    time.sleep(0.5)
    gc.collect(generation=2)
    time.sleep(0.5)
    run_at = now + timedelta(minutes=30)  #Increase the frequency of garbage collection - if needed, here.
    delay = (run_at - now).total_seconds()
    print("\nFreeing memory (generation 2)\n")
    threading.Timer(delay, garbage).start()

print("\nStart Time: ",datetime.now(), "\n", flush=False)

def break_string(string):
    final_string = wrapper.fill(string)
    return final_string

alerts = []
new_data = False

def scrape_alerts():
    print("\nChecking (for) alerts...\n"  ,datetime.now().time(), "\n")
    api_data = requests.get("https://api.weather.gov/alerts/active/zone/NEC109").json()["features"]  #This is the county alert line... comment out the line below if a countywide alert is desired.  See Readme for info.
    #api_data = requests.get("https://api.weather.gov/alerts/active/area/NE").json()["features"]  #This is the statewide alert line... comment out the line above and uncomment this line if a statewide alert is desired.  See Readme for info.
    temp = []
    global alerts
    for new_dict in api_data:
        temp_dict = {}
        temp_dict['sent'] = new_dict['properties']['sent']
        temp_dict['event'] = new_dict['properties']['event']
        print(new_dict['properties']['event'])
        temp_dict['sendername'] = new_dict['properties']['senderName']
        temp_dict['description'] = new_dict['properties']['description']
        temp_dict['instruction'] = new_dict['properties']['instruction']
        temp_dict['areadesc'] = new_dict['properties']['areaDesc']
        if temp_dict in alerts:
            temp_dict["type"] = "old"
        else:
            temp_dict["type"] = "new"
            global new_data
            new_data = True
        temp.append(temp_dict)
    alerts = temp

def convert_to_string(data):
    bells = 4
    text = "{0}\n\n".format(data['sent'])
    text += "Urgent\n"
    text += "{0}\n".format(data['event'])
    text += "{0}\n\n".format(data['sendername'])
    text += "{0}\n\n".format(data['description'])
    if data['instruction'] is not None:
        text += "{0}\n\n".format(data['instruction'])
    areas_text = break_string(data['areadesc'])
    text += " Counties/locations include:\n{0}\n".format(areas_text)
    
    if "warning" in data['event'].lower():
        bells = 10
        text = "{0}\n\n".format(data['sent'])
        text += "ZZZZZ\n\n"
        text += "Bulletin\n"
        text += "{0}\n".format(data['event'])
        text += "{0}\n\n".format(data['sendername'])
        text += "{0}\n\n".format(data['description'])
        if data['instruction'] is not None:
            text += "{0}\n\n".format(data['instruction'])
        areas_text = break_string(data['areadesc'])
        text += " Counties/locations include:\n{0}\n".format(areas_text)
    elif "watch" in data['event'].lower():
        bells = 5
        text = "{0}\n\n".format(data['sent'])
        text += "ZZZZZ\n\n"
        text += "Bulletin\n"
        text += "{0}\n".format(data['event'])
        text += "{0}\n\n".format(data['sendername'])
        text += "{0}\n\n".format(data['description'])
        if data['instruction'] is not None:
            text += "{0}\n\n".format(data['instruction'])
        areas_text = break_string(data['areadesc'])
        text += " Counties/locations include:\n{0}\n".format(areas_text)
    final_output = "\nZCZC\n"+text+"NNNN\n\n"
    return final_output, bells

try:
    garbage()
    while True:
        scrape_alerts()
        if new_data:
            turn_on_relay()  #If no relay, comment this line out.
            time.sleep(7.0)  #If no relay, comment this line out.
            while new_data:
                for data in alerts:
                    if data["type"] == "new":
                        text, bells = convert_to_string(data)
                        print_data(text, bells)
                new_data = False
                alerts = [{k: v for k, v in alert.items() if k != 'type'} for alert in alerts]  #If no relay, comment this line out.
                scrape_alerts()  #If no relay, comment this line out.
            time.sleep(5.0)  #If no relay, comment this line out.
            turn_off_relay()  #If no relay, comment this line out.
            new_data = False  #If no relay, comment this line out.
        alerts = [{k: v for k, v in alert.items() if k != 'type'} for alert in alerts]
        time.sleep(3.7)

except Exception as e:
    print("\nExit Time: ",datetime.now(), "\n")
    print(e, "\n")
