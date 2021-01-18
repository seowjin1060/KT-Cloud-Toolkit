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


def createLoadBalancer(**kargs):
    """ Create a new KT Cloud LoadBalancer.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required): loadbalancer Name
        - loadbalanceroption(String, Required): select[ roundrobin | leastconnection | leastresponse | sourceiphash | srcipsrcporthash ]
        - serviceport(String, Required): service port
        - servicetype(String, Required): select[ https | http | sslbridge | tcp | ftp ]
        - healthchecktype(String, Required): select[http | https | tcp]
        - healthcheckurl(String, Optional): URL when Health Check type is HTTP/HTTPS
    * Examples: print(lb.createLoadBalancer(zone='KR-M', name='testlbkk2', loadbalanceroption='roundrobin', serviceport='80', servicetype='tcp', healthchecktype='tcp'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument "name" '
    if not 'loadbalanceroption' in kargs:
        return '[ktcloud] Missing required argument "loadbalanceroption" (roundrobin or leastconnection or leastresponse or sourceiphash or srcipsrcporthash)'
    if not 'serviceport' in kargs:
        return '[ktcloud] Missing required argument "serviceport" '
    if not 'servicetype' in kargs:
        return '[ktcloud] Missing required argument "servicetype" '
    if not 'healthchecktype' in kargs:
        return '[ktcloud] Missing required argument "healthchecktype" '
    if kargs['healthchecktype'].lower() == 'http' or kargs['healthchecktype'].lower() == 'https':
        if not 'healthcheckurl' in kargs:
            return '[ktcloud] Missing required argument "healthcheckurl" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'createLoadBalancer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listLoadBalancers(**kargs):
    """ List the KT Cloud LoadBalancers.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(lb.listLoadBalancers(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'listLoadBalancers'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateLoadBalancer(**kargs):
    """ Update a KT Cloud LoadBalancer.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - loadbalancerid(String, Required): loadbalancer ID
        - loadbalanceroption(String, Required): select[ roundrobin | leastconnection | leastresponse | sourceiphash| srcipsrcporthash ]
        - servicetype(String, Optional): select[https | http | sslbridge | tcp | ftp]
        - healthchecktype(String, Optional): select[http | https | tcp]
        - healthcheckurl(String, Optional): URL(for Health Check type = HTTP/HTTPS)
    * Examples: print(lb.updateLoadBalancer(zone='KR-M', loadbalancerid='19870', loadbalanceroption='roundrobin', servicetype='http', healthchecktype='http', healthcheckurl='http://test11.com'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'loadbalancerid' in kargs:
        return '[ktcloud] Missing required argument \"loadbalancerid\" '
    if not 'loadbalanceroption' in kargs:
        return '[ktcloud] Missing required argument \"loadbalanceroption\" (roundrobin or leastconnection or leastresponse or sourceiphash or srcipsrcporthash)'
    if kargs['healthchecktype'].lower() == 'http' or kargs['healthchecktype'].lower() == 'https':
        if not 'healthcheckurl' in kargs:
            return '[ktcloud] Missing required argument "healthcheckurl" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'updateLoadBalancer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteLoadBalancer(**kargs):
    """ Delete a KT Cloud LoadBalancer.
        Related portforwarding rules will not be deleted.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - loadbalancerid(String, Required): LoadBalancer ID
    * Examples: print(lb.deleteLoadBalancer(zone='KR-M', loadbalancerid='19870'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'loadbalancerid' in kargs:
        return '[ktcloud] Missing required argument "loadbalancerid" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'deleteLoadBalancer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def checkLoadBalancerName(**kargs):
    """ Check the duplication of KT Cloud LoadBalancer name.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required): loadbalancer Name
    * Examples: print(lb.checkLoadBalancerName(zone='KR-M', name='testlbkk1'))
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
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'checkLoadBalancerName'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def usageLoadBalancerService(**kargs):
    """ Check the duplication of KT Cloud LoadBalancer name.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - startdt(String, Required): start time to search (YYYY-MM-DD)
        - enddt(String, Required): end time to search (YYYY-MM-DD)
        - lbname(String, Optional): loadbalancer Name
    * Examples: print(lb.usageLoadBalancerService(zone='KR-M', lbname='testlb001', startdt='2020-11-01', enddt='2020-12-01'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    # if not 'name' in kargs:
    #     return '[ktcloud] Missing required argument "name" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'usageLoadBalancerService'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def addLoadBalancerWebServer(**kargs):
    """ add a WebServer to load balance by KT Cloud LoadBalancer.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - loadbalancerid(String, Required): loadbalancer ID
        - virtualmachineid(String, Required): webserver ID
        - ipaddress(String, Required): webserver public IP
        - publicport(String, Required): webserver public port
    * Examples: print(lb.addLoadBalancerWebServer(zone='KR-M', loadbalancerid='19871', vmid='47d2ea4c-d434-418b-a854-c99054abeff7', ipaddress='1.1.1.1', publicport='80' ))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument "vmid" '
    if not 'ipaddress' in kargs:
        return '[ktcloud] Missing required argument "ipaddress" '
    if not 'publicport' in kargs:
        return '[ktcloud] Missing required argument "publicport" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']

    kargs['command'] = 'addLoadBalancerWebServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listLoadBalancerWebServers(**kargs):
    """ List the WebServers to load balance by KT Cloud LoadBalancer.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - loadbalancerid(String, Required): loadbalancer ID
    * Examples: print(lb.listLoadBalancerWebServers(zone='KR-M', loadbalancerid='19871'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'loadbalancerid' in kargs:
        return '[ktcloud] Missing required argument "loadbalancerid" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'listLoadBalancerWebServers'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def removeLoadBalancerWebServer(**kargs):
    """ Remove a WebServer to load balance by KT Cloud LoadBalancer.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - serviceid(String, Required): Service ID
    * Examples: print(lb.removeLoadBalancerWebServer(zone='KR-M', serviceid='187983'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'serviceid' in kargs:
        return '[ktcloud] Missing required argument "serviceid" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'removeLoadBalancerWebServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createTag(**kargs):
    """ Create Tag to load balance by KT Cloud LoadBalancer.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - loadbalancerid(String, Required): Loadbalancer ID
        - tag(String, Required): tag string
    * Examples: print(lb.createTag(zone='KR-M', loadbalancerid='19871', tag='just_test' ))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'loadbalancerid' in kargs:
        return '[ktcloud] Missing required argument "loadbalancerid" '
    if not 'tag' in kargs:
        return '[ktcloud] Missing required argument "tag" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'createTag'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteTag(**kargs):
    """ Delete Tag to load balance by KT Cloud LoadBalancer.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - loadbalancerid(String, Required): Loadbalancer ID
    * Examples: print(lb.createTag(zone='KR-M', loadbalancerid='19871', tag='just_test' ))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'loadbalancerid' in kargs:
        return '[ktcloud] Missing required argument "loadbalancerid" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='loadbalancer', m2=M2Bool)

    kargs['command'] = 'deleteTag'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)
#EOF