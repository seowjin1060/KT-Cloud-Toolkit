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
import sys
import os
import common as c


def Print_Welcome():
    print('-----------------------------------------------------------------------------------------------------------------')
    print('[ktcloud] ctype    :  server database loadbalancer gslb nas waf  ')
    print('[ktcloud] command  :  See Ref. https://cloud.kt.com/portal/openapi-guide/common-api_prologue-intro_api_intro  ')
    print('[ktcloud] Usage    :  python ktcloud.py < ctype > < command > < param_name1=param1, param_name2=param2,, > ')
    print('[ktcloud] example  :  python ktcloud.py server startVirtualMachine zone=KR-M id=yourid ')
    print('                      python ktcloud.py database listInstances ')
    print('-----------------------------------------------------------------------------------------------------------------')
    if len(sys.argv) < 3:
        print('[ktcloud] please check CMD again')
        sys.exit(0)


def Parse_CLI():
    # Parse CLI MSG
    # ktcloud.py server deployVirtualMachine Aid=AAA Bid=BBB Cid=CCC
    #  argv[0]   argv[1]      argv[2]        argv[3] argv[4] argv[5] 
    ctype = sys.argv[1]      
    cmd = sys.argv[2]
    params = sys.argv[3:]
    # if params.find('APIKEY') or params.find('SECKEY'):

    return ctype, cmd, params, my_apikey, my_secretkey


def sendcmd(params, **kargs):
    print('-----------------------------------------------------------------------------------------------------------------')
    print('[ktcloud] Result ')
    for index in params:
        try:
            string_temp = index.split("=")
        except:
            print('[ktcloud] please check again')
            exit(0)
        kargs[string_temp[0]] = string_temp[1]

    if kargs['ctype'] == 'server' and not 'zone' in kargs and kargs['command'] != 'listZones':
        return c.printZoneHelp()
    if 'zone' in kargs:
        kargs['zoneid'] = c.getzoneidbyhname(kargs['zone'])
        M2Bool = c.IsM2(kargs['zone'])
        del kargs['zone']
        baseurl = c.geturl(ctype=kargs['ctype'], m2=M2Bool)
    else:
        baseurl = c.geturl(ctype=kargs['ctype'], m2=False)
    kargs['response'] = 'json'
    del kargs['ctype']
    secretkey = kargs['secretkey']
    del kargs['secretkey']
    print(c.makerequest(kargs, baseurl, secretkey))


# Start
Print_Welcome()
my_apikey = ''
my_secretkey = ''
ctype, cmd, params, my_apikey, my_secretkey = Parse_CLI()
if my_apikey == '' or my_secretkey == '':
    my_apikey, my_secretkey = c.read_config()
print('Input Your MSG : ', ctype, cmd, params)
sendcmd(params, ctype=ctype, command=cmd, apikey=my_apikey, secretkey=my_secretkey)

