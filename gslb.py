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


def addGslbServer(**kargs):
    """ Add a new the KT Cloud GSLB.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - svrNm(String, Required): GSLB name, ex)GSLB1
        - domainNm(String, Required): Domain(CNAME) information,format: {domainNm}.g.ucloudbiz.com, ex)test.g.ucloudbiz.com
        - persistence(String, Required): select[none | use], after ttl expired, Select whether to inform the same IP for the Domain or not
        - ttl(nunber, Required): select[ 30 | 60 | 900 | 1800 | 3600 ](basic: 30), retention time of DNS for information offered by GSLB
    * Examples: print(gslb.addGslbServer(zone='KR-M', svrNm='mytest1234', domainNm='test1234.g.ucloudbiz.com', persistence='use', ttl='30'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'svrNm' in kargs:
        return '[ktcloud] Missing required argument "svrNm" (GSLB name)'
    if not 'domainNm' in kargs:
        return '[ktcloud] Missing required argument "domainNm" ({domainNm}.g.ucloudbiz.com)'
    if not 'persistence' in kargs:
        return '[ktcloud] Missing required argument "persistence" (none | use)'
    if not 'ttl' in kargs:
        return '[ktcloud] Missing required argument "ttl" (30 | 60 | 900 | 1800 | 3600)'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='gslb', m2=M2Bool)

    kargs['command'] = 'addGslbServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def checkGslbName(**kargs):
    """ Check duplication of the KT Cloud GSLB name.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required): GSLB name, ex)Testgslb1
    * Examples: print(gslb.checkGslbName(zone='KR-M', name='mytest1234'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument "name" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='gslb', m2=M2Bool)

    kargs['command'] = 'checkGslbName'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listGslbServer(**kargs):
    """ List the Servers of KT Cloud GSLB.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(gslb.listGslbServer(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='gslb', m2=M2Bool)

    kargs['command'] = 'listGslbServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteGslbServer(**kargs):
    """ Delete a KT Cloud GSLB Server.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - svrNm(String, Required): GSLB name, ex)GSLB1
    * Examples: print(gslb.deleteGslbServer(zone='KR-M', svrNm='mytest123'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'svrNm' in kargs:
        return '[ktcloud] Missing required argument "svrNm" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='gslb', m2=M2Bool)

    kargs['command'] = 'deleteGslbServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def addGslbService(**kargs):
    """ Add a KT Cloud GSLB Service Information(IP).
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - svrNm(String, Required): GSLB name, ex)GSLB1
        - ip(String, Required): service IP address
        - port(String, Required): service port
        - opType(String, Required): service action, select[ active | backup ]
        - healthCheckType(String, Required): monitoring type, select[ tcp | http ]
    * Examples: print(gslb.addGslbService(zone='KR-M', svrNm='mytest123', ip='10.10.10.10', port='80', opType='active', healthCheckType='tcp' ))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'svrNm' in kargs:
        return '[ktcloud] Missing required argument "svrNm" '
    if not 'ip' in kargs:
        return '[ktcloud] Missing required argument "ip" '
    if not 'port' in kargs:
        return '[ktcloud] Missing required argument "port" '
    if not 'opType' in kargs:
        return '[ktcloud] Missing required argument "opType" '
    if not 'healthCheckType' in kargs:
        return '[ktcloud] Missing required argument "healthCheckType" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='gslb', m2=M2Bool)

    kargs['command'] = 'addGslbService'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listGslbService(**kargs):
    """ List the Services(IPs) of KT Cloud GSLB.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(gslb.listGslbService(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='gslb', m2=M2Bool)

    kargs['command'] = 'listGslbService'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteGslbService(**kargs):
    """ Delete a KT Cloud GSLB Service Information(IP).
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - gslbsvcIpName(String, Required): GSLB service name(GSLB name, service IP, service port, backup combination)
          ex)GSLB1_1.1.1.1_80, GSLB1_1.1.1.1_80_bkup (for Back Up)
    * Examples: print(gslb.deleteGslbService(zone='KR-M', gslbsvcIpName='mytest123_10.10.10.10_80'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'gslbsvcIpName' in kargs:
        return '[ktcloud] Missing required argument "gslbsvcIpName" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='gslb', m2=M2Bool)

    kargs['command'] = 'deleteGslbService'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)
#EOF