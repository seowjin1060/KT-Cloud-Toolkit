import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import loadbalancer as lb

# ref : https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
# Zone parameter : Mandatory
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example
print(lb.createLoadBalancer(zone='KR-M', \
    name='testlbkk2', \
    loadbalanceroption='roundrobin', \
    serviceport='80', servicetype='tcp', \
    healthchecktype='tcp'))
    # healthcheckurl='http://test11.com'))

