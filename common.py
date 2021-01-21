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
import os
import sys    
import platform
import urllib
import base64
import hmac
import hashlib
import requests
import json
import pandas as pd


ZONE_LIST = pd.DataFrame(
    [['A', 'kr-1', 'KR-CA', 'KOR-Central A', 'eceb5d65-6571-4696-875f-5a17949f3317'],
    ['B', 'kr-2', 'KR-CB', 'KOR-Central B', '9845bd17-d438-4bde-816d-1b12f37d5080'],
    ['M', 'kr-0', 'KR-M', 'KOR-Seoul M', '95e2f517-d64a-4866-8585-5177c256f7c7'],
    ['M2', 'kr-m2', 'KR-M2', 'KOR-Seoul M2', 'd7d0177e-6cda-404a-a46f-a5b356d2874e'],
    ['US', 'usw-0', 'USW-0', 'US-West', 'b7eb18c8-876d-4dc6-9215-3bd455bb05be'],
    ['H', 'kr-3', 'KR-H', 'KOR-HA', 'dfd6f03d-dae5-458e-a2ea-cb6a55d0d994']],
    columns=['zone_ssname', 'zone_sname', 'zone_hname', 'zone_fname', 'zone_id'])


def printZoneHelp():
    print('Missing required argument \"zone\" \n \
  - KR-CA : KOREA-Central A Zone \n \
  - KR-CB : KOREA-Central B Zone \n \
  - KR-M  : KOREA M Zone  \n \
  - KR-M2 : KOREA M2 Zone ')
  

def getzoneidbyhname(hname):
    global ZONE_LIST
    for index in ZONE_LIST.index:
        if str(ZONE_LIST.loc[index, 'zone_hname']) == hname:
            return str(ZONE_LIST.loc[index, 'zone_id'])
    return 'error'


def getzonesnamebyhname(hname):
    global ZONE_LIST
    for index in ZONE_LIST.index:
        if str(ZONE_LIST.loc[index, 'zone_hname']) == hname:
            return str(ZONE_LIST.loc[index, 'zone_sname'])
    return 'error'


def IsM2(hname):
    global ZONE_LIST
    if hname.lower() == 'kr-m2':
        return True
    return False


def geturl(**args):
    if args['ctype'] == 'server' and args['m2'] == False:
        return 'https://api.ucloudbiz.olleh.com/server/v1/client/api?'
    elif args['ctype'] == 'server' and args['m2'] == True:
        return 'https://api.ucloudbiz.olleh.com/server/v2/client/api?'
    elif args['ctype'] == 'database' and args['m2'] == False:
        return 'https://api.ucloudbiz.olleh.com/db/v1/client/api?'
    elif args['ctype'] == 'database' and args['m2'] == True:
        return 'https://api.ucloudbiz.olleh.com/db/v2/client/api?'
    elif args['ctype'] == 'autoscaling':
        return 'https://api.ucloudbiz.olleh.com/autoscaling/v1/client/api?'
    elif args['ctype'] == 'waf' and args['m2'] == False:
        return 'https://api.ucloudbiz.olleh.com/waf/v1/client/api?'
    elif args['ctype'] == 'waf' and args['m2'] == True:
        return 'https://api.ucloudbiz.olleh.com/waf/v2/client/api?'
    elif args['ctype'] == 'nas' and args['m2'] == False:
        return 'https://api.ucloudbiz.olleh.com/nas/v1/client/api?'
    elif args['ctype'] == 'nas' and args['m2'] == True:
        return 'https://api.ucloudbiz.olleh.com/nas/v2/client/api?'
    elif args['ctype'] == 'loadbalancer' and args['m2'] == False:
        return 'https://api.ucloudbiz.olleh.com/loadbalancer/v1/client/api?'
    elif args['ctype'] == 'loadbalancer' and args['m2'] == True:
        return 'https://api.ucloudbiz.olleh.com/loadbalancer/v2/client/api?'
    elif args['ctype'] == 'gslb' and args['m2'] == False:
        return 'https://api.ucloudbiz.olleh.com/gslb/v1/client/api?'
    elif args['ctype'] == 'gslb' and args['m2'] == True:
        return 'https://api.ucloudbiz.olleh.com/gslb/v2/client/api?'
    else:
        return 'error'


def set_config_env():
    my_apikey = input('[ktcloud] api_key : ')
    my_secretkey = input('[ktcloud] secret key : ')
    os.environ['KTCAPI'] = my_apikey
    os.environ['KTCSEC'] = my_secretkey
    print('[ktcloud] After the command is executed, the KEY VALUE will be volatilized.')
    print('[ktcloud] So use the EXPORT(SET) CMD like in the following example.')
    print('-----------------------------------------------------------------------------------------------------------------')
    print('[ktcloud] #>export KTCAPI=yourkey   (linux cmd. use set in windows)')
    print('[ktcloud] #>export KTCSEC=yourkey   (linux cmd. use set in windows)')
    print('-----------------------------------------------------------------------------------------------------------------')


def read_config_env():
    return os.environ['KTCAPI'], os.environ['KTCSEC']


def read_config():
    # read OS Environment
    if not 'KTCAPI' in os.environ or not 'KTCSEC' in os.environ: 
        set_config_env()
    my_apikey, my_secretkey = read_config_env()
    return my_apikey, my_secretkey


def makerequest(request, baseurl, my_secretkey):
    secret_key = bytes(my_secretkey, 'UTF-8')
    sig_str = '&'.join(['='.join([k,urllib.parse.quote_plus(request[k]).replace('+','%20')]) for k in sorted(request.keys(), key=str.lower)])
    make_request = bytes(sig_str, 'UTF-8')
    sig = urllib.parse.quote_plus(base64.b64encode(hmac.new(secret_key, make_request.lower(), digestmod=hashlib.sha1).digest()))
    req=baseurl+sig_str+'&signature='+sig
    response = requests.get(req)
    res = response.json()
    return res


def makerequest_debug(request, baseurl, my_secretkey):
    secret_key = bytes(my_secretkey, 'UTF-8')
    sig_str = '&'.join(['='.join([k,urllib.parse.quote_plus(request[k]).replace('+','%20')]) for k in sorted(request.keys(), key=str.lower)])
    make_request = bytes(sig_str, 'UTF-8')
    sig = urllib.parse.quote_plus(base64.b64encode(hmac.new(secret_key, make_request.lower(), digestmod=hashlib.sha1).digest()))
    req=baseurl+sig_str+'&signature='+sig
    print(req)
    response = requests.get(req)
    res = response.json()
    return res

