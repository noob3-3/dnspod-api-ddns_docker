from loguru import logger
from send_msg import send_msg
import requests
import time

logger.add("file.log", retention="1days")



class DDNS_DNSPOD():
    def __init__(self):
        #间隔时间
        self.sleep = 5
        #dns_pod 登录token
        #可从这里获取 https://console.dnspod.cn/account/token/token
        self.dnspod_id = "3600xx"
        self.dnspod_token = "39xx39b0xxb8xxd674xx00b5xxedfxxa"
        #域名和前缀
        self.domain = "3dpxxcexxion.cxx.cn"
        self. prefix = "pan"
        #记录类型
        self.record_type = "A"
        self.ip = "0.0.0.0"

        self.login_token =f"{self.dnspod_id},{self.dnspod_token}"
        self.record_id = None
        self.run()


    def get_public_ip(self):
        try:
            r = requests.get("http://ipinfo.io/ip", timeout=10)
            ip = r.text.strip()
            return ip
        except Exception as e:
            logger.error(e)
            return False

    def get_dns_vlan(self):
        url = "https://dnsapi.cn/Record.List"
        payload = {
            "login_token":self.login_token,
            "domain":self.domain}
        response = requests.request("POST", url, data=payload)
        json_data = response.json()
        for name in json_data['records']:
            if "pan"==name['name']:
                self.record_id = name['id']
                return name['value']


    def update_ip(self,new_ip):
        url = "https://dnsapi.cn/Record.Modify"
        payload = {"login_token":self.login_token,
                   "domain":self.domain,
                   "record_id":self.record_id,
                   "sub_domain":self.prefix,
                   "record_type":self.record_type,
                   "record_line_id":"0",
                   "value":new_ip}
        response = requests.request("POST", url, data=payload)
        json_data = response.json()
        if json_data['status']['code'] != "1":
            logger.error("更新IP失败")
            self.sendMeg("更新IP失败 {}\n ip地址 {}".format(json_data['status']['message'],self.ip))
        else:
            #保存ip到文件文件名和域名关联
            with open("{}.{}.txt".format(self.prefix,self.domain),"w") as f:
                f.write(new_ip)

    #获取文件中的IP
    def get_file_ip(self):
        try:
            with open("{}.{}.txt".format(self.prefix,self.domain),"r") as f:
                return f.read()
        except Exception as e:
            logger.error(e)
            return False

    def ll(self):
        #获取公网IP
        self.ip = self.get_public_ip()
        #判断IP和文件中的IP是否一致
        if self.ip == self.get_file_ip():
            logger.debug("文件 IP一致")
        else:
            #获取域名解析IP
            dns_ip = self.get_dns_vlan()
            if self.ip != dns_ip:
                #更新域名解析IP
                self.update_ip(self.ip)
                logger.info("更新IP成功")
                self.sendMeg("更新IP成功 IP {}".format(self.ip))
            else:
                # self.update_ip("0.0.0.0")
                logger.debug("域名 IP一致")


    def run(self):
        while True:
            self.ll()
            time.sleep(60*self.sleep)

    def sendMeg(self,msg):
        send_msg("{}".format(msg))



if __name__ == '__main__':
    w = DDNS_DNSPOD()


