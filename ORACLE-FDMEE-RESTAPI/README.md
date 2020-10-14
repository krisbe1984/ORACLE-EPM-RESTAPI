# ORACLE EPM-RESTAPI
 RESTAPI Header Autorization
 
Pre-requisite
----------------
1. Donwload  & Install Python.
2. Install Pip
3. Import Required Packages

Stpes to Execute the RESTAPI_AuthHeader_Password_Encryption.py
--------------------------------------------------------------

Note: This program will take the Username & Password as input and return
encrypted content. It can be used in the header autorization.

1. Execute the RESTAPI_AuthHeader_Password_Encryption.py program.
2. Provide the username & Password in the python program as part of header.


Stpes to Configure the EPM_RESTAPI_for_DMRULE.py
--------------------------------------------------------------
Note: This program will trigger the Data Load Rule for Direct Connect.
and it will check the status of the Data Load Rule

1. Update the the following Variables in the code
	a.DEVBASEURL - Base url for the Oracle Instance
	b.DMRULENAME - Name of the Data Load Rule.
	c.AUTHHEADER - Encrypted Password from the RESTAPI_AuthHeader_Password_Encryption (Program)

Stpes to Configure the Event_Script_Planning_AftLoad_with_Attachment.py
-------------------------------------------------------------------------
Note : This program will send an email alert to the user based on the status code
it is a Jython scrpit and will work in Oracle FDMEE Event Scripts. Do not run this
program from outside the FDMEE.

1. Update the below variables in the code
	a. targetApp - Provide the Target Application Name.
	b. mail_sender - Enter the email address.
	c. recipients - list To email address or group.
	d. sndml - Provide the SMTP details.






