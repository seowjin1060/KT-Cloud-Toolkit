import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.listAccessControlGroupEntries(
    accesscontrolgroupid='55a56689-4a57-417c-8548-c4d6c8408c9b'
))
