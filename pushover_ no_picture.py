#!/usr/bin/python
 
import httplib, urllib
 
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "YOUR_TOKEN_HERE",                       # Insert app token here
    "user": "YOUR_USER_ID_HERE",                       # Insert user token here
    "html": "1",                                # 1 for HTML, 0 to disable
    "title": "Motion Detected!",                # Title of the message
    "message": "<b>Garage</b> camera!",     # Content of the message - include HTML if required
    "url": "YOUR_URL_HERE",               # Link to be included in message
    "url_title": "View live stream",            # Text for the link
    "sound": "siren",                           # Define the sound played on the receiving device
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
