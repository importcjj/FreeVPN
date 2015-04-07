# coding:utf-8
__author__ = 'cjj'

import os
import urllib2

helpcontent = \
    u"""如何设置一个VPN连接.

    步骤1: 右键单击你的网络连接图标

    步骤2: 选择打开网络和共享中心

    步骤3: 在出现的面板中选择 设置新的连接和网络

    步骤4: 选择连接到工作区,单击下一步

    步骤5: 选择创建新连接,单击下一步

    步骤6: 选择使用我的Internet连接

    步骤7: 填写下方IP地址和连接名称(英文),不勾选记住凭证

    步骤8: 完成创建

    """


class Vpn(object):
    def __init__(self):
        self.IP_address = '104.237.156.248'
        self.username = 'www.i-vpn.net'
        self.connectionname = self.__configure()
        if not self.connectionname:
            self.__connectionname()

    def __connectionname(self):
        print helpcontent
        print u"请设置一个VPN"
        print u"Internet地址:%s" % self.IPaddress
        while True:
            self.connectionname = raw_input(u"输入目标名称:".encode('gbk'))
            print u"is[%s](y/n)? " % self.connectionname,
            Is_check = raw_input()
            if Is_check == 'y' or Is_check == 'Y':
                break
            print
        with open(r'VPNdata\vpn.config', 'w+') as f:
            f.write('connectionname=%s' % self.connectionname)
        os.system('cls')

    def __configure(self):
        soft_path = os.getcwd()
        # print soft_path
        if 'VPNdata' not in os.listdir(soft_path):
            os.mkdir('VPNdata')
        with open(r'VPNdata\vpn.config', 'a+') as f:
            config = f.read().strip('\n')
        index = config.find('connectionname=')
        connectionname = config[index + 15:]
        return connectionname

    def __get_pwd(self):
        pwd_url = 'http://104.237.156.248/mm.txt'
        req = urllib2.Request(pwd_url)
        req.add_header(
            'User-Agent',
            'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36')
        try:
            page_html = urllib2.urlopen(req).read()
            password = page_html.strip()
        except:
            print "Can't open the url..."
        return password

    def connect(self):
        self.password = self.__get_pwd()
        open_command = 'rasdial %s %s %s' % (
            self.connectionname, self.username, self.password)
        print os.system(open_command)

    def close(self):
        close_command = 'rasdial %s /disconnect ' % self.connectionname
        print os.system(close_command)


def connction(vpn):
    vpn.connect()
    print


def shutdown(vpn):
    print u"正在断开 vpn..."
    vpn.close()
    print


def reconnect(vpn):
    vpn.close()
    v = Vpn()
    v.connect()
    # print
    # print u"status:已经连接"
    # print
    return v


if __name__ == '__main__':
    v = Vpn()
    print u"""
 (__)　　　　                   author:cjj
 /oo\\________                  notes: 仅供内部交流使用
 \　/　　　　 \---\                  
  \/　　　 /　 \　 \  Niu VPN        
　　\\_|___\\_|/　　*                  1. 连接   
　　  ||　 YY|                       2. 断开
　　  ||　　||  　　　　             3. 重连
    """
    print "*" * 80
    while True:
        while True:
            choose = raw_input("choose: ")
            print
            if choose in ['1', '2', '3']:
                break
        if choose == '1':
            connction(v)
        elif choose == '2':
            shutdown(v)
        else:
            v = reconnect(v)
