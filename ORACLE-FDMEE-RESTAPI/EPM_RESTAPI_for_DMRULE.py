#=========================================================================================
#Purpose: This Python program trigger the FDMEE Data Load rule using the RESTAPI Web Services.
#It will Check the status and return the code. It has calendar defined the DM rule will run based
#on the dates and get the Start & End Period.
# Author: Krishna Srinivasan Sr Solution Architect
# =========================================================================================
import requests
import datetime
import json
import base64
import sys
from requests.auth import HTTPBasicAuth
from datetime import date, datetime, timedelta
from requests.auth import HTTPDigestAuth

#Global Variables
BASEURL="http://xyz.oraclecloud.com"
POSTURI='/aif/rest/V1/jobs'
DATARUL=BASEURL + POSTURI
DMRULENAME='TEST'
AUTHHEADER='provide the encrypted password'
now='X'
STPER='X'
ENDPER='X'
j='X'
l='X'


#now=datetime.now()
now=datetime.now()
CURYEAR='{:02d}'.format(now.year)
PREYEAR='{:02d}'.format(now.year-1)
NEXTTER='{:02d}'.format(now.year+1)

#now=CURYEAR+"-10-29"
#now=datetime.strptime(now, "%Y-%m-%d")

#Jan StartDate
JAN_STDATE = CURYEAR+"-01-28"
JAN_STDATE = datetime.strptime(JAN_STDATE, "%Y-%m-%d")

#Jan EndDate
JAN_ENDATE = CURYEAR+"-02-28"
JAN_ENDATE = datetime.strptime(JAN_ENDATE, "%Y-%m-%d")

#Feb StartDate
FEB_STDATE = CURYEAR+"-03-01"
FEB_STDATE = datetime.strptime(FEB_STDATE, "%Y-%m-%d")


#Feb EndDate
FEB_ENDATE = CURYEAR+"-03-27"
FEB_ENDATE = datetime.strptime(FEB_ENDATE, "%Y-%m-%d")

#Nar StartDate
MAR_STDATE = CURYEAR+"-03-28"
MAR_STDATE = datetime.strptime(MAR_STDATE, "%Y-%m-%d")

#Mar EndDate
MAR_ENDATE = CURYEAR+"-04-28"
MAR_ENDATE = datetime.strptime(MAR_ENDATE, "%Y-%m-%d")

#Apr StartDate
APR_STDATE = CURYEAR+"-04-29"
APR_STDATE = datetime.strptime(APR_STDATE, "%Y-%m-%d")

#Apr EndDate
APR_ENDATE = CURYEAR+"-05-27"
APR_ENDATE = datetime.strptime(APR_ENDATE, "%Y-%m-%d")

#May StartDate
MAY_STDATE = CURYEAR+"-05-28"
MAY_STDATE = datetime.strptime(MAY_STDATE, "%Y-%m-%d")

#May EndDate
MAY_ENDATE = CURYEAR+"-06-28"
MAY_ENDATE = datetime.strptime(MAY_ENDATE, "%Y-%m-%d")

#Jun StartDate
JUN_STDATE = CURYEAR+"-06-29"
JUN_STDATE = datetime.strptime(JUN_STDATE, "%Y-%m-%d")

#Jun EndDate
JUN_ENDATE = CURYEAR+"-07-27"
JUN_ENDATE = datetime.strptime(JUN_ENDATE, "%Y-%m-%d")

#Jul StartDate
JUL_STDATE = CURYEAR+"-07-28"
JUL_STDATE = datetime.strptime(JUL_STDATE, "%Y-%m-%d")

#Jul EndDate
JUL_ENDATE = CURYEAR+"-08-28"
JUL_ENDATE = datetime.strptime(JUL_ENDATE, "%Y-%m-%d")

#Aug StartDate
AUG_STDATE = CURYEAR+"-08-29"
AUG_STDATE = datetime.strptime(AUG_STDATE, "%Y-%m-%d")

#Aug EndDate
AUG_ENDATE = CURYEAR+"-09-27"
AUG_ENDATE = datetime.strptime(AUG_ENDATE, "%Y-%m-%d")

#Sep StartDate
SEP_STDATE = CURYEAR+"-09-28"
SEP_STDATE = datetime.strptime(SEP_STDATE, "%Y-%m-%d")

#Sep EndDate
SEP_ENDATE = CURYEAR+"-10-28"
SEP_ENDATE = datetime.strptime(SEP_ENDATE, "%Y-%m-%d")

#Oct StartDate
OCT_STDATE = CURYEAR+"-10-29"
OCT_STDATE = datetime.strptime(OCT_STDATE, "%Y-%m-%d")

#Oct EndDate
OCT_ENDATE = CURYEAR+"-11-27"
OCT_ENDATE = datetime.strptime(OCT_ENDATE, "%Y-%m-%d")

