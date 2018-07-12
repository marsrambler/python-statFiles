'''
Created on Jun 15, 2018

@author: yiz
'''
import sys
import time
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_paytable():    
    url = ""
    querystring = {"":""}
    headers = {
        }
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
    print(response.text[0:200])

def get_initstat():
    url = ""
    querystring = {"":""}
    headers = {
        }
    response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
    resp_text = response.text[0:200]    
    print(resp_text)

def get_initstat_session():
    url = ""
    querystring = {"":""}
    headers = {
        }    
    req_session = requests.Session()
    response = req_session.request("GET", url, headers=headers, params=querystring, verify=False)
    resp_text = response.text[0:200]    
    print(resp_text)

def post_play(tid):
    url = ""
    querystring = {"":""}
    payload = ""
    payload1 = payload.replace("yiz", tid)
    
    #print("payload:")
    #print(payload1)
    
    headers = {
        }
    response = requests.request("POST", url, data=payload1, headers=headers, params=querystring, verify=False)
    print(response.text[0:200])


def post_play_session(req_sess, tid):
    url = ""
    querystring = {"":""}
    payload = ""
    payload1 = payload.replace("yiz", tid)
    
    #print("payload:")
    #print(payload1)
        
    headers = {
        }
    
    response = req_sess.request("POST", url, data=payload1, headers=headers, params=querystring, verify=False)
    if not response.ok:
        print("http response status: " + str(response.status_code))
        sys.exit(0)
        
    resp_text = response.text[0:1000] 
    print(resp_text) 
    
    
if __name__ == "__main__":
    print("Send get  [GET]:")
    get_paytable()    
    print("\n")
    
    print("Send get in Session [GET]:")
    req_session,sub_text2 = get_initstat_session()
    print("\n")
    
    for num in range(0,10):
        print("\n")
        print("Send play [POST], idx = " + str(num))
        sub_text2 = post_play_session(req_session, sub_text2)
        time.sleep(0.1)
        
    