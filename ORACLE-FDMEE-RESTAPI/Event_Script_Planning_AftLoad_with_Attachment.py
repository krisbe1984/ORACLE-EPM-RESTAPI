#=========================================================================================
#Purpose: Email Alert for the End User when the FDMEE Data Load Fail or Success.
#Author: Krishna Srinivasan Sr Solution Architect
#=========================================================================================

# Importing the Neccesary Packages
import smtplib
import os
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
import java.sql as sql

global vformt,vLocName,vPer,vPID,vRulename,vSrc,vformt1,vsts,vcatname,vformt2,vformt3

targetApp = str(fdmContext["TARGETAPPNAME"])

if (targetApp == "ApplicationName"):

	fdmAPI.logInfo("======================================================================")
	fdmAPI.logInfo("**** Write getProcessStates statuses to log during AftCheck script: Begin")
	p = fdmAPI.getProcessStates(fdmContext["LOADID"])
	pCHKSTATUS = p['CHKSTATUS']
	fdmAPI.logInfo("CHKSTATUS is " + str(pCHKSTATUS))
	pPROCESSSTATUS = p['PROCESSSTATUS']
	pVALSTATUS = p['VALSTATUS']
	fdmAPI.logInfo("VALSTATUS is " + str(pVALSTATUS))
	fdmAPI.logInfo("PROCESSSTATUS is " + str(pPROCESSSTATUS))
	sRuleName = fdmContext["RULENAME"]
	sLocName = fdmContext["LOCNAME"]
	sPeriod = fdmContext["PERIODNAME"]
	sSource = fdmContext["SOURCENAME"]
	fdmProcessID = fdmContext["LOADID"]
	scatname = fdmContext["CATNAME"]

	procStatusDescSQL = "SELECT PROCESSSTATUSDESC FROM TLOGPROCESSSTATES WHERE PROCESSSTATUSKEY = " + str(pPROCESSSTATUS)
	rsProcStatusDesc = fdmAPI.executeQuery(procStatusDescSQL, None) 
	rsProcStatusDesc.next() 
	procStatusDesc = rsProcStatusDesc.getString("PROCESSSTATUSDESC")
	fdmAPI.logInfo("PROCESS STATUS description is " + str(procStatusDesc))
	rsProcStatusDesc.close()
    
	if pPROCESSSTATUS == 32:
		vformt = "============================================================= \n"
		vLocName = "Location Name : %s \n" % sLocName
		vPer = "Period : %s \n" % sPeriod
		vcatname="Category %s \n" % scatname
		vPID = "Process ID : %s \n" % fdmProcessID
		vRulename = "Rule Executed : %s \n" % sRuleName
		vSrc = "Data Source %s \n" % sSource
		vformt1 = "\n"
		vsts = "Status : Data Load Failed.\n"
		vformt2 = "\n"
		vformt3 = "============================================================= \n"

        #Subject
		mail_subject = "DEV - FDMEE Data Load failed for %s %s" % (sLocName,scatname)

		#Sender
		mail_sender = 'test@test.com'

		#Recipients
		recipients = ['test@test.com']
		
        #Body
		mail_txt = "Hi, \n DEV - FDMEE Data Load failed: %s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n \n Regards, \n Hyperion Administrator" %(vformt,vLocName,vPer,vcatname,vPID,vRulename,vSrc,vformt1,vsts,vformt2,vformt3)
		mail_html = """\
		<html>
		<head></head>
		<body>
		<pr>Hi,<br>
		Please find below the status for Data Load from DEV Instance <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		<br>
		Regards,<br>
		Hyperion Admin <br>
		<br>
		<br>
		Note: This is an Auto Generated Email, please do not reply to this email id.
		</p>
		</body>
		</html>
		""" % (vformt,vLocName,vPer,vcatname,vPID,vRulename,vSrc,vformt1,vsts,vformt2,vformt3)
		mail = MIMEMultipart('mixed')
		mail['Subject'] = mail_subject
		mail['FROM']=mail_sender
		mail['To']=", ".join(recipients)
		mail_a=MIMEText(mail_html, 'html', 'utf-8')
		mail.attach(mail_a)
        
		#Attachment
		os.chdir("/u02/hypmqa/CM_Plan/outbox/logs")
		LogFile = "%s_%s.log" % (targetApp, fdmProcessID)
		fLog = file(LogFile)
		part = MIMEText(fLog.read())
		part.add_header('Content-Disposition', 'attachment; filename="%s"' % LogFile)
		mail.attach(part)

		#Connection to SMTP
		sndml = smtplib.SMTP("smtp.domain.com:25")
		sndml.sendmail(mail_sender, recipients, mail.as_string())
		sndml.quit()
	fdmAPI.logInfo("**** Write getProcessStates statuses to log during AftCheck script: End")
	fdmAPI.logInfo("======================================================================")

	if pPROCESSSTATUS == 31:
		vformt = "============================================================= \n"
		vLocName = "Location Name : %s \n" % sLocName
		vPer = "Period : %s \n" % sPeriod
		vcatname="Category %s \n" % scatname
		vPID = "Process ID : %s \n" % fdmProcessID
		vRulename = "Rule Executed : %s \n" % sRuleName
		vSrc = "Data Source %s \n" % sSource
		vformt1 = "\n"
		vsts = "Status : Data Load Completed.\n"
		vformt2 = "\n"
		vformt3 = "============================================================= \n"

        #Subject
		mail_subject = "DEV - FDMEE Data Load Completed for %s %s" % (sLocName,scatname)

		#Sender
		mail_sender = 'test@test.com'

		#Recipients
		recipients = ['test@test.com']
		
        #Body
		mail_txt = "Hi, \n DEV - FDMEE Data Load Completed: %s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n \n Regards, \n Hyperion Administrator" %(vformt,vLocName,vPer,vcatname,vPID,vRulename,vSrc,vformt1,vsts,vformt2,vformt3)
		mail_html = """\
		<html>
		<head></head>
		<body>
		<pr>Hi,<br>
		Please find below the status for Data Load from DEV Instance <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		%s <br>
		<br>
		Regards,<br>
		Hyperion Admin <br>
		<br>
		<br>
		Note: This is an Auto Generated Email, please do not reply to this email id.
		</p>
		</body>
		</html>
		""" % (vformt,vLocName,vPer,vcatname,vPID,vRulename,vSrc,vformt1,vsts,vformt2,vformt3)
		mail = MIMEMultipart('mixed')
		mail['Subject'] = mail_subject
		mail['FROM']=mail_sender
		mail['To']=", ".join(recipients)
		mail_a=MIMEText(mail_html, 'html', 'utf-8')
		mail.attach(mail_a)
        
		#Connection to SMTP
		sndml = smtplib.SMTP("smtp.domain.com:25")
		sndml.sendmail(mail_sender, recipients, mail.as_string())
		sndml.quit()
	fdmAPI.logInfo("**** Write getProcessStates statuses to log during AftCheck script: End")
	fdmAPI.logInfo("======================================================================")
