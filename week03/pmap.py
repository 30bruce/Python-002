import os
import sys
import socket
from functools import partial
from concurrent.futures import ThreadPoolExecutor

kv = {}

def ping(ip):
    res = os.system(f"ping -c 1 -W0 {ip} > /dev/null 2>&1")
    if res == 0:
        return ip


def tcp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip, port))
    if result == 0:
        return port
    sock.close()


def get_ips(arg_ip):
    ips = [arg_ip]
    if '-' in arg_ip:
        tmp = arg_ip.split('-')
        ip_splits = tmp[0].split('.')
        ip_prefix = '.'.join(ip_splits[:-1])
        min_ip_int, max_ip_int = int(ip_splits[-1]), int(tmp[1].split('.')[-1])
        ips = []
        max_ip_int = min(255, max_ip_int)
        for i in range(min_ip_int, max_ip_int+1):
            ips.append(f'{ip_prefix}.{i}')
    return ips
    

if __name__ == '__main__':
    # print(sys.argv)
    arg_it = iter(sys.argv[1:])
    kv = dict(zip(arg_it, arg_it))
    ip_val = kv.get('-ip', '')
    if not ip_val:   # 必须有指定ip才能运行
        sys.exit('请输入指定ip')

    ips = get_ips(ip_val)
    # print(ips)
    n = int(kv.get('-n', 1))   # 默认开启一个线程
    f = kv.get('-f', 'ping')
    res = []
    if f == 'tcp':
        ports = (i+1 for i in range(1024))
        with ThreadPoolExecutor(n) as executor:
            func = partial(tcp, ips[0])
            res = executor.map(func, ports)
    else:  # 默认执行 ping
        res = []
        with ThreadPoolExecutor(n) as executor:
            res = executor.map(ping, ips)
    
    if res:
        res = '\n'.join([f'{i}' for i in res if i])
        print(res)
        w_path = kv.get('-w', '')
        if w_path:
            with open(w_path, 'w') as f:
                f.write(res)
        
    
    

    


