#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: kuangl
# This is backup scripts file
import os
import time,datetime
import string
import shutil

''' 设置变量 '''
SOU_DIR = ['/app/www/','/app/opbin/work','/app/opbin/rundeck']
DSR_DIR='/app/opbak/scripts_bakcup'
now = DSR_DIR + '_' +  time.strftime('%Y%m%d%H%M%S')
target = os.sep + now  + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(SOU_DIR))

''' 创建目录 '''
if not os.path.exists(DSR_DIR):
    os.mkdir(DSR_DIR)
    print 'Successfully created directory', DSR_DIR

''' 备份文件 '''
if os.system(zip_command) == 0:
    print "="*30
    print 'Successful backup to', target
else:
    print "="*30
    print 'Backup "\033[1;31;40m FAILED \033[0m"'

''' 移动备份文件到指定目录 '''
if os.path.exists(target):
    os.chdir('/app/opbak')
    shutil.move(target,DSR_DIR)
    print "="*30
    print 'Move Backup File SUCC'
else:
    print "="*30
    print 'Move Backup File "\033[1;31;40m FAILD \033[0m"'

''' 删除过期的备份文件 '''
os.chdir(DSR_DIR)
os.getcwd()
del_file = os.system('find ./ -name  "*.zip" -mtime +5 |xargs rm -f')
if del_file == 0:
    print 'Delete Backup ZIP File SUCC'
else:
    print 'Delete Backup ZIP File Fail'
