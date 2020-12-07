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
print(server.updateUsagePlanTypeForServer(zone='KR-M', \
    type='disk', usagePlanType='hourly', \
    id='6f08d33e-1187-4d1e-be40-e24fd638280c'))
    # type='ip', # disk or ip
    # usagePlanType='hourly',
    # id='3a304bed-d7c0-4836-a31f-c4e10d2ab0be'))

# type : disk or ip