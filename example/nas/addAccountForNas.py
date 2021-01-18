import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import nas

# ref : https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
# Zone parameter : Mandatory
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example
print(nas.addAccountForNas(zone='KR-M',
    cifsid='mytest',
    cifspw='test!13579',
    accountId='46616224-c207-4008-937e-a3ea504ae580',
    cifsworkgroup='workgroup'))
# print(nas.addAccountForNas(zone='KR-M2', id='1234'))
#'8359', \