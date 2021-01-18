import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.deleteAccessControlGroup(
    accesscontrolgroupid='534a49fc-b230-46ef-a9c7-43337ea04090'
))
