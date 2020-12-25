# 7-12-2020
# request model for http request
# it is used for request  http and get response from it
import requests
r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=b2da6be3aef2442aa6c1b8fe70b34f44")
# print(r.text)
print(r.status_code)

url = ("http://newsapi.org/v2/top-headlines?country=in&apiKey=b2da6be3aef2442aa6c1b8fe70b34f44")
# data = {
#     "p1":"1",
#     "p2":"2"
# }

r2 = requests.post(url=url)#, data= data)
print(r2)