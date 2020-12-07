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
# resourcetype : userVm, Template, ISO, Volume, Snapshot,Network, PortForwardingRule, FirewallRule
mytags = {'key':'os', 'value':'centos'}
print(server.deleteTags(zone='KR-M', \
    resourceids='47d2ea4c-d434-418b-a854-c99054abeff7', \
    resourcetype='userVm', \
    mytagkey=mytags['key'], mytagvalue=mytags['value']))

