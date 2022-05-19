import restful_request
import log
import time

from log import LOG_I, LOG_W, LOG_E, LOG_H, LOG_B, LOG_T
from restful_request import rest_get, rest_post

TAG = "app_main"

api_url = "https://api.meplis.dev/v1/vals/output"

output_val = 0
packet_cnt = 0
while True:
    data = '{"value":'+str(output_val)+ '}'
    resp = rest_post(api_url, data)
    LOG_H(TAG, f"~~~~~~~~~~~~~~Test packet:{packet_cnt}~~~~~~~~~~~~~~")
    LOG_I(TAG, f"Post response:{resp.status_code}")
    LOG_I(TAG, f"Post data:{data}")
    resp = rest_get(api_url)
    LOG_I(TAG, f"Get response:{resp.status_code}")
    LOG_I(TAG, f"Get data:{resp.text}")
    LOG_H(TAG, f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    if output_val == 3:
        output_val = 0
    else:    
        output_val +=1
    packet_cnt+=1
    time.sleep(1)