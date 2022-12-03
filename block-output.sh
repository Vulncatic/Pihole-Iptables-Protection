#!/bin/bash

iptables -A OUTPUT -s $1 -j DROP
