import requests

from requests.structures import CaseInsensitiveDict

def rest_get(api_url):
    return requests.get(api_url)
    
def rest_post(api_url, data):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"
    return requests.post(api_url, headers=headers, data=data)
