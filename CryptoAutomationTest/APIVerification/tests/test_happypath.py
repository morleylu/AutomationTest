import requests
from APIVerification.BaseFunction import common


def test_happypath():
    #define the paramars
    query_paramars = {
        "random": 0.048975734889627254,
        "marketId": 1,
        "code": "000001",
        "language": "EN"
    }

    #call API
    res = common.call_api(query_paramars)

    #return response
    print(res.status_code)
    data = res.json()['data']
    highprice = data.get('high')
    print(highprice)
    lowprice = data.get('low')
    print(lowprice)

    #assertion response
    assert res.status_code == 200
    assert res.json()['message'] == "成功"
    assert res.json()['code'] == "0"
    assert data['code'] == "000001"
    assert highprice>lowprice

test_happypath()

