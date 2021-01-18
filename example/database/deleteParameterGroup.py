import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.deleteParameterGroup(
   parametergroupid='21d6a82f-7eb1-4889-bd2e-6c761320ae39'
))
