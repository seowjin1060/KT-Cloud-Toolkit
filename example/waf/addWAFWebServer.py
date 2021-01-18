import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import waf

# ref : https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
# Zone parameter : Mandatory
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example 
print(waf.addWAFWebServer(
    zone='KR-M2',
    id='3108',
    vmid='78f205b5-6ef4-470a-9d47-437d356d104e',
    webserverport='80',
    proxyport1='80',
    sslmode='disabled',
    proxyport2='81'
))

