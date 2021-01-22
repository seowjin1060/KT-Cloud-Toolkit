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


def deployVirtualMachine(**kargs):
    """ Create a new VirtualMachine(VM) 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - serviceofferingid(String, Required): Spec ID of VM. See Ref(below link).
        - templateid(String, Required): OS ID. See Ref(below link).
        - diskofferingid(String, Required): Additional Volume ID of Your VM. See Ref(below link).
            ** Choose above 3 option or this productcode option.
        - productcode(String, Required) : producttype_OStype_VMSpec code. 
    * Examples : print(server.deployVirtualMachine(zone='KR-M', serviceofferingid='f86f09f6-9acf-4b30-936c-cfb409a89e68', diskofferingid='87c0a6f6-c684-4fbe-a393-d8412bcf788d'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make
    """
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'deployVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    if not 'zone' in kargs:
        return 'Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone '
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    if 'userdata' in kargs:
        kargs['userdata'] = base64.b64encode(kargs['userdata'].encode('UTF-8'))
    if 'productcode' in kargs:
        if 'serviceofferingid' in kargs:
            return '[ktcloud] Not required argument \"serviceofferingid\"'
        if 'templateid' in kargs:
            return '[ktcloud] Not required argument \"templateid\"'
        if 'diskofferingid' in kargs:
            return '[ktcloud] Not required argument \"diskofferingid\"'
    else:
        if not 'serviceofferingid' in kargs:
            return '[ktcloud] Missing required argument \"serviceofferingid\"'
        if not 'templateid' in kargs:
            return '[ktcloud] Missing required argument \"templateid\"'
#         if not 'diskofferingid' in kargs:
#             return '[ktcloud] Missing required argument "diskofferingid"'
    return c.makerequest(kargs, baseurl, my_secretkey)


