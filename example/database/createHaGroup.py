import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.createHaGroup(
   instanceid='8ab079df-ca71-4f0f-aee6-b4db482fc4c1',
   slavecount='1',
   hamode='Y',
   semisync='N',
   hagroupname='ktclouddev_sdktest1!'
))
