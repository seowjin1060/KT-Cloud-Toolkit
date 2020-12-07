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
server.deployVirtualMachine()
print(server.deployVirtualMachine(zone='KR-M', \
    serviceofferingid='f86f09f6-9acf-4b30-936c-cfb409a89e68', \
    templateid='60b1376f-c576-440e-b36f-9b8b39b05104', \
    diskofferingid='87c0a6f6-c684-4fbe-a393-d8412bcf788d'\
    # , \  # choose : above 3 option or below 1 option
    # productcode='std_cent 7.0 64bit en_1x10' \
    ))
