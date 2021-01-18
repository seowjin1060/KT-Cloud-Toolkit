import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance

# simple example
print(db.updateHaSemiSync(
    hagroupid='d1df63a3-a0c9-4e18-87c0-a804a0f2bf23',
    semisync='N'
))
