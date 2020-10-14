#=========================================================================================
#Purpose: This Python program will encrypt the username and password.The encrypted content 
#can be passed as part of Header Authorization
#it will be passed to header autorzation.
# Author: Krishna Srinivasan Sr Solution Architect
# =========================================================================================
import urllib3
import requests
from getpass import getpass
from base64 import b64encode

def authpass(username,password):
    encoded_credentials = b64encode(bytes(f'{username}:{password}',encoding='ascii')).decode('ascii')
    auth_header = f'Basic {encoded_credentials}'
    print(f'Auth header: {auth_header}')


# Main Funcation
if __name__ == '__main__':
	try:
		authpass(input('Enter the Admin username:'),getpass('Enter the Admin password:'))
	except requests.exceptions.RequestException as e:
		print(e)