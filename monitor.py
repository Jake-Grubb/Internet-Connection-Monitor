#Programmer: Jacob Grubb (jgrubb013@gmail.com)
#Organzation: Independent
#Project: Internet Connection Monitor
#File: monitor.py
#Description: Python script to be ran in the background. 
#	Will attempt periodic connections to the internet over long periods of time.
#	Will then report results to a log to be analyzed.

import requests
import time


def main():
	while(True):
		#Script will wait 10 seconds between 
		time.sleep(10)
		#Attempt to contact
		try:
			requests.get('8.8.8.8', timeout=1)
			#If we get here, then success
			logWriter(time.strftime('%x %X') + ": " + "Successful")
		except requests.exceptions.Timeout:
			#Connection has timed out
			logWriter(time.strftime('%x %X') + ": " +  "Timeout")
		except requests.exceptions.ConnectionError:
			#Error with the connection: report this
			logWriter(time.strftime('%x %X') + ": " + + "Failure")
			
	

def logWriter(message):
	with open("./connections.log", "w") as outFile:
			outFile.write(message + \n)
			
main()