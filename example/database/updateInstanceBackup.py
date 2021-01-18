import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.updateInstanceBackup(
    instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce',
    backupretention='5',
    backupstarthour='3',
    backupstartmin='13'
    # backupduration='4'
))
