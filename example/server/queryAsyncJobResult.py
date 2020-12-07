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
#python queryAsyncJobResult.py 'KR-M' '9820e9b2-d380-4cae-ba19-4102da6dd3b3'
print('Input Params : ', sys.argv[1], sys.argv[2])
print(server.queryAsyncJobResult(zone=sys.argv[1], jobid=sys.argv[2]))

# print(server.queryAsyncJobResult(zone='KR-M', jobid='c929772e-a487-4657-8ccc-23f5905c8185'))

