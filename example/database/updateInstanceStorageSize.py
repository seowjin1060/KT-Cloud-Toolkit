import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make 

# simple example
print(db.updateInstanceStorageSize(
    instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce',
    storagesize='100',
    usageplantype='monthly'))
