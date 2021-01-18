import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.updateInstancePerfClass(
    instanceid='75652e98-b06c-47cc-a14b-55e2595ea897',
    perfclass='1x2'))
