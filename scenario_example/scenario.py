from time import sleep
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
import server
import loadbalancer as lb

# 1. Check whether there is or not default VM OS Template
# 1-1. If find, Go Step 2
# 1-2. If no exists, stop Your Default VM and Create OS Template image from your VM
# 2. Create loadbalancer
# 3. Create VM(Webserver)
# 4. Attach loadbalancer to your created VM(WebServer)
# 5. Repeat a certain Times Step 3~4

# ----------------------Input-----------------------------
#     Default_zone : Seoul - M Zone
default_zone = 'KR-CB'                                          # Zone:KR-CB
my_vm_id = 'For Your VM ID on your default_zone'                # your VM
vm_serviceoffering_id = '385df834-6cf7-485b-bca8-de4d4f59b0b0'  # 1vCore 1GB
vm_diskoffering_id = '87c0a6f6-c684-4fbe-a393-d8412bcf788d'     # 100GB
ipid = 'For Your Public IP ID on your default_zone'             # public IP ID on KR-CB
ipaddress = 'For Your Public IP on your default_zone'           # public IP addr on KR-CB
lb_name = 'scenariotest'
template_name = 'scenariotest'
deploy_nameheader = 'scenario_vm'
public_port = 80
VM_COUNT = 2
# --------------------------------------------------------

print('[Scenario Start] Create ' + str(VM_COUNT) + '-WebServer from your VM(Webserver) Image')
Exist_VM = False
OSlist = server.listTemplates(zone=default_zone, templatefilter='self', name=template_name)
temp_list = OSlist['listtemplatesresponse']['template']
for x in temp_list:
    temp_name = x.pop('displaytext')
    tem_id = x.pop('id')
    if temp_name == template_name:
        Exist_VM = True
        print('[Step1] Find OS Template Image. ')
    else:
        print('[Step1] No Exists \"scenariotest\" Image. Go to step 1-2')

if not Exist_VM:
    stop_job = server.stopVirtualMachine(zone=default_zone, vmid=my_vm_id)
    if 'errorcode' in stop_job['stopvirtualmachineresponse']:
        if stop_job['stopvirtualmachineresponse']['errortext'] == "VirtualMachine already is stopped.":
            print('[Step1-2] Default VM Ready')
        else:
            raise RuntimeError('[Step1-2] ! Fail Default VM Stop ' + '\n - errortext : ' + stop_job['stopvirtualmachineresponse']['errortext'])
    else:
        while True:
            stopvmres = server.queryAsyncJobResult(zone=default_zone, jobid=stop_job['stopvirtualmachineresponse']['jobid'])
            if(stopvmres['queryasyncjobresultresponse']['jobstatus'] == 1):
                print('[Step1-2] Default VM Stop Complete')
                break
            sleep(10)

    # Get OSID from VirtualMachine List
    list_server = server.listVirtualMachines(zone=default_zone, vmid=my_vm_id)
    server_info = list_server['listvirtualmachinesresponse']['virtualmachine']
    for x in server_info:
        vmosid = x.pop('guestosid')


    # Get VOLID from Volume List
    list_vol = server.listVolumes(zone=default_zone, vmid=my_vm_id, type='ROOT')
    tem_vol = list_vol['listvolumesresponse']['volume']
    for x in tem_vol:
        volid = x.pop('id')


    # Create OS Template Image
    create_tem = server.createTemplate(zone=default_zone, displaytext=template_name, name=template_name, ostypeid=vmosid, volumeid=volid)
    if 'errorcode' in create_tem['createtemplateresponse']:
        raise RuntimeError('[Step1-2] ! Fail Template Creation' + '\n - errortext : ' + create_tem['createtemplateresponse']['errortext'])
    else:
        print('[Step1-2] Please wait. OS Template Image Creating', end='')
        while True:
            temres = server.queryAsyncJobResult(zone=default_zone, jobid=create_tem['createtemplateresponse']['jobid'])
            if(temres['queryasyncjobresultresponse']['jobstatus']==1):
                tem_id = temres['queryasyncjobresultresponse']['jobinstanceid']
                break
            else:
                print('.', end='')
            sleep(10)
        print('    Done!')


lbres = lb.createLoadBalancer(zone=default_zone, name=lb_name, loadbalanceroption='roundrobin', serviceport='80', servicetype='http', healthchecktype='tcp')
if 'errorcode' in lbres['createloadbalancerresponse']:
    raise RuntimeError('[Step2] ! Fail LB Creation ' + '\n - errortext : ' + lbres['createloadbalancerresponse']['errortext'])
else:
    lb_id = lbres['createloadbalancerresponse']['loadbalancerid']
    lb_ip = lbres['createloadbalancerresponse']['serviceip']
    print('[Step2] LB Creation Complete.' + '\n - LB ID : ' + lb_id + '\n - LB IP : ' + lb_ip)


print('[Step3] ' + str(VM_COUNT) + ' VM Create  ')
for i in range(0, VM_COUNT):
    vm_name = deploy_nameheader + str(i)
    vm_id = 'vm_id' + str(i)
    vm_pw = 'vm_pw' + str(i)

    print('[Step3] Please wait a few minutes. ' + str(i+1) + 'th VM Deploying', end='')
    createVM = server.deployVirtualMachine(zone=default_zone, displayname=vm_name, templateid=tem_id, serviceofferingid=vm_serviceoffering_id, diskofferingid=vm_diskoffering_id)
    if 'deployvirtualmachineresponse' in createVM and 'errorcode' in createVM['deployvirtualmachineresponse']:
        raise RuntimeError('[Step3] ! ' + vm_name + ' Fail Deploy' + '\n - errortext : ' + createVM['deployvirtualmachineresponse']['errortext'])
    else:
        while True:
            res = server.queryAsyncJobResult(zone=default_zone, jobid=createVM['deployvirtualmachineresponse']['jobid'])
            if(res['queryasyncjobresultresponse']['jobstatus'] == 1):
                vm_id = createVM['deployvirtualmachineresponse']['id']
                vm_pw = res['queryasyncjobresultresponse']['jobresult']['virtualmachine']['password']
                break
            else:
                print('.', end='')
            sleep(10)
        print('\n[Step3] ' + vm_name + ' Deploy Complete.' + '\n - VM Name : ' + vm_name + '\n - VM ID : ' + vm_id + '\n - VM PassWord : ' + vm_pw)

    print('[Step4] Please wait. LB Attaching', end='')
    while True:
        lb_add = lb.addLoadBalancerWebServer(zone=default_zone, loadbalancerid=lb_id, vmid=vm_id, ipaddress=ipaddress, publicport=str(public_port))
        public_port = public_port + 1

        if (not 'errorcode' in lb_add['addloadbalancerwebserverresponse']) or ('errorcode' in lb_add['addloadbalancerwebserverresponse'] and lb_add['addloadbalancerwebserverresponse']['errorcode'] != "400"):
            break
        else:
            print('.', end='')
        sleep(20)
    print('    Done!')

print('Scenario Finish!')
