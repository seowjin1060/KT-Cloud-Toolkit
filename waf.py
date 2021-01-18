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


def createWAF(**kargs):
    """ Create a new KT Cloud WAF.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required): WAF Name(max.63 length, english+(english,number,'-'))
        - type(String, Required): compositon[ single | dual ] 
        - spec(String, Required): specification, select[ basic | standard | advanced | premiun ]
        - waf1consoleport(String, Required): WAF1 VM console connection port (5950~5999)
        - waf1sshport(String, Required): WAF1 VM ssh connection port (5950~5999)
        - waf1dbport(String, Required): WAF1 VM DB connection port (5950~5999)
    * Examples: print(waf.createWAF( zone='KR-CA', name='sdktest3', type='single', spec='standard', waf1consoleport='5997', waf1sshport='5998', waf1dbport='5999'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument "name" '
    if not 'type' in kargs:
        return '[ktcloud] Missing required argument "type" '
    if not 'spec' in kargs:
        return '[ktcloud] Missing required argument "spec" '
    if not 'waf1consoleport' in kargs:
        return '[ktcloud] Missing required argument "waf1consoleport" '
    if not 'waf1sshport' in kargs:
        return '[ktcloud] Missing required argument "waf1sshport" '
    if not 'waf1dbport' in kargs:
        return '[ktcloud] Missing required argument "waf1dbport" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)
    
    kargs['command'] = 'createWAF'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listWAFs(**kargs):
    """ List the KT Cloud WAFs.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(waf.listWAFs(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)

    kargs['command'] = 'listWAFs'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest_debug(kargs, baseurl, my_secretkey)


def deleteWAF(**kargs):
    """ Delete a KT Cloud WAF.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): WAF ID
    * Examples: print(waf.deleteWAF(zone='KR-M', id='3105'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument "id" (waf id)'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)

    kargs['command'] = 'deleteWAF'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def addWAFWebServer(**kargs):
    """ Add a WebServer to protect by KT Cloud WAF.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): WAF ID
        - vmid(String, Required): virtualmachine ID
        - webserverport(String, Required): web server service port
        - proxyport1(String, Required): RVM to WAF VM1 connection port
        - sslmode(String, Required): select[ disabled | sslthru | sslterm ]
        - proxyport2(String, Optional): (Dual Product) RVM to WAF VM2 connection port
        - loadbalancerid(String, Optional): (Single Product) RVM to LB connection loadbalancerID
    * Examples:
        - waf.addWAFWebServer(id='3046', zoneid='95e2f517-d64a-4866-8585-5177c256f7c7', virtualmachineid='4930ed0f-2967-11eb-891c-90e2bad10000', webserverport='80', proxyport1='80', proxyport2='81', sslmode='disabled')
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument "id" '
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument "vmid" '
    if not 'webserverport' in kargs:
        return '[ktcloud] Missing required argument "webserverport" '
    if not 'proxyport1' in kargs:
        return '[ktcloud] Missing required argument "proxyport1" '
    if not 'sslmode' in kargs:
        return '[ktcloud] Missing required argument "sslmode" (disabled | sslthru | sslterm)'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)

    kargs['command'] = 'addWAFWebServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listWAFWebServers(**kargs):
    """ List the WebServers to protect by KT Cloud WAF.
    * Args:
        - id(String, Required): WAF ID
        - zone(String, Optional) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples: print(waf.listWAFWebServers(zone='KR-M2', id='3108'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)

    kargs['command'] = 'listWAFWebServers'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def removeWAFWebServer(**kargs):
    """ Remove a WebServer to protect by KT Cloud WAF.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): WAF ID
        - webserverid(String, Required): webserver ID. see listWAFWebServers
    * Examples: print(waf.removeWAFWebServer(zone='KR-M', id='3107', webserverid='8802'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument "id" '
    if not 'webserverid' in kargs:
        return '[ktcloud] Missing required argument "webserverid '
    if 'zone' in kargs:
        ZoneName = kargs['zone']
        del kargs['zone']
        kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
        M2Bool = c.IsM2(ZoneName)
        baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)
    else:
        baseurl = c.geturl(ctype='waf', m2=False)

    kargs['command'] = 'removeWAFWebServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def addWAFWebSite(**kargs):
    """ Add a WebSite to protect by KT Cloud WAF.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): WAF ID
        - sitename(String, Required): site name or IP
        - port(String, Required): service port
        - policynum(String, Required): security policy, select[ 0: standard | 1: basic | 2: detection only| 3: pass ]
    * Examples: print(waf.addWAFWebSite(zone='KR-M', id='3107', sitename='test.com', port='80', policynum='0'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" '
    if not 'sitename' in kargs:
        return '[ktcloud] Missing required argument \"sitename\" '
    if not 'port' in kargs:
        return '[ktcloud] Missing required argument \"port\" '
    if not 'policynum' in kargs:
        return '[ktcloud] Missing required argument \"policynum\" (0: standard | 1: basic | 2: detection only| 3: pass) '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)

    kargs['command'] = 'addWAFWebSite'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listWAFWebSites(**kargs):
    """ List the WebSites to protect by KT Cloud WAF.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): WAF ID
        - websiteid(String, Required): Website ID
    * Examples: print(waf.removeWAFWebSite(zone='KR-M', id='3108', websiteid='7658'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)

    kargs['command'] = 'listWAFWebSites'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def removeWAFWebSite(**kargs):
    """ Remove a WebSite to protect by KT Cloud WAF.
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required): WAF ID
        - websiteid(String, Required): website ID. see listWAFWebSites (waf_websvc_seq)
    * Examples: print(waf.removeWAFWebSite(zone='KR-M', id='3107', websiteid='7657'))
    """
    my_apikey, my_secretkey = c.read_config()
    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument "id" '
    if not 'websiteid' in kargs:
        return '[ktcloud] Missing required argument "websiteid '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype = 'waf', m2 = M2Bool)

    kargs['command'] = 'removeWAFWebSite'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)
# END of File