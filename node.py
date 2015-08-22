#!/usr/bin/env python
# coding=utf8
# Filename: node.py


import os
import yaml

#定义/srv/pillar/top.sls文件
pillar_top_conf = open('/srv/pillar/test/top.sls', 'w+')
'''
#打开pillar_node_conf.txt，此文件为节点信息配置文件，注意必须为标准的yaml格式, 如
web-ns-vm-10-10-10-30-huzhou.kx1d.com:
    server: 1000
    number: 1001
    money: 1002
'''
PillarNodeConf  = open('pillar_node_conf.txt',  'r')
PillarNodeFile  = yaml.load(PillarNodeConf)
#用for循环生成top.sls和节点pillar文件
for i in range(0,len(PillarNodeFile)):
    #取出自动的key值，即主机名
    key=PillarNodeFile.keys()[i]
    #取出主机的values，即自定义的pillar变量
    values=PillarNodeFile[key]
    #将主机对应的pillar文件名修改为web_ns.10-10-10-30-huzhou.sls这种格式
    node_key=key.replace('\n', '').replace('-ns','_ns').replace('-vm-','.').replace('-py-','.').replace('.kx1d.com','')
    pillar_top_conf_info= "'"+key+"':\n" + "    - " + node_key + "\n" 
    '''
    shell#cat top.sls 
    'web-ns-vm-10-10-10-30-huzhou.kx1d.com':
         - web_ns.10-10-10-30-huzhou
    '''
    pillar_top_conf.write(pillar_top_conf_info)

    #定义文件名，例如web_ns.10-10-10-30-huzhou.sls
    node_pillar_sls=node_key+".sls"
    '''
    #往node节点里面定义pillar变量, web_ns.10-10-10-30-huzhou.sls 
        server: 1000
        number: 1001
        money: 1002
    '''
    pillar_node_file =  open(node_pillar_sls, 'a')
    for i in range(0,len(values)):
        serverkey    = values.keys()[i]
        servervalues = values[serverkey]
        pillar_node_file_info= serverkey+": "+str(servervalues) + "\n"
        pillar_node_file.write(pillar_node_file_info)

    PillarNodeConf.close()
    pillar_node_file.close()
