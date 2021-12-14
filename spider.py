import requests
from bs4 import BeautifulSoup
import json
import pprint 
from collections import deque

url = "https://ieeexplore.ieee.org/rest/document/738001/references"


def fetch_links(doc_link):

    payload={}
    # just need to change Referer header for different links
    headers = {
    'Connection': 'keep-alive',
    'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
    'Accept': 'application/json, text/plain, */*',
    'cache-http-response': 'true',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': '',
    'Accept-Language': 'en-US,en;q=0.9,bn;q=0.8',
    'Cookie': 'fp=21d23b7c3c889aaf8c611522b95cb473; s_ecid=MCMID%7C21774097973097263011716406627369542088; JSESSIONID=JvkKfee9dFCMlYxnw5anWFlFT8krPOGbCZeneocCNNHosulxjbTJu0021-1937166891; ipCheck=61.1.107.231; WLSESSIONAZ=237134346.20480.0000; TS01109a32=012933e65955ddca48991f794336c1fff71d6bc9395b130ff61c3c8e57833a48b4f0556d3738450f95688328261b03d62cb7f914c1; TS01cbcee7=012933e65955ddca48991f794336c1fff71d6bc9395b130ff61c3c8e57833a48b4f0556d3738450f95688328261b03d62cb7f914c1; ipList=61.1.107.231; AMCVS_8E929CC25A1FB2B30A495C97%40AdobeOrg=1; AMCV_8E929CC25A1FB2B30A495C97%40AdobeOrg=1687686476%7CMCIDTS%7C18922%7CMCMID%7C21774097973097263011716406627369542088%7CMCAAMLH-1637163369%7C12%7CMCAAMB-1637163369%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1636565769s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C3.0.0; s_cc=true; cookieconsent_status=dismiss; ERIGHTS=9qt3SXYwq3TducqMAAGsUOQWjQvM5Ft4*ITjYdRJI8oixxqyOevLFChQx3Dx3D-18x2ddH224qn8EB5TPTpUU0DGKQx3Dx3Dx2ByAyPttUcCXO2pp2IIzcGAx3Dx3D-UKxxUx2F9sE8W72L3zjFpJGagx3Dx3D-WDy0L5LbqD96lrh32v76Wgx3Dx3D; TS01dcb973=012933e65911894e86c745cbb655ff199190ecbe79b9d1cb7a5081c1135d03f61d99fd87c04630370abcd2cb9173d8e1d03a29b9ac; s_sq=%5B%5BB%5D%5D; utag_main=v_id:017ca3d55927001e3153666e02eb05072002b06a00978$_sn:3$_se:3$_ss:0$_st:1636562722566$vapi_domain:ieee.org$ses_id:1636560883471%3Bexp-session$_pn:3%3Bexp-session; xpluserinfo=eyJpc0luc3QiOiJ0cnVlIiwiaW5zdE5hbWUiOiJJbmRpYW4gSW5zdGl0dXRlIG9mIFRlY2hub2xvZ3kgLSBKb2RocHVyIiwicHJvZHVjdHMiOiJJRUx8VkRFfE5PS0lBIEJFTEwgTEFCU3wifQ==; seqId=1985775; TS01cbcee7=012933e65955ddca48991f794336c1fff71d6bc9395b130ff61c3c8e57833a48b4f0556d3738450f95688328261b03d62cb7f914c1; xpluserinfo=eyJpc0luc3QiOiJ0cnVlIiwiaW5zdE5hbWUiOiJJbmRpYW4gSW5zdGl0dXRlIG9mIFRlY2hub2xvZ3kgLSBKb2RocHVyIiwicHJvZHVjdHMiOiJJRUx8VkRFfE5PS0lBIEJFTEwgTEFCU3wifQ==; JSESSIONID=KvQKrNhWM-k0XKlOHxiT5lwjlhfQcXA84jnVIj0umkIK8LhFcNOt!-1053924985; TS01109a32=012933e65955ddca48991f794336c1fff71d6bc9395b130ff61c3c8e57833a48b4f0556d3738450f95688328261b03d62cb7f914c1; TS01dcb973=012933e6591a01f31a6a6442042467f56302c79deec3413b20ceff192e7acb6d4b82fb9d6105f75d3e961938518d8b98e9e754dfd8; WLSESSIONAZ=237134346.20480.0000; ipList=61.1.107.231,54.86.50.139; seqId=1985775'
    }

    max_papers = 50
    visited = {}
    queue = deque()

    papers = []
    queue.append(doc_link)

    while((len(papers) < max_papers) and (len(queue) > 0)):

        top = queue.popleft()
        visited[top] = True
        papers.append(top)

        print("Visiting: " + top)
        headers['Referer'] = 'https://ieeexplore.ieee.org/' + top + '/references'

        url = 'https://ieeexplore.ieee.org/rest/' + top + '/references'
        response = requests.request("GET", url, headers=headers, data=payload)

        # convert json to dictionary
        data = json.loads(response.text)

        # make dictionary of reference key in the data
        try:
            references = data['references']
        except:
            continue

        for x in references:
            x = dict(x)
            # check if key is in the dictionary
            if 'links' in x:
                # convert links to dictionary
                y = dict(x['links'])
                # print(y)
                # check if key is in the dictionary
                if 'documentLink' in y:
                    # print(y['documentLink'])
                    doc_url = y['documentLink']
                    if(doc_url not in visited.keys()):
                        queue.append(doc_url)
                        visited[doc_url] = False

    # print('Size of queue = ', len(queue))
    # for x in visited.keys():
    #     print(x)
    # print('-----------------------------------')
    return papers

        


