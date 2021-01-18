import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import database as db

# ref : https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
# Zone parameter
    # 1) KR-CA : KOR-Central A Zone
    # 2) KR-CB : KOR-Central B Zone
    # 3) KR-M  : KOR-Seoul M Zone
    # 4) KR-M2 : KOR-Seoul M2 Zone

# simple example
print(db.createHaGroupSingleZone(
   instancename='sdktest5',
   storagesize='80',
   perfclass='1x1',
   maintenanceweekday='sun',
   parametergroupid='21',
   dbmastername='AAtest123',
   dbmasterpassword='abcd1234',
   dbname='AATest123',
   dbengineversion='5.6.24',
   mainzone='KR-M',
   remotezone='KR-M',
   usageplantype='monthly',
   hamode='Y',
   backupretention='2',
   semisync='N',
   hagroupname='hatest1'
))
