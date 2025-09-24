import requests

def call_api(parmars):
    url = 'https://www.szse.cn/api/market/ssjjhq/getTimeData'
    headers = {'Content-Type': 'application/json'}

    res = requests.get(url=url,params=parmars,headers=headers)

    return res
    