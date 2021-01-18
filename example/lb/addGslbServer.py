import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import gslb

# ref : https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
# Zone parameter : Mandatory
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example
#checkGslbName : {'text': '중복없음'}
print(gslb.addGslbServer(
    zone='KR-M',
    svrNm='mytest1234',
    domainNm='test1234.g.ucloudbiz.com',
    persistence='use',
    ttl='30'
))

