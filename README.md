﻿# IRbaby
**中文版 | [English](README_en.md)**

IRbaby 使用 [IRext](https://github.com/irext/irext-core) 开源红外库(**由于某些原因该仓库已关闭,相关网站已下架,但是码库服务仍然提供**)，提供数以万计的红外设备遥控编码。IRbaby 是一个 ESP8266 万能红外方案，配合硬件支持达到类似于市面上售卖的万能红外遥控。并且只需对其进行简单设置就可以快速部署在[HomeAssisant](https://www.home-assistant.io)。

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

---

## 特点

* IRext 强大红外码库
* 基于 ESP8266 的芯片
* 提供 MQTT API
* 提供 UDP API
* 支持录码
* 离线解码
* HomeAssistant 自动发现
* LED 工作指示灯
---

## 架构图
![struction](/src/architecture.svg)
## 开始使用
> 1. **下载 ESP8266 固件并烧写到设备。[IRbaby-firmware](https://github.com/Caffreyfans/IRbaby-firmware/releases)**
> 2. **设备上电，移动端搜索连接到 `ESP**` 信号，并在浏览器中输入 `192.168.4.1` 对设备进行联网设置**
> 3. **下载 `Android` 客户端并运行,对设备进行 MQTT 和红外收发引脚设定。[IRbaby-android](https://github.com/Caffreyfans/IRbaby-android/releases)**
> 4. **匹配电器，完成控制, HomeAssistant 用户可在控制界面导出配置文件（现已支持 HomeAssistant 自动发现功能，设备添加之后，可直接在 HA 集成中看到）**

> **IRbaby目前仍处于开发阶，目前的交互协议可能随时改变，不保证向后兼容，升级新版本时需要注意公告说明同时升级固件和客户端。**

## 六步连接HomeAssistant
**[效果演示视频](https://www.bilibili.com/video/BV13K411j7QD)**

||||
|---|---|---|
|![发现设备](/src/discovery.jpg) |![配置信息](/src/device_setting.jpg) |![添加电器](/src/select.jpg) |
|![匹配电器](/src/parse.jpg) |![已有电器](/src/main.jpg) |![导出MQTT](/src/mqtt.jpg) |

## 材料
### 红外接收头可选(如果需要录码功能)
|||
|---|---|
|![Nodemcu](/src/nodemcu.jpg) | ![红外二级管](/src/ir_led.jpg) |
![红外接收头](/src/ir_receiver.jpg) | ![三级管](/src/transistor.jpg) |

## 关于连线

![接线](/src/connect.jpg)

`备注：红外二级管连接的时候也可以尝试不用三级管，直接连接。红外二级管长引脚接gpio，短脚接地。红外接收头的话就照着上图标示的那样与模块连接。红外接收头非必须，如果你不使用录码功能可忽略红外接收头。只要你有一个红外发射管和一块 ESP8266 和一部 Android 手机就可以尝试该项目。另外目前项目只支持空调控制，其他功能暂不支持，后续会添加。控制客户端目前也只支持 Android，跨平台客户端也在后续添加中`

## 附加下载地址
如果你有在 **github releases** 下载文件过慢的问题，请在 [https://irbaby.caffreyfans.top](https://irbaby.caffreyfans.top) 下在对应文件

## 捐赠
|支付宝|微信|
|---|---|
<img src="/src/donate-alipay.jpg" align="left" height="160" width="160">  |  <img src="/src/donate-wechat.jpg" align="left" height="160" width="160">

## 特别感谢
[Strawmanbobi](https://github.com/strawmanbobi) IRext开源库的作者，给予我技术和精神上的支持。
