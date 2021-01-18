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


def addVolume(**kargs):
    """ Add a new Volume for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required): Volume Name
        - path(String, Required): Volume mount point(English, number, ‘_’ , max. 20 length), ex) nas_1, nas2
        - totalsize(String, Required): Volume Size(GB) : decimal point not supported, min:500/ max:20000(changable)
        - volumetype(String, Required): select[ nfs | cifs ]
        - zoneid(String, Required): Volume zoneid, checkable by server API(listZones)
        - volumetype(String, M2-Required): [KOR-SEOUL M2 zone only]file storage[ nfs | cifs ], block storage(iscsi), select[ nfs | cifs | iscsi ]
    * Examples: print(nas.addVolume(zone='KR-M', name='carrier', path='nas_1', totalsize='1000', volumetype='nfs'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument "name" '
    if not 'path' in kargs:
        return '[ktcloud] Missing required argument "path" '
    if not 'totalsize' in kargs:
        return '[ktcloud] Missing required argument "totalsize" '
    if not 'volumetype' in kargs:
        return '[ktcloud] Missing required argument "volumetype" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'addVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listVolumes(**kargs):
    """List Volumes for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(nas.listVolumes(zone='KR-M'))
    """
    import time
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'listVolumes'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateVolume(**kargs):
    """Update Volume for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): Volume ID
        - totalsize(String, Required): Volume size(GB) : decimal point not supported. min:500/ max:20000(changable)
        - name(String, Optional): Volume name
        - description(String, Optional): Volume description
    * Examples: print(nas.updateVolume(zone='KR-M', id='1234', totalsize='1000', name='test' ))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (NAS Volume id)'
    if not 'totalsize' in kargs:
        return '[ktcloud] Missing required argument \"totalsize\" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'updateVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteVolume(**kargs):
    """Delete Volume for KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): Volume ID
    * Examples: print(nas.deleteVolume(zone='KR-M', id='1234'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument "id" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'deleteVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def getVolumeUsage(**kargs):
    """Get Volume Uasge for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): Volume ID
    * Examples: print(nas.getVolumeUsage(zone='KR-M', id='1234'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument "id" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'getVolumeUsage'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def addAccountForNas(**kargs):
    """Add Cifs Account for the KT Cloud NAS(MAX. 10EA).
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - cifsid(String, Required): CIFS name(6 ~ 20 length, English & number combination)
        - cifspw(String, Required): CIFS password(8 ~ 14 length, combination of English & number & (! @ # $ ?))
        - cifsworkgroup(String, Required): WorkGroup
    * Examples: nas.addCifsAccount(cifsid='jintest99', cifspw='vhxkf!21213')
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'cifsid' in kargs:
        return '[ktcloud] Missing required argument "cifsid" '
    if not 'cifspw' in kargs:
        return '[ktcloud] Missing required argument "cifspw" '
    # if not 'cifsworkgroup' in kargs:
    #     return '[ktcloud] Missing required argument "cifsworkgroup" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'addAccountForNas'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listCifsAccounts(**kargs):
    """List Cifs Accounts for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(nas.listCifsAccounts(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'listCifsAccounts'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def addCifsAccount(**kargs):
    """Add Cifs Account for the KT Cloud NAS(MAX. 10EA).
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - cifsid(String, Required): CIFS name(6 ~ 20 length, English & number combination)
        - cifspw(String, Required): CIFS password(8 ~ 14 length, combination of English & number & (! @ # $ ?))
        - accountid(String, Required): CloudStack Account ID(NAS1.0)
        - volumeid(String, Required): CIFS volume ID(NAS2.0)
    * Examples: print(nas.listCifsAccounts(zone='KR-M', cifsId='mytest123', cifsPw='test!13579', accountId='46616224-c207-4008-937e-a3ea504ae580'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'cifsId' in kargs:
        return '[ktcloud] Missing required argument "cifsId" '
    if not 'cifsPw' in kargs:
        return '[ktcloud] Missing required argument "cifsPw" '
    if not 'accountId' in kargs and not 'volumeId' in kargs:
        return '[ktcloud] Missing required argument \"accountId or volumeId\" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'addCifsAccount'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateCifsAccount(**kargs):
    """Update Cifs Account password for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - cifsId(String, Required): CIFS name(6 ~ 20 length, english & number combination)
        - cifsPw(String, Required): CIFS password(8 ~ 14 length, combination of english & number & (! @ # $ ?))
    * Examples: print(nas.updateCifsAccount(zone='KR-M', cifsId='mytest123', cifsPw='test!135790'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'cifsId' in kargs:
        return '[ktcloud] Missing required argument "cifsId" '
    if not 'cifsPw' in kargs:
        return '[ktcloud] Missing required argument "cifsPw" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'updateCifsAccount'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteCifsAccount(**kargs):
    """Delete Cifs Accounts for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - cifsId(String, Required): CIFS name
    * Examples: print(nas.deleteCifsAccount(zone='KR-M', cifsId='mytest123'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'cifsId' in kargs:
        return '[ktcloud] Missing required argument "cifsId" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'deleteCifsAccount'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def snapshotVolume(**kargs):
    """Create Snapshot of Volume for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - volumeid(String, Required): volume ID
        - name(String, Required): volume name
    * Examples: print(nas.snapshotVolume(zone='KR-M', volumeid='8359', name='mytest'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'volumeid' in kargs:
        return '[ktcloud] Missing required argument "volumeid" '
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument "name" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'snapshotVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def restoreSnapshot(**kargs):
    """Restore Snapshot of Volume for the KT Cloud NAS.
       After restoring, the Snapshot of Volume will be deleted
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - volumeid(String, Required): volume ID
        - name(String, Required): volume name
    * Examples: print(nas.restoreSnapshot(zone='KR-M', volumeid='8359', name='mytest'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'volumeid' in kargs:
        return '[ktcloud] Missing required argument "volumeid" '
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument "name" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'restoreSnapshot'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteSnapshot(**kargs):
    """Delete Snapshot of Volume for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - volumeid(String, Required): volume ID
        - name(String, Required): volume name
    * Examples: print(nas.deleteSnapshot(zone='KR-M', volumeid='8359', name='mytest'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'volumeid' in kargs:
        return '[ktcloud] Missing required argument "volumeid" '
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument "name" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'deleteSnapshot'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def scheduleSnapshot(**kargs):
    """Schedule Snapshot of Volume for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - volumeid(String, Required): volume ID
          * Required 1~4 of below 4 optons
        - weekmaxcount(String, Optional): max. count of creating snapshot per week(sunday midnight)
        - daymaxcount(String, Optional): max. snapshot count(max. 150EA)
        - activate(bool, Optional): activate snapshot. true or false
        - snapshottime(String, Optional): snapshot hour, ex) 1, 2, 10
    * Examples: print(nas.scheduleSnapshot(zone='KR-M', volumeid='8359', weekmaxcount='5', daymaxcount='2', activate='false', snapshottime='11'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)
    if not M2Bool:
        if not 'weekmaxcount' in kargs and not 'daymaxcount' in kargs and \
            not 'activate' in kargs and not 'snapshottime' in kargs:
            return '[ktcloud] Missing required argument \"weekmaxcount or daymaxcount or activate or snapshottime\" '
    kargs['command'] = 'scheduleSnapshot'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listSnapshots(**kargs):
    """List Snapshot of Volume for the KT Cloud NAS.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(nas.listSnapshots(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'listSnapshots'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listNetworks(**kargs):
    """List the KT Cloud Networks.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - networkid(String, Optinal): Network uuid
    * Examples: print(nas.listNetworks(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='nas', m2=M2Bool)

    kargs['command'] = 'listNetworks'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)
#EOF