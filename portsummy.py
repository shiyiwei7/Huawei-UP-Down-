import paramiko
import time
import re


def count_interface_status(target_ip, target_username, target_password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(target_ip, username=target_username, password=target_password)

    command = ssh.invoke_shell()
    command.send("screen-length 10 temporary\n")
    time.sleep(1)

    command.send("sys\n")
    time.sleep(1)
    output = command.recv(65535).decode()

    up_count = 0
    down_count = 0

    for i in range(1, 48):
        interface = f"G0/0/{i}"
        command.send(f"display interface {interface}\n")
        time.sleep(1)

        output = ""
        while True:
            page = command.recv(65535)
            page = page.decode("ASCII")
            output += page
            time.sleep(0.1)
            if page.endswith('>') or page.endswith(']'):
                break
            if "  ---- More ----" in page:
                command.send(" ")

        output = re.sub(r"  ---- More ----.*16D", "", output)

        if "Line protocol current state : UP" in output:
            up_count += 1
        elif "Line protocol current state : DOWN" in output:
            down_count += 1

    ssh.close()

    return up_count, down_count


# Replace with your actual IP address, username, and password
ip_addresses = [ "10.50.0.32", "10.50.0.33", "10.50.0.38", "10.50.0.40", "10.50.0.41"]
username = "gscddcn"
password = "Huawei@123"

for ip in ip_addresses:
    up, down = count_interface_status(ip, username, password)
    print(f"IP: {ip}")
    print(f"处于'up'状态的接口数量：{up}")
    print(f"处于'down'状态的接口数量：{down}")
    print("-" * 20)