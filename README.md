# WePushMsg-Server 微信消息推送服务器
![status](https://img.shields.io/badge/status-developing-red.svg) ![py3x](https://img.shields.io/badge/python-3.x-blue.svg)
## 简介
本项目是微信消息推送系统的一环，旨在微信关闭的情况下也能获得微信消息推送。

此为服务器端，作为推送者。
## 安装
本项目仅使用了[youfou/wxpy](https://github.com/youfou/wxpy)项目为依赖

安装方式：

`pip3 install -U wxpy`

将本项目clone到你的目录，在目录中运行start.py即可开启服务器：

`python3 start.py`

可以通过配置`config.json`修改服务器信息

本项目自带一个测试客户端`test_client.py`，可以测试服务器可用性：

`python3 test_client.py`

其服务器信息编码在程序内，请自行修改
### 2018.1.26 项目立项