def destroyVirtualMachine(**kargs):
    """ Destroy your VirtualMachine(VM) 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required): VM id to destory. 
    * Examples : print(server.destroyVirtualMachine (zone='KR-M', id='2a40283f-148d-4144-a6ce-e042fad08109'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'destroyVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def startVirtualMachine(**kargs):
    """ Start your VirtualMachine(VM) 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required): VM id to stop. 
    * Examples : print(server.startVirtualMachine(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'startVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def stopVirtualMachine(**kargs):
    """ Stop your VirtualMachine(VM) 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required): VM id to stop. 
    * Examples : print(server.stopVirtualMachine(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'stopVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def rebootVirtualMachine(**kargs):
    """ Reboot your VirtualMachine(VM) 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required): VM id to Reboot. 
    * Examples : print(server.rebootVirtualMachine(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'rebootVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def restoreVirtualMachine(**kargs):
    """ Restore your VirtualMachine disk(VM) 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required): VM id to Restore. 
    * Examples : print(server.restoreVirtualMachine(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'restoreVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateVirtualMachine(**kargs):
    """ update your VirtualMachine displayname or haenable 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required): VM id to update. 
            ** Choose 1 of 2 option Below
        - displayname(String, Optional) : VM name
        - haenable(String, Optional) : ha enable true or false
    * Examples : print(server.updateVirtualMachine(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7', displayname='AATest123'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    if not 'displayname' in kargs and not 'haenable' in kargs:
        return '[ktcloud] Missing required argument \"VM displayname or haenable\"'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'updateVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey   
    return c.makerequest(kargs, baseurl, my_secretkey)


def createVolume(**kargs):
    """ Create your Additional Volume 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required) : Volume disk name
        - diskofferingid(String, Required) : Volume disk id. See Ref.
    * Examples : print(server.createVolume(zone='KR-M', name='AATestdisk', diskofferingid='1539f7a2-93bd-45fb-af6d-13d4d428286d'))
    * Ref :  https://cloud.kt.com/portal/openapi-guide/computing_enterprise-Server-server_api_make    
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'diskofferingid' in kargs:
        return '[ktcloud] Missing required argument \"diskofferingid\"'
    ZoneName = kargs['zone']
    del kargs['zone']
    kargs['zoneid'] = c.getzoneidbyhname(ZoneName)
    M2Bool = c.IsM2(ZoneName)
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    return c.makerequest(kargs, baseurl, my_secretkey)


def attachVolume(**kargs):
    """ attachVolume your Additional Volume to Your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required): VM id to attach volume. 
        - id(String, Required) : Volume disk ID
    * Examples : print(server.attachVolume(zone='KR-M', id='7f933f86-e8bf-4600-9423-09e8f1c84460', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (disk volume id)'
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'attachVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    return c.makerequest(kargs, baseurl, my_secretkey)


def detachVolume(**kargs):
    """ detachVolume your Additional Volume
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Volume disk ID
    * Examples : print(server.detachVolume(zone='KR-M', id='7f933f86-e8bf-4600-9423-09e8f1c84460'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (disk volume id)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)
    
    kargs['command'] = 'detachVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteVolume(**kargs):
    """ delete your Additional Volume
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Volume disk ID
    * Examples : print(server.deleteVolume(zone='KR-M', id='7f933f86-e8bf-4600-9423-09e8f1c84460'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (disk volume id)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deleteVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def resizeVolume(**kargs):
    """ resize your Additional Volume
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Volume disk ID
        - vmid(String, Required) : VM ID 
        - size(String, Required) : Volume disk Size
        - isLinux(String, Required) : Is your OS Linux or not (Y/N)
    * Examples : print(server.resizeVolume(zone='KR-M', id='83617062-0aa4-4c18-8b04-a810c2bbb597', vmid='47d2ea4c-d434-418b-a854-c99054abeff7', size='50', isLinux='Y'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (disk volume id)'
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\" '
    if not 'size' in kargs:
        return '[ktcloud] Missing required argument \"size\" (50/80/100)'
    if not 'isLinux' in kargs:
        return '[ktcloud] Missing required argument \"isLinux\" (Y/N)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'resizeVolume'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def associateIpAddress(**kargs):
    """ Get additional public IP in Selected Zone
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.associateIpAddress(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'associateIpAddress'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def disassociateIpAddress(**kargs):
    """ return additional public IP in Selected Zone
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : additional public IP ID
    * Examples : print(server.disassociateIpAddress(zone='KR-M', id='1ef85657-e5ea-4226-88e0-1ebdad98c95f'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (additional public IP id)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'disassociateIpAddress'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createPortForwardingRule(**kargs):
    """ Create PortForwarding Rule in your Selected VM & IP
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - ipaddressid(String, Required) : public IP ID
        - privateport(String, Required) : private port
        - protocol(String, Required) : TCP or UDP
        - publicport(String, Required) : public port
        - vmid(String, Required): VM id to update. 
    * Examples : print(server.createPortForwardingRule(zone='KR-M', ipaddressid='3a304bed-d7c0-4836-a31f-c4e10d2ab0be', privateport='5555', protocol='tcp', publicport='5555', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'ipaddressid' in kargs:
        return '[ktcloud] Missing required argument \"ipaddressid\" (public IP id)'
    if not 'privateport' in kargs:
        return '[ktcloud] Missing required argument \"privateport\"'
    if not 'protocol' in kargs:
        return '[ktcloud] Missing required argument \"protocol\" (TCP or UDP)'
    if not 'publicport' in kargs:
        return '[ktcloud] Missing required argument \"publicport\"'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']

    kargs['command'] = 'createPortForwardingRule'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deletePortForwardingRule(**kargs):
    """ Delete PortForwarding Rule in your Selected VM & IP
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : PortforwardingRule ID
    * Examples : print(server.deletePortForwardingRule(zone='KR-M', id='39d0a7e8-92c9-49f1-ad3d-bb7470422993'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (PortforwadingRule id)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deletePortForwardingRule'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createFirewallRule(**kargs):
    """ Create Firewall Rule in your Selected VM & IP
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - ipaddressid(String, Required) : public IP address ID
        - protocol(String, Required) : TCP or UDP or ICMP
        - startport(String, Required) : Firewall port
    * Examples : print(server.createFirewallRule(zone='KR-M', ipaddressid='3a304bed-d7c0-4836-a31f-c4e10d2ab0be', protocol='tcp', startport='1280'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'ipaddressid' in kargs:
        return '[ktcloud] Missing required argument \"ipaddressid\" '
    if not 'protocol' in kargs:
        return '[ktcloud] Missing required argument \"protocol\" '
    if not 'startport' in kargs:
        return '[ktcloud] Missing required argument \"startport\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createFirewallRule'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)

def deleteFirewallRule(**kargs):
    """ Delete Firewall Rule in your Selected VM & IP
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Firewall ID
    * Examples : print(server.deleteFirewallRule(zone='KR-M', id='9681fe5b-8c87-45ce-84cb-adf8d465ccf5'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deleteFirewallRule'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createNetwork(**kargs):
    """ Create CIP Network (Private Subnet)
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - displaytext(String, Required) : CIP name
        - account(String, Required) : User Account (Can See listVirtualMachine)
        - domainid(String, Required) : User Domain ID (Can See listVirtualMachine)
        - ipcount(String, Required) : IP (32/64/128)
    * Examples : print(server.createNetwork(zone='KR-M', displaytext='AAA22', account='EPC_M0000_S0000', domainid='849e8028-dafc-4ad6-a649-800221fdf834', ipcount='32'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'displaytext' in kargs:
        return '[ktcloud] Missing required argument \"displaytext\" '
    if not 'account' in kargs:
        return '[ktcloud] Missing required argument \"account\" (Can See listVirtualMachine)'
    if not 'domainid' in kargs:
        return '[ktcloud] Missing required argument \"domainid\" (Can See listVirtualMachine)'
    if not 'ipcount' in kargs:
        return '[ktcloud] Missing required argument \"ipcount\" (32/64/128)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createNetwork'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)

def deleteNetwork(**kargs):
    """ Delete CIP Network (Private Subnet)
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : CIP Network ID
    * Examples : print(server.deleteNetwork(zone='KR-M', id='9064d31f-430e-4021-bb48-80e2b8ae01de'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (CIP Network ID)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deleteNetwork'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def addNicToVirtualMachine(**kargs):
    """ ADD CIP Network On your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - networkid(String, Required) : CIP Network ID
        - vmid(String, Required) : Your VM ID to Add Network
    * Examples : print(server.addNicToVirtualMachine(zone='KR-M', networkid='13f92d9e-5019-4e85-82fd-148191069478', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'networkid' in kargs:
        return '[ktcloud] Missing required argument \"networkid\" (CIP Network ID)'
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'addNicToVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def removeNicFromVirtualMachine(**kargs):
    """ Remove CIP Network On your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - nicid(String, Required) : NIC ID
        - vmid(String, Required) : Your VM ID to Add Network
    * Examples : print(server.removeNicFromVirtualMachine(zone='KR-M', nicid='04bd117d-5a5c-4b0c-a3d4-88b0152112dc', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'nicid' in kargs:
        return '[ktcloud] Missing required argument \"nicid\" (Can See listVirtualMachine)'
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'removeNicFromVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createOverlay(**kargs):
    """ Create Overlay (Cloud Link)
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required) : Overlay Name
        - displaytext(String, Required) : Overlay Name
        - cidr(String, Required) : Overlay cidr
    * Examples : print(server.createOverlay(zone='KR-M', name='AAtest1', displaytext='AAtest1', cidr='192.168.8.0/22'))
    * Caution
        - C-class can only be multiples of 4
        - The following bands cannot be used
          : 172.27.x.x 172.16.x.x 10.x.x.x
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument \"name\" '
    if not 'displaytext' in kargs:
        return '[ktcloud] Missing required argument \"displaytext\" '
    if not 'cidr' in kargs:
        return '[ktcloud] Missing required argument \"cidr\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createOverlay'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listOverlays(**kargs):
    """ retur list of Overlays
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listOverlays(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listOverlays'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteOverlay(**kargs):
    """ Delete Overlay (Cloud Link)
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - overlayid(String, Required) : Overlay ID
    * Examples : print(server.deleteOverlay(zone='KR-M', overlayid='eab0b5dc-0859-4450-845e-1b930feef5ca'))
    """ 
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'overlayid' in kargs:
        return '[ktcloud] Missing required argument \"overlayid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deleteOverlay'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createSSHKeyPair(**kargs):
    """ Create SSH Key Pair
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required) : SSH Key Pair Name
    * Examples : print(server.createSSHKeyPair(zone='KR-M', name='AAATest'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument \"name\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createSSHKeyPair'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteSSHKeyPair(**kargs):
    """ Delete SSH Key Pair
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required) : SSH Key Pair Name
    * Examples : print(server.deleteSSHKeyPair(zone='KR-M', name='AAATest'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument \"name\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deleteSSHKeyPair'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def enableStaticNat(**kargs):
    """ Enable Static Nat for Your IP
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - ipaddressid(String, Required) : Public IP address ID
        - vmid(String, Required) : VirtualMachine ID
    * Examples : print(server.enableStaticNat(zone='KR-M', ipaddressid='3a304bed-d7c0-4836-a31f-c4e10d2ab0be', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'ipaddressid' in kargs:
        return '[ktcloud] Missing required argument \"ipaddressid\" '
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'enableStaticNat'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def disableStaticNat(**kargs):
    """ Disable Static Nat for Your IP
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - ipaddressid(String, Required) : Public IP address ID
    * Examples : print(server.disableStaticNat(zone='KR-M', ipaddressid='3a304bed-d7c0-4836-a31f-c4e10d2ab0be'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'ipaddressid' in kargs:
        return '[ktcloud] Missing required argument \"ipaddressid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'disableStaticNat'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createOverlayNetwork(**kargs):
    """ Create Overlay(CloudLink) Network
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Required) : OverlayNetwork Name
        - displaytext(String, Required) : OverlayNetwork Name
        - netmask(String, Required) : netmask
        - gateway(String, Required) : gateway
        - startip(String, Required) : startip
        - endip(String, Required) : endip
        - overlayid(String, Required) : Overlay ID
    * Examples : 
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument \"name\" '
    if not 'displaytext' in kargs:
        return '[ktcloud] Missing required argument \"displaytext\" '
    if not 'netmask' in kargs:
        return '[ktcloud] Missing required argument \"netmask\" '
    if not 'gateway' in kargs:
        return '[ktcloud] Missing required argument \"gateway\" '
    if not 'startip' in kargs:
        return '[ktcloud] Missing required argument \"startip\" '
    if not 'endip' in kargs:
        return '[ktcloud] Missing required argument \"endip\" '
    if not 'overlayid' in kargs:
        return '[ktcloud] Missing required argument \"overlayid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createOverlayNetwork'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateVirtualMachineForCharge(**kargs):
    """ Change usageplantype of your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required) : Your VM ID To Change
        - usageplantype(String, Required) : monthly or hourly
    * Examples : print(server.updateVirtualMachineForCharge(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7', usageplantype='hourly'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\" '
    if not 'usageplantype' in kargs:
        return '[ktcloud] Missing required argument \"usageplantype\" (monthly or hourly)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'updateVirtualMachineForCharge'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listAvailableProductTypes(**kargs):
    """ Combinations of templateid, serviceofferingid, diskofferingid, zoneid
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listAvailableProductTypes(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listAvailableProductTypes'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listVirtualMachines(**kargs):
    """ List VirtualMachines
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listVirtualMachines(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listVirtualMachines'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def checkVirtualMachineName(**kargs):
    """ Check if name is available or not
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.checkVirtualMachineName(zone='KR-M', display_name='AAA'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'checkVirtualMachineName'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listVirtualMachineForCharge(**kargs):
    """ List of VirtualMahcine usageplantype
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Optional) : Select VM ID To Check usageplantype
    * Examples : print(server.listVirtualMachineForCharge(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    if 'vmid' in kargs:
        kargs['id'] = kargs['vmid']
        del kargs['vmid']    
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listVirtualMachineForCharge'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listPublicIpAddresses(**kargs):
    """ List of Public IP Address
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listPublicIpAddresses(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listPublicIpAddresses'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listPortForwardingRules(**kargs):
    """ List of PortForwarding Rule Set
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listPortForwardingRules(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listPortForwardingRules'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listFirewallRules(**kargs):
    """ List of Firewall Rule Set
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listFirewallRules(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listFirewallRules'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listAccounts(**kargs):
    """ List of Accounts
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listAccounts(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listAccounts'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listEvents(**kargs):
    """ List of User Events
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listEvents(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listEvents'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listSnapshots(**kargs):
    """ List of Volume Snapshots
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listSnapshots(zone='KR-M'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listSnapshots'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listSnapshotSize(**kargs):
    """ List of Volume Snapshots Size
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listSnapshotSize(zone='KR-M2'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listSnapshotSize'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listTemplates(**kargs):
    """ List of Templates (OS images)
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - templatefilter(String, Required) : self or selfexecutable
    * Examples : print(server.listTemplates(zone='KR-M', templatefilter='self'))
    """
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'templatefilter' in kargs:
        return '[ktcloud] Missing required argument \"templatefilter\" (self or selfexecutable)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listTemplates'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listNetworks(**kargs):
    """ List Networks
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listNetworks(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listNetworks'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listNetworkFlatRate(**kargs):
    """ List NetworkFlatRate
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listNetworkFlatRate(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listNetworkFlatRate'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listNetworkUsages(**kargs):
    """ List NetworkUsages
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - startdate(String, Required) : StartDay To inquiry Usage (YYYY-MM-DD)
        - enddate(String, Required) : EndDay To inquiry Usage (YYYY-MM-DD, Within 1 month)
    * Examples : print(server.listNetworkUsages(zone='KR-M', startdate='2020-11-1', enddate='2020-11-18'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'startdate' in kargs:
        return '[ktcloud] Missing required argument \"startdate\" (YYYY-MM-DD)'
    if not 'enddate' in kargs:
        return '[ktcloud] Missing required argument \"enddate\" (YYYY-MM-DD, Within 1 month)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listNetworkUsages'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listZones(**kargs):
    """ List Zones
    * Examples : print(server.listZones())
    """    
    import time
    my_apikey, my_secretkey = c.read_config()

    kargs['command'] = 'listZones'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey

    baseurl1 = c.geturl(ctype='server', m2=False)
    baseurl2 = c.geturl(ctype='server', m2=True)
    req1 = c.makerequest(kargs, baseurl1, my_secretkey)
    time.sleep(1)
    req2 = c.makerequest(kargs, baseurl2, my_secretkey)
    if('count' in req1['listzonesresponse']):
        if('count' in req2['listzonesresponse']):
            req = {'listzonesresponse':{'zone':req1['listzonesresponse']['zone']+req2['listzonesresponse']['zone']}}
            # log.info(json.dumps(req, indent=3))
            return req
        else:
            # log.info(json.dumps(req1, indent=3))
            return req1
    else:
        if('count' in req2['listzonesresponse']):
            # log.info(json.dumps(req2, indent=3))
            return req2


def listSSHKeyPairs(**kargs):
    """ List SSH Key Pairs
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - name(String, Optional) : SSH Key Pair Name To inquiry
    * Examples : print(server.listSSHKeyPairs(zone='KR-M', name='MyKey'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listSSHKeyPairs'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listTags(**kargs):
    """ List Tags
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
    * Examples : print(server.listTags(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listTags'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def listVolumes(**kargs):
    """ List Volumes
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Optional) : VirtualMachine ID
    * Examples : print(server.listVolumes(zone='KR-M'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['virtualmachineid'] = kargs['vmid']
    del kargs['vmid']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'listVolumes'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def resetPasswordForVirtualMachine(**kargs):
    """ Reset Password for your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required) : VM ID To Reset Password
    * Examples : print(server.resetPasswordForVirtualMachine(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\"'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'resetPasswordForVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def changeServiceForVirtualMachine(**kargs):
    """ Change Spec your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required) : VM ID To Change Spec
        - serviceofferingid(String, Required) : Spec
    * Examples : print(server.changeServiceForVirtualMachine(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7', serviceofferingid='dfd1a951-726b-4ac7-955f-5419554844c9'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\" '
    if not 'serviceofferingid' in kargs:
        return '[ktcloud] Missing required argument \"serviceofferingid\" (See listAvailableProductTypes)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'changeServiceForVirtualMachine'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateUsagePlanTypeForServer(**kargs):
    """ Change usagePlanType your disk or ip
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - type(String, Required) : disk or ip
        - usagePlanType(String, Required) : hourly or monthly
        - id(String, Required) : your disk ID or IP ID To Change usagePlanType
    * Examples : print(server.updateUsagePlanTypeForServer(zone='KR-M', type='disk', usagePlanType='hourly', id='6f08d33e-1187-4d1e-be40-e24fd638280c'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'type' in kargs:
        return '[ktcloud] Missing required argument \"type\" '
    if not 'usagePlanType' in kargs:
        return '[ktcloud] Missing required argument \"usagePlanType\" (hourly or monthly)'
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (disk ID or IP ID)'    
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'updateUsagePlanTypeForServer'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def changeServiceForVirtualMachineVerify(**kargs):
    """ Checks whether the product can be changed
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - vmid(String, Required) : VM ID
           * Required 1 of below 2 options
        - serviceofferingid(String, Optional) : serviceofferingid
        - serviceofferingcode(String, Optional) : serviceofferingcode
    * Examples : print(server.changeServiceForVirtualMachineVerify(zone='KR-M', vmid='47d2ea4c-d434-418b-a854-c99054abeff7', serviceofferingid='dfd1a951-726b-4ac7-955f-5419554844c9'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'vmid' in kargs:
        return '[ktcloud] Missing required argument \"vmid\" '
    if not 'serviceofferingid' in kargs and not 'serviceofferingcode' in kargs:
        return '[ktcloud] Missing required argument \"serviceofferingid or serviceofferingcode\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone']
    kargs['id'] = kargs['vmid']
    del kargs['vmid']    
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'changeServiceForVirtualMachineVerify'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createSnapshot(**kargs):
    """ Create Snapshot of your Volume
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - volumeid(String, Required) : Volumeid ID
    * Examples : print(server.createSnapshot(zone='KR-M', volumeid='83617062-0aa4-4c18-8b04-a810c2bbb597'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'volumeid' in kargs:
        return '[ktcloud] Missing required argument \"volumeid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createSnapshot'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteSnapshot(**kargs):
    """ Delete Snapshot of your Volume
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Snapshot ID
    * Examples : 
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (Snapshot ID)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deleteSnapshot'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createTemplate(**kargs):
    """ Create Template (OS Image) of Your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - displaytext(String, Required) : CreateTemplate Name
        - name(String, Required) : CreateTemplate Name
        - ostypeid(String, Required) : ostypeid
           * Required 1 of below 2 options (volumeid or snapshotid)
        - volumeid(String, Optional) : volumeid
        - snapshotid(String, Optional) : snapshotid
    * Examples : print(server.createTemplate(zone='KR-M', displaytext='AAATest', name='AAATest', ostypeid='69a99f0e-4299-11e9-8624-1e00d900072f', volumeid='83617062-0aa4-4c18-8b04-a810c2bbb597'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'displaytext' in kargs:
        return '[ktcloud] Missing required argument \"displaytext\" '
    if not 'name' in kargs:
        return '[ktcloud] Missing required argument \"name\" '
    if not 'ostypeid' in kargs:
        return '[ktcloud] Missing required argument \"ostypeid\" (See listVirtualMachines guestosid)'
    if not 'volumeid' in kargs and not 'snapshotid' in kargs:
        return '[ktcloud] Missing required argument \"volumeid or snapshotid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'createTemplate'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def deleteTemplate(**kargs):
    """ Delete Template (OS Image) of Your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Template ID
    * Examples : print(server.deleteSnapshot(zone='KR-M', id='6a59215f-df8b-4633-9a55-c42ac41b3467'))
    """    
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (Template ID)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'deleteTemplate'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def updateTemplate(**kargs):
    """ Update Template (OS Image) displaytext of Your VM
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Template ID
        - displaytext(String, Required) : Template name
    * Examples : print(server.updateTemplate(zone='KR-M', id='d3bb554d-116c-495f-bcb2-bca65f607605', displaytext='ATestABCD'))
    """ 
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (Template ID)'
    if not 'displaytext' in kargs:
        return '[ktcloud] Missing required argument \"displaytext\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'updateTemplate'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def copyTemplate(**kargs):
    """ Copy Template (OS Image) from Source-Zone To Dest-Zone 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - id(String, Required) : Template ID
        - sourcezoneid(String, Required) : Template Source-Zone
        - destzoneid(String, Required) : Template Dest-Zone
    * Examples : print(server.copyTemplate(zone='KR-M', id='d3bb554d-116c-495f-bcb2-bca65f607605', sourcezoneid='95e2f517-d64a-4866-8585-5177c256f7c7', destzoneid='eceb5d65-6571-4696-875f-5a17949f3317')) # from M-zone To A-Zone
    """ 
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'id' in kargs:
        return '[ktcloud] Missing required argument \"id\" (Template ID)'
    if not 'sourcezoneid' in kargs:
        return '[ktcloud] Missing required argument \"sourcezoneid\" '
    if not 'destzoneid' in kargs:
        return '[ktcloud] Missing required argument \"destzoneid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'copyTemplate'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def createTags(**kargs):
    """ Create Tag for your Resources 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - resourceids(String, Required) : resource id (ex.VMID)
        - resourcetype(String, Required) : userVm, Template, ISO, Volume, Snapshot,Network, PortForwardingRule, FirewallRule
    * Examples : mytags = {'key':'os', 'value':'centos'}
        print(server.createTags(zone='KR-M', resourceids='47d2ea4c-d434-418b-a854-c99054abeff7', resourcetype='userVm', mytagkey=mytags['key'], mytagvalue=mytags['value']))
    """ 
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'resourceids' in kargs:
        return '[ktcloud] Missing required argument \"resourceids\" (ex.VMID)'
    if not 'resourcetype' in kargs:
        return '[ktcloud] Missing required argument \"sourcezoneid\" (userVm, Template, ISO, Volume, Snapshot,Network, PortForwardingRule, FirewallRule)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)
    kargs['tags[0].key']=kargs['mytagkey']
    kargs['tags[0].value']=kargs['mytagvalue']
    del kargs['mytagkey']
    del kargs['mytagvalue']

    kargs['command'] = 'createTags'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)

def deleteTags(**kargs):
    """ Delete Tag for your Resources 
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - resourceids(String, Required) : resource id (ex.VMID)
        - resourcetype(String, Required) : userVm, Template, ISO, Volume, Snapshot,Network, PortForwardingRule, FirewallRule
    * Examples : mytags = {'key':'os', 'value':'centos'}
        print(server.deleteTags(zone='KR-M', resourceids='47d2ea4c-d434-418b-a854-c99054abeff7', resourcetype='userVm', mytagkey=mytags['key'], mytagvalue=mytags['value']))
    """ 
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'resourceids' in kargs:
        return '[ktcloud] Missing required argument \"resourceids\" (ex.VMID)'
    if not 'resourcetype' in kargs:
        return '[ktcloud] Missing required argument \"sourcezoneid\" (userVm, Template, ISO, Volume, Snapshot,Network, PortForwardingRule, FirewallRule)'
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)
    kargs['tags[0].key']=kargs['mytagkey']
    kargs['tags[0].value']=kargs['mytagvalue']
    del kargs['mytagkey']
    del kargs['mytagvalue']

    kargs['command'] = 'deleteTags'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)


def queryAsyncJobResult(**kargs):
    """ Check Async Job Result
    * Args:
        - zone(String, Required) : [KR-CA, KR-CB, KR-M, KR-M2]
        - jobid(String, Required) : jobid To check result
    * Examples : print(server.queryAsyncJobResult(zone='KR-M', jobid='c929772e-a487-4657-8ccc-23f5905c8185'))
    """ 
    my_apikey, my_secretkey = c.read_config()

    if not 'zone' in kargs:
        return c.printZoneHelp()
    if not 'jobid' in kargs:
        return '[ktcloud] Missing required argument \"jobid\" '
    kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
    M2Bool = c.IsM2(kargs['zone'])
    del kargs['zone'] 
    baseurl = c.geturl(ctype='server', m2=M2Bool)

    kargs['command'] = 'queryAsyncJobResult'
    kargs['response'] = 'json'
    kargs['apikey'] = my_apikey
    return c.makerequest(kargs, baseurl, my_secretkey)
# End Of File
