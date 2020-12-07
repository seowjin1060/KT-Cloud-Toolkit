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
print(server.createTemplate(zone='KR-M', \
    displaytext='AAATest', name='AAATest', \
    ostypeid='69a99f0e-4299-11e9-8624-1e00d900072f', \
    volumeid='83617062-0aa4-4c18-8b04-a810c2bbb597'))

