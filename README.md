# dns_pod_ddns_docker

## 说明
通过docker部署的dns_pod_ddns，用于动态更新域名解析记录
## 使用方法
修改ddns_dns_pod.py中DDNS_DNSPOD类的配置信息
```
    #间隔时间 分钟
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
修改send_email.py中send_msg函数的配置信息
```
    # 企业微信机器人 key    
    key = "key-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

## 运行
```
上传项目到服务器 /home/docker/ddns_dnspod  文件位置后面需要用到
``` 

### docker build
```
    docker build . -t ddns_dnspod
```
### 测试
```
    docker run  -it -v /home/docker/ddns_dnspod:/code --rm --name ddns_dnspod_test ddns_dnspod
```
### 后台运行
```
    docker run  -d -v /home/docker/ddns_dnspod:/code --restart=always --name ddns_dnspod ddns_dnspod 
```
