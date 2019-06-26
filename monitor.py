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
	

def logWriter(message):
	with open("./connections.log", "w") as outFile:
			outFile.write(message + \n)
			
main()