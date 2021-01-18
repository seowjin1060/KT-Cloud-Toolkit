import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.updateInstanceAccessControlGroup(
    instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce',
    accesscontrolgroupids='a6d39205-5474-48d2-979e-9f3914157fc3'
))