#Nov StartDate
NOV_STDATE = CURYEAR+"-11-28"
NOV_STDATE = datetime.strptime(NOV_STDATE, "%Y-%m-%d")

#Nov EndDate
NOV_ENDATE = CURYEAR+"-12-28"
NOV_ENDATE = datetime.strptime(NOV_ENDATE, "%Y-%m-%d")

#Dec StartDate
DEC_STDATE = CURYEAR+"-12-29"
DEC_STDATE = datetime.strptime(DEC_STDATE, "%Y-%m-%d")

#Dec EndDate CURR YEAR
DEC_ENDATECR = CURYEAR+"-12-31"
DEC_ENDATECR = datetime.strptime(DEC_ENDATECR, "%Y-%m-%d")

#Dec StartDate Next Year -1
DEC_STDATEPR = CURYEAR+"-01-01"
DEC_STDATEPR = datetime.strptime(DEC_STDATEPR, "%Y-%m-%d")

#Dec EndDate Next Year -1
DEC_ENDATEPR = CURYEAR+"-01-27"
DEC_ENDATEPR = datetime.strptime(DEC_ENDATEPR, "%Y-%m-%d")

# Jan Period Variable
if(JAN_STDATE <= now and  now <= JAN_ENDATE):
	STPER=CURYEAR+'01'
	ENDPER=CURYEAR+'01'

# Feb Period Variable
elif(FEB_STDATE <= now and  now <= FEB_ENDATE):
	STPER=CURYEAR+'02'
	ENDPER=CURYEAR+'02'

# Mar Period Variable
elif(MAR_STDATE <= now and  now <= MAR_ENDATE):
	STPER=CURYEAR+'03'
	ENDPER=CURYEAR+'03'

# Apr Period Variable
elif(APR_STDATE <= now and  now <= APR_ENDATE):
	STPER=CURYEAR+'04'
	ENDPER=CURYEAR+'04'

# May Period Variable
elif(MAY_STDATE <= now and  now <= MAY_ENDATE):
	STPER=CURYEAR+'05'
	ENDPER=CURYEAR+'05'
    
# Jun Period Variable
elif(JUN_ENDATE <= now and  now <= JUN_ENDATE):
	STPER=CURYEAR+'06'
	ENDPER=CURYEAR+'06'

# Jul Period Variable
elif(JUL_ENDATE <= now and  now <= JUL_ENDATE):
	STPER=CURYEAR+'07'
	ENDPER=CURYEAR+'07'
    
 # Aug Period Variable
elif(AUG_STDATE <= now and  now <= AUG_ENDATE):
	STPER=CURYEAR+'08'
	ENDPER=CURYEAR+'08'

# Sep Period Variable
elif(SEP_STDATE <= now and  now <= SEP_ENDATE):
	STPER=CURYEAR+'09'
	ENDPER=CURYEAR+'09'

#Oct Period Variable
elif(OCT_STDATE <=  now or  now <= OCT_ENDATE):
	STPER=CURYEAR+'10'
	ENDPER=CURYEAR+'10'
    
#Nov Period Variable
elif(NOV_STDATE <=  now or  now <= NOV_ENDATE):
	STPER=CURYEAR+'11'
	ENDPER=CURYEAR+'11'

#Dec Period Variable
elif(DEC_STDATE <=  now or  now <= DEC_ENDATECR):
	STPER=CURYEAR+'12'
	ENDPER=CURYEAR+'12'
    
#Dec Period Prior Year Variable
elif(DEC_STDATEPR <=  now or  now <= DEC_ENDATEPR):
	STPER=PREYEAR+'12'
	ENDPER=PREYEAR+'12'
   
# Call the Data Management Rule
def datamgmtrule():
		headers = {'Authorization': AUTHHEADER}
		payload={"jobType":"DATARULE","jobName":DMRULENAME,"startPeriod":STPER,"endPeriod":ENDPER,"importMode":"REPLACE","exportMode":"REPLACE"}
		dmsts = requests.post(DATARUL,data=json.dumps(payload),headers=headers)
		json_status=dmsts.json()
		j=json_status['jobId']
		rescode=dmsts.status_code
		#print(j)
		#print(rescode)
		if rescode==200:
		getjobstatus()
            #sys.exit(0)
		else:
			sys.exit(1)


# Get the FDMEE Job Status for the Data Load Rule
def getjobstatus():
		headers = {'Authorization': AUTHHEADER}
		l='RUNNING'
		while l=='RUNNING':
				jbsts=requests.get(DATARUL.format(j),headers=headers)
				jst=jbsts.json()
				l=jst['items'][0]['jobStatus']
        #print(l)
		if l=='SUCCESS':
			sys.exit(0)
		else:
			sys.exit(1)

# Main Funcation
if __name__ == '__main__':
	try:
		datamgmtrule()
	except requests.exceptions.RequestException as e:
		print(e)
