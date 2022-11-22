#!/usr/bin/env python3

import os

term = 'blacklist> '
while True:
	cmd = input(term)
	os.system(f"iptables -A INPUT -s {cmd} -j DROP && echo {cmd} >> /root/iplist.txt")

