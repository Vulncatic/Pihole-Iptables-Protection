# Pihole-Iptables-Protection
This Is A Simple Python Script With A List of ip's To Block With Iptables

This Is A Python And A bash Script That Blocks Ip's With iptables I Made This repository Because Pihole doesn't have Many Options To Protect Pihole server's That Act As Open Resolver's
I Use My Pihole Server For me And my grandmother And She's In A Different Network Than Me

If The Pihole Developer's See This Please Add Some Advanced iptables Setting In The Web Interface Just Like How You Can Block Domain's From Resolving It Would Block Those Ip's From Connecting To Your Pihole Server


Btw After U Set An iptables rule to save it Run This

if Your on CentOS/RHEL/Fedora, you can save the Iptables rule with the following command

service iptables save

On Ubuntu/Debian, you must install the iptables-persistent package in your system. You can install it with the following command

apt-get update -y && apt-get install iptables-persistent -y

Once installed, you can save the Iptables rule with the following command

service netfilter-persistent save


