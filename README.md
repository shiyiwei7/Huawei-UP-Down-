![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/2cdf2d23-e5bd-41b6-8a36-3f74caf14f52)
华为交换机
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
    for i in range(1, 48):       /48指循环查询1-48口的接口状态      
        interface = f"G0/0/{i}"            /注：当接口为同一类型设备那么接口描述相同，如果类型不同需要修改描述存在40G、10G接口
        command.send(f"display interface {interface}\n")
        time.sleep(1)
      
 函数分析，输出结果为UP，时候upport端口+1，依次循环，逐个端口查询状态
       
       if "Line protocol current state : UP" in output:
            up_count += 1
        elif "Line protocol current state : DOWN" in output:
            down_count += 1
       
 设备定义：定义爬取端口信息的设备IP地址
      
ip_addresses = [ "10.50.0.32", "10.50.0.33", "10.50.0.38", "10.50.0.40", "10.50.0.41"]      //表示指定该4台设备进行地址循环查询

ip_addresses = [f"10.50.0.{i}" for i in range(1, 31)]    //表示对1-31台设备的地址进行循环查询



效果展示：
     ![image](https://github.com/shiyiwei7/Huawei-CE-switch-interface-UP-down-statistics/assets/153582486/aae56240-ec4d-43b9-a2b1-16ac444274b0)
