#=========================================================================================
#Purpose: This Python program will download the activity JSON report from EPM Cloud Directory
#         and transform the file into CSV file. The #Essbase BSO Cube Statistics.User Ondemand Feedback
#Author: Krishna Srinivasan (Grant Thornton LLP)
#Date: 12-11-2020
# =========================================================================================
import requests
import os
import json
import sys
import time
import csv
import urllib.parse
from urllib import parse
from urllib.parse import quote
from requests.auth import HTTPBasicAuth
from datetime import date, datetime, timedelta
from requests.auth import HTTPDigestAuth
import pandas as pd


z="X"
GETFILELISTURL="interop/rest/11.1.2.3.600/applicationsnapshots/"
FEEDBACKURI="interop/rest/11.1.2.3.600/feedback/"
DOWNLOADURI="interop/rest/v1/applicationsnapshots/"
TGTFilename="Feedback_ActivityReport"
TGTFileext=".json"
AUTH1='Basic '
AUTH='X'
BASEURL='X'
finalapifilename="X"
TIMESTR = time.strftime("%Y-%m-%d-%H-%M-%S")
FINALCSVFILENAME="EssbaseReports"
FINALCSVEXT=".csv"
filetime="X"
CUST="OndemandFeedback-"
Feedbacknow=datetime.utcnow()
Feedbackutc = Feedbacknow.strftime("%Y-%m-%d-%H-%M-%S")

#Read the config file
def Fileread():
	global FINALAUTH
	global AUTH
	global BASEURL
	global FileDOwnloadLoc
	d = {}
	with open("Config.txt") as f:
		for line in f:
			x=line.split(':=')
			a=x[0]
			b=x[1]
			c=len(b)-1
			b=b[0:c]
			d[a]=b
		AUTH=d.get('AUTH')
		BASEURL=d.get('BASEURL')
		FileDOwnloadLoc=d.get('FileDOwnloadLoc')+'\\'
		FINALAUTH=AUTH1+AUTH

        
#Feedback from EPM Instance
def restapifeedback():
	Fileread()
	headers = {'Content-type': 'application/json','Authorization':FINALAUTH}
	fstatus = requests.post(BASEURL+FEEDBACKURI,json={"configuration":{"URL":BASEURL},"description":CUST+Feedbackutc},headers=headers)
	feedbacksts=fstatus.status_code
	if feedbacksts==200:
		print("Job Started UTC Time:"+Feedbackutc)
		print("Job will wait for 5 mins to collect stats and download the file to--->"+FileDOwnloadLoc)
		time.sleep(300)
		activityreport()
	else:
		print(" I AM OUT")
		sys.exit(1)

#Get the Feedback JSON file
def getfilestatus():
	global finalapifilename
	global filetime
	global ss
	global now1
	#Fileread()
	headers = {'Content-type': 'application/json','Authorization':FINALAUTH}
	now=datetime.utcnow()
	now1 = now.strftime("%Y-%m-%d")
	FILEPREFIX="apr/Feedback "+now1
	FILESUFFIX="/activityreport.json"
	status = requests.get(BASEURL+GETFILELISTURL,headers=headers)
	status.raise_for_status()
	apifilename=status.json()
	for i in apifilename['items']:
		ss=i['name']
		if FILEPREFIX in ss:
			finalapifilename=FILEPREFIX+''+ss[23:32]+FILESUFFIX
			filetime=ss[23:32]
		#else:
			#print(" I AM OUT")
			#sys.exit(1)
	#print(finalapifilename)

#Get the Activity Report
def activityreport():
	global k
	global z
	getfilestatus()
	headers = {'Content-type': 'application/x-www-form-urlencoded','Authorization':FINALAUTH}
	FINALFILE=finalapifilename.replace('/','\\')
	b=urllib.parse.quote(FINALFILE,safe='',encoding='utf-8')
	status = requests.get(BASEURL+DOWNLOADURI+b+"/contents/",headers=headers)
	status.raise_for_status()
	s=status.json()
	status3=s['links'][0]['href']
	rescode=status.status_code
	k=s['links'][1]['href']
	z=k.replace('+','%20')
	if rescode==200:
		getjobstatus()
		print("Job Competed Successfully")
	else:
		sys.exit(1)

#Get the Job Status
def getjobstatus():
	headers = {'Authorization':FINALAUTH}
	l=-1
	while l==-1:
		jbsts=requests.get(z,headers=headers)
		jst=jbsts.json()
		l=jst['status']
		#print(l)
	if l==0:
		downloadjsonfile()
	else:
		exit(0)

#Donwload the JSON file and Convert to CSV Essbase Metrics
def downloadjsonfile():
	headers1 = {'Content-type': 'application/octet-stream','Authorization':FINALAUTH}
	statusfinal = requests.get(z+"/contents",headers=headers1)
	y=statusfinal.content
	with open(FileDOwnloadLoc+TGTFilename+'_'+now1+filetime+TGTFileext, "wb") as code:
		code.write(statusfinal.content)
	code.close()
	with open(FileDOwnloadLoc+TGTFilename +'_'+now1+filetime+TGTFileext) as file:
		data =json.load(file)
		for s in range(len(data['sarTables'])):
			if data['sarTables'][s]['title'] == "Essbase BSO Cube Statistics":
				for ss in range(len(data['sarTables'][s]['tableRows'])):
					flat=data['sarTables'][s]['tableRows'][ss]['tableData']
					flat1=json.dumps(flat,indent=2)
					df = pd.DataFrame(flat,columns=['string'])
					df1=df.T
					df1.to_csv(FileDOwnloadLoc+FINALCSVFILENAME+TIMESTR+FINALCSVEXT, sep=',', mode='a',encoding='utf-8',header=None,index=False)
#Main
if __name__ == '__main__':
	try:
		restapifeedback()
	except requests.exceptions.RequestException as e:
		print(e)
