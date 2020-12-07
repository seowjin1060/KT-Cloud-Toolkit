import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import server

# ref : https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make 
# Zone parameter : Mandatory
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example
# print(server.stopVirtualMachine (zone='KR-M', \
#     id='2a40283f-148d-4144-a6ce-e042fad08109'))
# wait few minutes...
print(server.destroyVirtualMachine (\
    zone='KR-M', \
    vmid='89dab3a8-2e17-42b5-b42a-62e05a06f04b'))
