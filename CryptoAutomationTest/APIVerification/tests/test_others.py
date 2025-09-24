import pytest
import requests
from APIVerification.BaseFunction import common

test_data=[
    #0.input random <0
    ({"random": -1,"marketId": 1,"code": "000001","language": "EN"},200,"0"),
    #1.input random =0
    ({"random": 0,"marketId": 1,"code": "000001","language": "EN"},200,"0"),
    #2.inout random not number
    ({"random": 'A',"marketId": 1,"code": "000001","language": "EN"},200,"0"),
    #3.missing random
    ({"marketId": 1,"code": "000001","language": "EN"},200,"0"),
    #4.input market<0
    ({"random": 0.048975734889627254,"marketId": -1,"code": "000001","language": "EN"},200,"-1"),
    #5.input market=0
    ({"random": 0.048975734889627254,"marketId": 0,"code": "000001","language": "EN"},200,"-1"),
    #6.input market=0 is not number
    ({"random": 0.048975734889627254, "marketId": 'a', "code": "000001", "language": "EN"},200,-1),
    #7.input missing market
    ({"random": 0.048975734889627254, "code": "000001", "language": "EN"},200,-1),
    #8.input code <6 char
    ({"random": 0.048975734889627254,"marketId": 1,"code": "00001","language": "EN"},200,"-1"),
    #9.input invalid code
    ({"random": 0.048975734889627254,"marketId": 1,"code": "test","language": "EN"},200,"-1"),
    #10.input missing code
    ({"random": 0.048975734889627254,"marketId": 1,"language": "EN"},200,"-1"),
    #11.input language is number
    ({"random": 0.048975734889627254,"marketId": 1,"code": "000001","language": 20},200,"0"),
    #12. input language is invalid
    ({"random": 0.048975734889627254, "marketId": 1, "code": "000001", "language": 'test'},200,"0"),
    #13. input missing language
    ({"random": 0.048975734889627254, "marketId": 1, "code": "000001"},200,"0")
]

@pytest.mark.parametrize('query_paramars,stautscode,code',test_data)
def test_others(query_paramars,stautscode,code):
    print (query_paramars,stautscode,code)

    res = common.call_api(query_paramars)

    #print (res.json())

    assert res.status_code == stautscode
    assert res.json()['code'] == code
