from machine import UART, Pin
from NetworkHelper import NetworkHelper
import time
import sys

from SG90 import Servo


def wifi():
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # print("RPi-Pico MicroPython Ver:", sys.version)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    esp8266_at_ver = None
    print("StartUP", con.startUP())
    # print("ReStart",con.reStart())
    print("StartUP", con.startUP())
    print("Echo-Off", con.echoING())
    print("\r\n\r\n")
    esp8266_at_ver = con.getVersion()
    if esp8266_at_ver != None:
        print(esp8266_at_ver)
    print("\r\n\r\n")
    wifimode = con.getCurrentWiFiMode()
    print(f"WIFI mode : {wifimode}")
    if(wifimode != "STA"):
        con.setCurrentWiFiMode(mode=1)
        wifimode = con.getCurrentWiFiMode()
        print(f"WIFI mode : {wifimode}")
    print("\r\n\r\n")
    """
    Connect with the WiFi
    """
    ssid = "KUWIN."  # wifi name
    pwd = "tamarin17"  # password
    print("Try to connect with the WiFi..")
    timeout = 0
    # default delay wifi delay 2 sec
    while timeout < 6:
        if "WIFI CONNECTED" in con.connectWiFi(ssid, pwd):
            print("ESP8266 connect with the WiFi..")
            return True
            break
        else:
            print(".")
            timeout += 1
            time.sleep(0.5)
    if timeout >= 6:
        print("Timeout connect with the WiFi")
        return False

def getApi(host, path, param=""):
    print("\r\n\r\n")
    print("Now it's time to start HTTP Get/Post Operation.......\r\n")
    # host = "192.168.1.2"  # host
    # path = "/"  # path  ?? url
    #param = ""
    if param != "":
        path = path + "?" + param
    else:
        path = path
    timeout = 0
    # default delay get api delay 3 sec
    while timeout < 3:
        httpCode, httpRes = con.doHttpGet(host, path, delay=0.5)
        print(
            "-----------------------------------------------------------------------------"
        )
        print("HTTP Code:", httpCode)
        print("HTTP Response:", httpRes)
        print(
            "-----------------------------------------------------------------------------\r\n"
        )
        if httpCode == 200:
            print("Get data successful..\r\n")
            return httpRes
            break
        else:
            print("Error")
            print("Get data fail...")
            print("Please wait to try again....\r\n")
            timeout += 1
            time.sleep(0.5)
        if timeout >= 3:
            return False


con = NetworkHelper()
wifiCon = wifi()

host = "18.141.11.24"  # host
path = "/hw/get_by_id"  # path  ?? url
param = "ID=34"

servo = Servo(27)
led_red = Pin(9,Pin.OUT)

if (wifiCon):
    while(True):
        data = getApi(host, path, param)      
        if(data[0]['value'] == 180):
            servo.setServo180()
            print("180 degree")
        elif(data[0]['value'] == 90):
            servo.setServo90()
            print("90 degree")
        elif(data[0]['value'] == 0):
            servo.setServo0()
            print("0 degree")
        else:
            led_red.high()

        


