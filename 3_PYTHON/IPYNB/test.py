############################# OPEN DIALOG
#-*- coding:utf-8 -*-
import urllib3
import json
 
openApiURL = "http://aiopen.etri.re.kr:8000/Dialog"
accessKey = "74ae25e3-777e-48c6-a3e6-e3e10f56c3c1"
access_method = "ACCESS_METHOD"
method = "open_dialog"
name = "DOMAIN_NAME"
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "name": name,
        "method": method,
        "access_method": access_method
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(str(response.data,"utf-8"))