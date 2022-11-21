#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
import sys
import logging
import requests
import urllib3
import coloredlogs as coloredlogs

urllib3.disable_warnings()
coloredlogs.install(level="INFO", fmt='%(asctime)s [%(levelname)s] %(message)s',level_styles={
        'info': {'color': 'white', 'bold': False},
        'warn': {'color': 'green', 'bold': True},
        'error': {'color': 'red', 'bold': False}},isatty=True)
def login():
    body ={
        "username":"admin",
        "password":"123"
    }
    header = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    }
    check_txt = 'list.txt'
    succcess_txt = 'success.txt'
    with open(check_txt) as lines:
        for line in lines:
            check_passwd = line + '/login/verify'
            try:
                res_post = requests.post(url=check_passwd,data=body,headers=header,verify=False,timeout=1)
                if res_post.status_code == 200 and ('login success' in res_post.text and '1' in res_post.text):
                    with open(succcess_txt,'a') as success:
                        success.write(line)
                    logging.info(line + '账号密码为:admin/123')
                else:
                    logging.error(line+'账号密码错误')
            except:
                    logging.warning(line + '连接超时')
if __name__ == '__main__':
    login()