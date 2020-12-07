import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import server

# ref : https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
# Zone parameter : Mandatory
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example
print(server.createOverlayNetwork(zone='KR-M', \
    name='AACtest1', \
    displaytext='AACtest1', \
    netmask='255.255.252.0', gateway='192.168.0.1', \
    startip='192.168.0.6', endip='192.168.0.180', \
    networkofferingid='d29454ca-373d-4135-9278-5a08358b8b61', \
    overlayid='d29454ca-373d-4135-9278-5a08358b8b61'))