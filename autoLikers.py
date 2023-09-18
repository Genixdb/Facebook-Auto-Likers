import os
import time
import datetime
from author import Status

try:
	import requests
	from bs4 import BeautifulSoup as bs
except ImportError:
	os.system("pip install bs4")
	os.system("pip install requests")

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
def request_cookie():
	server = requests.get("https://az-like.com")
	cookie = server.cookies.get_dict()
	return cookie['az_likecom_session']
	
	
banner = """\x1b[34m
   ╔══╦═╦═╦╦══╦╗╔╗╔══╦╗╔╦═╦═╗
   ║╔═╣╦╣║║╠║║╩╗╔╝║══╣╚╝║║║╬║  \x1b[31mAUTHORIZATION \x1b[00m: \x1b[33mGENIX SHOP
\x1b[34m   ║╚╗║╩╣║║╠║║╦╝╚╗╠══║╔╗║║║╔╝  \x1b[31mFACEBOOK \x1b[00m: \x1b[33mhttps://facebook.com/MsreYazTV123
 \x1b[34m  ╚══╩═╩╩═╩══╩╝╚╝╚══╩╝╚╩═╩╝ 
"""

def Likers(cookies):
	clear()
	print(banner)
	targetID = input("\x1b[32m      TargetID \x1b[00m: \x1b[35m")
	print()
	headers = {
		"Host": "az-like.com",
		"accept": "application/json, text/plain, */*",
		"content-type": "application/json;charset=UTF-8",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
		"cookie": f"_gid=GA1.2.218249696.1694182129;__gads=ID=d928c394ec47fe7b-22afb117cbe30068:T=1694182130:RT=1694263039:S=ALNI_Mb47KlDdoMn4VBCp32I0XlOfvLEBw;__gpi=UID=00000c3e0b6efbc3:T=1694182130:RT=1694263039:S=ALNI_MYA0bHYFCljawriRpJc0ozaJZVZfg;_gat_gtag_UA_175303241_1=1;{cookies};_ga_Q6G7B4WRCL=GS1.1.1694259425.3.1.1694263133.0.0.0;_ga=GA1.2.1370309963.1694182129"
	}
	try:
		response3 = requests.post("https://az-like.com/likes",headers=headers,json={"fbid":targetID,"type":"1"})
		if response3.status_code == 200:
			total = response3.json()['success']
			id = response3.json()['log']['post_id']
			retry_time = datetime.datetime.now()
			strftime = retry_time.strftime("%H:%M:%S")
			print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[35mSent total \x1b[31m{total}\x1b[35m to post_id \x1b[31m{id} \x1b[36m!")
		elif response3.status_code == 400:
			next = response3.json()['next']
			retry_time = datetime.datetime.now()
			strftime = retry_time.strftime("%H:%M:%S")
			print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mRateLimited next {next} !")
		else:
			print(response3,response3.json())
	except requests.exceptions.ConnectionError:
		retry_time = datetime.datetime.now()
		strftime = retry_time.strftime("%H:%M:%S")
		print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mPlease check your internet network !")
		os._exit(0)
	except requests.exceptions.ReadTimeout:
		retry_time = datetime.datetime.now()
		strftime = retry_time.strftime("%H:%M:%S")
		print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mUnable to connect to the internet !")
		os._exit(0)

def loginWithTokenv2(tokens):
	headers = {
		"Host": "az-like.com",
		"accept": "application/json, text/plain, */*",
		"content-type": "application/json;charset=UTF-8",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36",
		"cookie": "_gid=GA1.2.218249696.1694182129;__gads=ID=d928c394ec47fe7b-22afb117cbe30068:T=1694182130:RT=1694263039:S=ALNI_Mb47KlDdoMn4VBCp32I0XlOfvLEBw;__gpi=UID=00000c3e0b6efbc3:T=1694182130:RT=1694263039:S=ALNI_MYA0bHYFCljawriRpJc0ozaJZVZfg;_ga_Q6G7B4WRCL=GS1.1.1694259425.3.1.1694263067.0.0.0;_ga=GA1.1.1370309963.1694182129;az_likecom_session=eyJpdiI6InJrZ2k0UHluTllPdnQ3c3h1NXdDdWc9PSIsInZhbHVlIjoiQzEyejk1MTdyY0k4LzZxYkk1U2xtQUZkMjdCUUZ4YmlRdHpOZVBVcTk4dW15aWw2NUQ0ZUV0ZFNCVkxnbmJJeDZ5RnFvb1pDVlBib0dpWHRWVERGRVNoQjVDajcvdDRQbjRIcnVpZEltYzZDN1g3QTBzZUphTHdaSGxGVFRaYUwiLCJtYWMiOiI0MmRiY2VmOGU2NmU5YzdhYjIwZDUzNTkxZWViZmFkYjFkZGM3MTg2OTAzMjViYTJmODJlMTFjNWMxYmEwZTA0In0%3D"
	}
	try:
		response = requests.post("https://az-like.com/loginWithToken_v2",headers=headers,json={"access_token": tokens})
		if response.status_code == 200:
			retry_time = datetime.datetime.now()
			strftime = retry_time.strftime("%H:%M:%S")
			cookie = response.headers['set-cookie'][:349]
			print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[35mSuccessfully !")
			time.sleep(1)
			Likers(cookie)
		else:
			retry_time = datetime.datetime.now()
			strftime = retry_time.strftime("%H:%M:%S")
			print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mUnable to login !")
	except requests.exceptions.ConnectionError:
		retry_time = datetime.datetime.now()
		strftime = retry_time.strftime("%H:%M:%S")
		print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mPlease check your internet network !")
		os._exit(0)
	except requests.exceptions.ReadTimeout:
		retry_time = datetime.datetime.now()
		strftime = retry_time.strftime("%H:%M:%S")
		print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mUnable to connect to the internet !")
		os._exit(0)

def home():
	clear()
	print(banner)
	Status()
	try:
		response = requests.get("https://az-like.com/login_v2",timeout=15).text
		html = bs(response, "html.parser")
		code_value = html.find("input", attrs={"id": "user-code"})['value']
		code_submit = html.find("button", attrs={"id": "btn-verify-login"})['onclick'][19:51]
		print(f"   \x1b[36m   [ Code : \x1b[00m{code_value} \x1b[36m]")
		print(f"   \x1b[36m   [ Link : \x1b[00mhttps://fb.com/device?user_code={code_value} \x1b[36m]")
		print()
		os.system(f"termux-open --view https://facebook.com/device?user_code={code_value}")
		input("  \x1b[32mPLEASE ENTER TO CONTINUE...")
		clear()
		print(banner)
		print("                 \x1b[00m[ \x1b[32mDATABASE\x1b[00m ]")
		print()
		headers = {
			"Host": "az-like.com",
			"accept": "application/json, text/plain, */*",
			"content-type": "application/json;charset=UTF-8",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36"
		}
		response2 = requests.post("https://az-like.com/verifyLogin",headers=headers,json={"code": code_submit})
		if response2.status_code == 200:
			retry_time = datetime.datetime.now()
			strftime = retry_time.strftime("%H:%M:%S")
			token = response2.json()['access_token']
			loginWithTokenv2(token)
		elif response2.status_code == 400:
			retry_time = datetime.datetime.now()
			strftime = retry_time.strftime("%H:%M:%S")
			res_msg = response2.json()['error']['message']
			print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31m{res_msg} !")
		else:
			print(response2.json(),response2)
	except requests.exceptions.ConnectionError:
		retry_time = datetime.datetime.now()
		strftime = retry_time.strftime("%H:%M:%S")
		print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mPlease check your internet network !")
		os._exit(0)
	except requests.exceptions.ReadTimeout:
		retry_time = datetime.datetime.now()
		strftime = retry_time.strftime("%H:%M:%S")
		print(f"  \x1b[00m[\x1b[33mINFO - {strftime}\x1b[00m] \x1b[36m: \x1b[31mUnable to connect to the internet !")
		os._exit(0)
	
	
home()
	

