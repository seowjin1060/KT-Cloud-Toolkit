#
#  kt cloud SDK v1.0
#
#  Copyright (c) 2020 kt corp. All rights reserved.
#
#  This is a proprietary software of kt corp
#  and you may not use this file except in compliance
#  with license agreement with kt corp.
#  Any redistribution or use of this software,
#  with or without modification shall be strictly
#  prohibited without prior written approval of kt corp,
#  and the copyright notice above does not evidence
#  any actual or intended publication of such software.
#
import common as c


def createInstance(**kargs):
    """ Create a new Database 
    * Args :
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - instancename(String, Required): name
        - storagesize(String, Required): DB Storage Size (10G~300G-step:10G)
        - perfclass(String, Required): CPU x MEM
        - maintenanceweekday(String, Required): maintenance Day (sun | mon | tue | wed | thu | fri | sat)
        - parametergroupid(String, Required): parametergroupid
        - dbmastername(String, Required): dbmastername
        - dbmasterpassword(String, Required): dbmasterpassword
        - dbname(String, Required): dbname
        - dbengineversion(String, Required): MySQL version
        - usageplantype(String, Required): hourly or monthly
    * Examples : 
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return 'Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone '
    if not 'instancename' in kargs:
        return '[ktcloud] Not required argument \'instancename\' (8~256 length english, numer )'
    if not 'storagesize' in kargs:
        return '[ktcloud] Not required argument \'storagesize\' (10G ~ 300G numer, interval 10G)'
    if not 'perfclass' in kargs:
        return '[ktcloud] Not required argument \'perfclass\' (CPUxMEM ) '
    if not 'maintenanceweekday' in kargs:
        return '[ktcloud] Missing required argument \'maintenanceweekday\' (sun | mon | tue | wed | thu | fri | sat)'
    if not 'parametergroupid' in kargs:
        return '[ktcloud] Missing required argument \'parametergroupid\' '
    if not 'dbmastername' in kargs:
        return '[ktcloud] Missing required argument \'dbmastername\' (1~16 length english, number)'
    if not 'dbmasterpassword' in kargs:
        return '[ktcloud] Missing required argument \'dbmasterpassword\' (8~15 length english, number)'
    if not 'dbname' in kargs:
        return '[ktcloud] Missing required argument \'dbname\' (1~64 length english, number)'
    if not 'dbengineversion' in kargs:
        return '[ktcloud] Missing required argument \'dbengineversion\' '
    if not 'usageplantype' in kargs:
        return '[ktcloud] Missing required argument \'usageplantype\' (monthly or hourly)'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zone'] = c.getzonesnamebyhname(ZoneName)
    print(kargs['zone'])
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='database', m2 = M2Bool)

    kargs['command'] = 'createInstance'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listInstances(**kargs):
    """ Database list
    * Examples : print(db.listInstances())
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """    
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listInstances'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateInstancePerfClass(**kargs):
    """ Update Database Class
    * Args :
        - instanceid(String, Required) : instanceid
        - perfclass(String, Required) : CPU x MEM
    * Examples : print(db.updateInstancePerfClass(instanceid='75652e98-b06c-47cc-a14b-55e2595ea897', perfclass='1x2'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'perfclass' in kargs:
        return '[ktcloud] Not required argument \'perfclass\' (CPU x MEM)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateInstancePerfClass'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateInstanceStorageSize(**kargs):
    """ Update Database Size
    * Args :
        - instanceid(String, Required) : instanceid
        - storagesize(String, Required) : storagesize
        - usageplantype(String, Required) : hourly or monthly
    * Examples : print(db.updateInstanceStorageSize(instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce', storagesize='100', usageplantype='monthly'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'storagesize' in kargs:
        return '[ktcloud] Not required argument \'storagesize\' '
    if not 'usageplantype' in kargs:
        return '[ktcloud] Not required argument \'usageplantype\' (hourly or monthly)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateInstanceStorageSize'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateInstanceBackup(**kargs):
    """ Update Database Backup Plan
    * Args :
        - instanceid(String, Required) : instanceid
        - backupretention(String, Required) : backup store duration 0~7
        - backupstarthour(String, Required) : 0~23
        - backupstartmin(String, Required) : 0~60
        - backupduration(String, Optional) : 2~8
    * Examples : print(db.updateInstanceBackup(instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce', backupretention='2', backupstarthour='2', backupstartmin='55', backupduration='3'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'backupretention' in kargs:
        return '[ktcloud] Not required argument \'backupretention\' (0~7 days)'
    if not 'backupstarthour' in kargs:
        return '[ktcloud] Not required argument \'backupstarthour\' (0~23 hour)'
    if not 'backupstartmin' in kargs:
        return '[ktcloud] Not required argument \'backupstartmin\' (0~60 min)'
    # if not 'backupduration' in kargs:
    #     return '[ktcloud] Not required argument \'backupduration\' (2~8 hours)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateInstanceBackup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateInstanceMaintenance(**kargs):
    """ Update Database Maintenance Plan
    * Args :
        - instanceid(String, Required) : instanceid
        - maintenanceweekday(String, Required) : sun ~ sat
        - maintenancestarthour(String, Required) : 0~23
        - maintenancestartmin(String, Required) : 0~60
        - maintenanceduration(String, Optional) : 4~8
    * Examples : print(db.updateInstanceMaintenance(instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce', maintenanceweekday='mon', maintenancestarthour='1', maintenancestartmin='23', maintenanceduration='8'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'maintenanceweekday' in kargs:
        return '[ktcloud] Not required argument \'maintenanceweekday\' (sun | mon | tue | wed | thu | fri | sat)'
    if not 'maintenancestarthour' in kargs:
        return '[ktcloud] Not required argument \'maintenancestarthour\' (0~23 hour)'
    if not 'maintenancestartmin' in kargs:
        return '[ktcloud] Not required argument \'maintenancestartmin\' (0~60 min)'
    # if not 'maintenanceduration' in kargs:
    #     return '[ktcloud] Not required argument \'maintenanceduration\' (2~8 hours)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateInstanceMaintenance'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateInstanceParameterGroup(**kargs):
    """ Update Database Parameter Group
    * Args :
        - instanceid(String, Required) : instanceid
        - parametergroupid(String, Required) : parameterGroupID
    * Examples : print(db.updateInstanceParameterGroup(zone='KR-M', instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce', parametergroupid='d83cdb0a-a5a3-44ce-874e-612bf9ed4620'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'parametergroupid' in kargs:
        return '[ktcloud] Not required argument \'parametergroupid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateInstanceParameterGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateInstancePassword(**kargs):
    """ Update Database dbmasterpassword
    * Args :
        - instanceid(String, Required) : instanceid
        - dbmasterpassword(String, Required) : dbmasterpassword
    * Examples : print(db.updateInstancePassword(zone='KR-M', instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce', dbmasterpassword='abcd1357'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'dbmasterpassword' in kargs:
        return '[ktcloud] Not required argument \'dbmasterpassword\' (8~32 chars)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateInstancePassword'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listAccessControlGroups(**kargs):
    """ Database AccessControlGroup List
    * Args : None
    * Examples : print(db.listAccessControlGroups())
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listAccessControlGroups'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateInstanceAccessControlGroup(**kargs):
    """ Update Database dbmasterpassword
    * Args :
        - instanceid(String, Required) : instanceid
        - accesscontrolgroupids(String, Required) : accesscontrolgroupids
    * Examples : print(db.updateInstanceAccessControlGroup(zone='KR-M', instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce', accesscontrolgroupids='a6d39205-5474-48d2-979e-9f3914157fc3'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'accesscontrolgroupids' in kargs:
        return '[ktcloud] Not required argument \'accesscontrolgroupids\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateInstanceAccessControlGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def startInstance(**kargs):
    """ start Database Instance
    * Args :
        - instanceid(String, Required) : instanceid
    * Examples : print(db.startInstance(zone='KR-M', instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'startInstance'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def restartInstance(**kargs):
    """ Restart Database Instance
    * Args :
        - instanceid(String, Required) : instanceid
    * Examples : print(db.restartInstance(zone='KR-M', instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'restartInstance'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteInstance(**kargs):
    """ delete Database Instance
    * Args :
        - instanceid(String, Required) : instanceid
    * Examples :
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'deleteInstance'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createParameterGroup(**kargs):
    """ Create Database ParameterGroup
    * Args :
        - sourceparametergroupid(String, Required) : source parametergroupid
        - parametergroupname(String, Required) : source parametergroupname
    * Examples : print(db.createParameterGroup(zone='KR-M', sourceparametergroupid='11', parametergroupname='mytest'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'sourceparametergroupid' in kargs:
        return '[ktcloud] Not required argument \'sourceparametergroupid\' '
    if not 'parametergroupname' in kargs:
        return '[ktcloud] Not required argument \'parametergroupname\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'createParameterGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listParameterGroupEntries(**kargs):
    """ Database ParameterGroup Entries List
    * Args :
        - parametergroupid(String, Required) : source parametergroupid
    * Examples : print(db.listParameterGroupEntries(parametergroupid='11'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'parametergroupid' in kargs:
        return '[ktcloud] Not required argument \'parametergroupid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listParameterGroupEntries'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listParameterGroups(**kargs):
    """ Database Parameter Group List
    * Args : None
    * Examples : print(db.listParameterGroups())
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listParameterGroups'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteParameterGroup(**kargs):
    """ Delete Database Parameter Group
    * Args :
        - parametergroupid(String, Required) : source parametergroupid
    * Examples : print(db.deleteParameterGroup(parametergroupid='21d6a82f-7eb1-4889-bd2e-6c761320ae39'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'parametergroupid' in kargs:
        return '[ktcloud] Not required argument \'parametergroupid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'deleteParameterGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listEvents(**kargs):
    """ Database Event List
    * Args :
        - starttime(String, Required) : starttime
    * Examples : print(db.listEvents(starttime='2021-01-01 13:00'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'starttime' in kargs:
        return '[ktcloud] Not required argument \'starttime\' (yyyy-MM-DD HH:mm)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listEvents'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def recoverFromBackup(**kargs):
    """ Database Event List
    * Args :
        - instanceid(String, Required) : instanceid
        - newinstancename(String, Required) : new instance name
        - timetorecover(String, Required) : recovery time
    * Examples : print(db.recoverFromBackup(instanceid='94699dfe-f3f9-4867-8fe7-14b5298792ce', newinstancename='sdktestback', timetorecover='2021-01-08 01:42:00'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'newinstancename' in kargs:
        return '[ktcloud] Not required argument \'newinstancename\' '
    if not 'timetorecover' in kargs:
        return '[ktcloud] Not required argument \'timetorecover\' (yyyy-MM-DD HH:mm:ss)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'recoverFromBackup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createReplicationGroup(**kargs):
    """ Create Database Replication Group and Replica
    * Args :
        - instanceid(String, Required) : instanceid
        - slavecount(String, Required) : count of replication (0~2)
    * Examples : # print(db.createReplicationGroup(instanceid='30f187f5-caa4-43e2-b169-d7b6dc2abd5f', slavecount='1'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'slavecount' in kargs:
        return '[ktcloud] Not required argument \'slavecount\' (0~2)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'createReplicationGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createReplicationGroupMultiZone(**kargs):
    """ Make Database copy from mainzone to remote zone
    * Args :
        - instancename(String, Required) : instancename
        - storagesize(String, Required) : storagesize
        - perfclass(String, Required) : perfclass
        - maintenanceweekday(String, Required) : maintenanceweekday
        - parametergroupid(String, Required) : parametergroupid
        - dbmastername(String, Required) : dbmastername
        - dbmasterpassword(String, Required) : dbmasterpassword
        - dbname(String, Required) : dbname
        - dbengineversion(String, Required) : dbengineversion
        - mainzone(String, Required) : mainzone
        - remotezone(String, Required) : remotezone
        - usageplantype(String, Required) : usageplantype
    * Examples : print(db.createReplicationGroupMultiZone(instancename='sdktestmca', storagesize='80', perfclass='1x1', maintenanceweekday='sun', parametergroupid='11', dbmastername='AAtest123', dbmasterpassword='abcd1234', dbname='AATest123', dbengineversion='5.5.27', mainzone='KR-M', remotezone='KR-CA', usageplantype='monthly'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'instancename' in kargs:
        return '[ktcloud] Not required argument \'instancename\' '
    if not 'storagesize' in kargs:
        return '[ktcloud] Not required argument \'storagesize\' '
    if not 'perfclass' in kargs:
        return '[ktcloud] Not required argument \'perfclass\' (CPU x MEM)'
    if not 'maintenanceweekday' in kargs:
        return '[ktcloud] Not required argument \'maintenanceweekday\' '
    if not 'parametergroupid' in kargs:
        return '[ktcloud] Not required argument \'parametergroupid\' '
    if not 'dbmastername' in kargs:
        return '[ktcloud] Not required argument \'dbmastername\' '
    if not 'dbmasterpassword' in kargs:
        return '[ktcloud] Not required argument \'dbmasterpassword\' '
    if not 'dbname' in kargs:
        return '[ktcloud] Not required argument \'dbname\' '
    if not 'dbengineversion' in kargs:
        return '[ktcloud] Not required argument \'dbengineversion\' '
    if not 'mainzone' in kargs:
        return '[ktcloud] Not required argument \'mainzone\' '
    if not 'remotezone' in kargs:
        return '[ktcloud] Not required argument \'remotezone\' '
    if not 'usageplantype' in kargs:
        return '[ktcloud] Not required argument \'usageplantype\' '
    ZoneName = kargs['mainzone']
    del kargs['mainzone']
    kargs['mainzone'] = c.getzonesnamebyhname(ZoneName)
    print(kargs['mainzone'])
    M2Bool = c.IsM2(ZoneName)
    ZoneName = kargs['remotezone']
    del kargs['remotezone']
    kargs['remotezone'] = c.getzonesnamebyhname(ZoneName)
    print(kargs['remotezone'])
    baseurl = c.geturl(ctype='database', m2=M2Bool)

    kargs['command'] = 'createReplicationGroupMultiZone'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listReplicationGroups(**kargs):
    """ Database Replication Group List
    * Args : None
    * Examples : print(db.listReplicationGroups())
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listReplicationGroups'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateReplicationGroupSlaveCount(**kargs):
    """ Change count of Database Replica
    * Args :
        - replicationgroupid(String, Required) : replicationgroupid
        - slavecount(String, Required) : slavecount 0~2
    * Examples : print(db.updateReplicationGroupSlaveCount(replicationgroupid='30f187f5-caa4-43e2-b169-d7b6dc2abd5f', slavecount='0'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'replicationgroupid' in kargs:
        return '[ktcloud] Not required argument \'replicationgroupid\' '
    if not 'slavecount' in kargs:
        return '[ktcloud] Not required argument \'slavecount\' (0~2)'
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateReplicationGroupSlaveCount'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteReplicationGroup(**kargs):
    """ Delete Database Replica Group
    * Args :
        - replicationgroupid(String, Required) : replicationgroupid
    * Examples : print(db.deleteReplicationGroup(replicationgroupid='30f187f5-caa4-43e2-b169-d7b6dc2abd5f'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'replicationgroupid' in kargs:
        return '[ktcloud] Not required argument \'replicationgroupid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'deleteReplicationGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createHaGroup(**kargs):
    """ Create Database HA Group
    * Args :
        - instanceid(String, Required) : instanceid
        - slavecount(String, Required) : slavecount 0~1
        - hamode(String, Required) : auto hamode Y or N
        - semisync(String, Required) : semisync Y or N
        - hagroupname(String, Required) : hagroupname
    * Examples : print(db.createHaGroup(instanceid='8ab079df-ca71-4f0f-aee6-b4db482fc4c1', slavecount='1', hamode='Y', semisync='N', hagroupname='hatest15'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'instanceid' in kargs:
        return '[ktcloud] Not required argument \'instanceid\' '
    if not 'slavecount' in kargs:
        return '[ktcloud] Not required argument \'slavecount\' (0~1)'
    if not 'hamode' in kargs:
        return '[ktcloud] Not required argument \'hamode\' (Y or N)'
    if not 'semisync' in kargs:
        return '[ktcloud] Not required argument \'semisync\' (Y or N)'
    if not 'hagroupname' in kargs:
        return '[ktcloud] Not required argument \'hagroupname\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'createHaGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createHaGroupSingleZone(**kargs):
    """ Create Database HA Group in single zone
    * Args :
        - instancename(String, Required) : instancename
        - storagesize(String, Required) : storagesize
        - perfclass(String, Required) : perfclass (CPU x MEM)
        - maintenanceweekday(String, Required) : maintenanceweekday
        - parametergroupid(String, Required) : parametergroupid
        - dbmastername(String, Required) : dbmastername
        - dbmasterpassword(String, Required) : dbmasterpassword
        - dbname(String, Required) : dbname
        - dbengineversion(String, Required) : dbengineversion
        - mainzone(String, Required) : mainzone
        - remotezone(String, Required) : remotezone
        - usageplantype(String, Required) : usageplantype
        - hamode(String, Required) : hamode
        - backupretention(String, Required) : backupretention
        - semisync(String, Required) : semisync
        - hagroupname(String, Required) : hagroupname
    * Examples : print(db.createHaGroupSingleZone(instancename='sdktest5', storagesize='80', perfclass='1x1', maintenanceweekday='sun', parametergroupid='21', dbmastername='AAtest123', dbmasterpassword='abcd1234', dbname='AATest123', dbengineversion='5.6.24', mainzone='KR-M', remotezone='KR-M', usageplantype='monthly', hamode='Y', backupretention='2', semisync='N', hagroupname='hatest1))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'instancename' in kargs:
        return '[ktcloud] Not required argument \'instancename\' '
    if not 'storagesize' in kargs:
        return '[ktcloud] Not required argument \'storagesize\' '
    if not 'perfclass' in kargs:
        return '[ktcloud] Not required argument \'perfclass\' (CPU x MEM)'
    if not 'maintenanceweekday' in kargs:
        return '[ktcloud] Not required argument \'maintenanceweekday\' '
    if not 'parametergroupid' in kargs:
        return '[ktcloud] Not required argument \'parametergroupid\' '
    if not 'dbmastername' in kargs:
        return '[ktcloud] Not required argument \'dbmastername\' '
    if not 'dbmasterpassword' in kargs:
        return '[ktcloud] Not required argument \'dbmasterpassword\' '
    if not 'dbname' in kargs:
        return '[ktcloud] Not required argument \'dbname\' '
    if not 'dbengineversion' in kargs:
        return '[ktcloud] Not required argument \'dbengineversion\' '
    if not 'mainzone' in kargs:
        return '[ktcloud] Not required argument \'mainzone\' '
    if not 'remotezone' in kargs:
        return '[ktcloud] Not required argument \'remotezone\' '
    if not 'usageplantype' in kargs:
        return '[ktcloud] Not required argument \'usageplantype\' '
    if not 'hamode' in kargs:
        return '[ktcloud] Not required argument \'hamode\' '
    if not 'backupretention' in kargs:
        return '[ktcloud] Not required argument \'backupretention\' '
    if not 'semisync' in kargs:
        return '[ktcloud] Not required argument \'semisync\' '
    if not 'hagroupname' in kargs:
        return '[ktcloud] Not required argument \'hagroupname\' '
    baseurl = c.geturl(ctype='database', m2=False)

    ZoneName = kargs['mainzone']
    del kargs['mainzone']
    kargs['mainzone'] = c.getzonesnamebyhname(ZoneName)
    # print(kargs['mainzone'])
    M2Bool = c.IsM2(ZoneName)
    ZoneName = kargs['remotezone']
    del kargs['remotezone']
    kargs['remotezone'] = c.getzonesnamebyhname(ZoneName)
    # print(kargs['remotezone'])
    kargs['command'] = 'createHaGroupSingleZone'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listHaGroups(**kargs):
    """ Database HA Group List
    * Args : None
    * Examples : print(db.listHaGroups())
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listHaGroups'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateHaMode(**kargs):
    """ Change Database HA mode
    * Args :
        - hagroupid(String, Required) : hagroupid
        - hamode(String, Required) : hamode Y or N
    * Examples : print(db.updateHaMode(hagroupid='d1df63a3-a0c9-4e18-87c0-a804a0f2bf23', hamode='Y'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateHaMode'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateHaSemiSync(**kargs):
    """ Change Database HA SemiSync
    * Args :
        - hagroupid(String, Required) : hagroupid
        - semisync(String, Required) : semisync Y or N
    * Examples : print(db.updateHaSemiSync(hagroupid='d1df63a3-a0c9-4e18-87c0-a804a0f2bf23', semisync='N'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateHaSemiSync'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateHaGroupSlaveCount(**kargs):
    """ Change Database HA count of Slave
    * Args :
        - hagroupid(String, Required) : hagroupid
        - slavecount(String, Required) : slavecount 1~2
    * Examples : print(db.updateHaGroupSlaveCount(hagroupid='d1df63a3-a0c9-4e18-87c0-a804a0f2bf23', slavecount='1'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'updateHaGroupSlaveCount'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteHaGroup(**kargs):
    """ Change Database HA count of Slave
    * Args :
        - hagroupid(String, Required) : hagroupid
    * Examples : print(db.deleteHaGroup(hagroupid='d1df63a3-a0c9-4e18-87c0-a804a0f2bf23'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'deleteHaGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createAccessControlGroup(**kargs):
    """ Create Access Control Group
    * Args :
        - accesscontrolgroupname(String, Required) : accesscontrolgroup name
        - accesscontrolentries(String, Required) : Allow IP CIDR
    * Examples : print(db.createAccessControlGroup(accesscontrolgroupname='MyTest', accesscontrolentries='192.168.100.129/24'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'accesscontrolgroupname' in kargs:
        return '[ktcloud] Not required argument \'accesscontrolgroupname\' '
    if not 'accesscontrolentries' in kargs:
        return '[ktcloud] Not required argument \'accesscontrolentries\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'createAccessControlGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteAccessControlGroup(**kargs):
    """ Create Access Control Group
    * Args :
        - accesscontrolgroupid(String, Required) : accesscontrolgroup ID
    * Examples :
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'accesscontrolgroupid' in kargs:
        return '[ktcloud] Not required argument \'accesscontrolgroupid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'deleteAccessControlGroup'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listAccessControlGroups(**kargs):
    """ Create Access Control Group
    * Args : None
    * Examples : print(db.listAccessControlGroups())
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listAccessControlGroups'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listAccessControlGroupEntries(**kargs):
    """ Create Access Control Group
    * Args :
        - accesscontrolgroupid(String, Required) : accesscontrolgroup ID
    * Examples : print(db.listAccessControlGroups())
    * Ref :  https://cloud.kt.com/portal/openapi-guide/database-ucloudDB-Instance
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'accesscontrolgroupid' in kargs:
        return '[ktcloud] Not required argument \'accesscontrolgroupid\' '
    baseurl = c.geturl(ctype='database', m2=False)

    kargs['command'] = 'listAccessControlGroupEntries'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)
#EOF