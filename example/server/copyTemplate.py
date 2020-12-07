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
print(server.copyTemplate(zone='KR-M', \
    id='d3bb554d-116c-495f-bcb2-bca65f607605', \
    sourcezoneid='95e2f517-d64a-4866-8585-5177c256f7c7', \
    destzoneid='eceb5d65-6571-4696-875f-5a17949f3317')) # from M-zone To A-Zone

