import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.updateReplicationGroupSlaveCount(
    replicationgroupid='30f187f5-caa4-43e2-b169-d7b6dc2abd5f',
    slavecount='0'
))
