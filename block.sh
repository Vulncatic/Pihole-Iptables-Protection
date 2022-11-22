#!/bin/bash

iptables -A INPUT -s $1 -j DROP
echo $1 >> iplist.txt
