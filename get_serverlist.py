# -*- coding: utf-8 -*-
# author: kuangl
# filename get_serverlist.py

import os
import urllib
import urllib2

''' 设置文件名及下载的本地路径 '''
local_dir='/app/www/serverlist'
file_name=['serverlist_all','serverlist_open']
len(file_name)

''' 下载设置 '''
def downLoadPicFromURL(dest_dir,URL):
    try:
        urllib.urlretrieve(url_01 , dest_dir)
    except:
        print '\tError retrieving the URL:', dest_dir

for file_list in file_name:
    print file_list
    dest_dir=os.path.join(local_dir,file_list)

    ''' 设置下载路径 '''
    url_01='http://192.169.1.12/{0}'.format(file_list)
    downLoadPicFromURL(dest_dir,url_01)
