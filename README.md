![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/2cdf2d23-e5bd-41b6-8a36-3f74caf14f52)华为交换机

型号：CE6856
版本  FM6857-48S6CQ-EI
图片：![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/6e3f4df3-f43e-4e5d-a21b-fe60c6a0501b)

背景：需要统计下设备接口的UP/Down信息

已知条件：设备的账号密码
         设备的登录地址

环境：Python
依赖包：paramiko 
![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/fb09297b-bdb8-4bb0-a483-42a5d1d9979a)

原理：控制台登录指定交换后，使用命令输出接口up/down状态
      ![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/b8a75e40-4b7d-4420-950b-919e7502fa9e)

      函数分析，输出结果为UP，时候upport端口+1，依次循环，逐个端口查询状态
      ![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/3c2f6957-17fe-4b43-918d-9d2ab6ad863a)

      设备定义：定义爬取端口信息的设备IP地址
      ![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/b8371df6-806a-431d-80d1-401132db4ab4)

效果展示：
![Uploading image.png…]()
